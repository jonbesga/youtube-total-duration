import json
import re
from apiclient.discovery import build

from config import YOUTUBE_API_KEY

service = None

def get_uploads_playlist_id(id=None, forUsername=None):
    response = service.channels().list(part='contentDetails', id=id, forUsername=forUsername).execute()
    return response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

def get_playlist_videos(playlist_id):
    videos = []
    response = service.playlistItems().list(part='contentDetails', playlistId=playlist_id, maxResults=50).execute()
    videos = videos + response['items']
    while 'nextPageToken' in response:
        nextPageToken = response['nextPageToken']
        response = service.playlistItems().list(part='contentDetails', playlistId=playlist_id, maxResults=50, pageToken=nextPageToken).execute()
        videos = videos + response['items']
    return videos

def format_duration(duration):
    p = re.compile('^PT(?:(.*)H)?(?:(.*)M)?(?:(.*)S)?$')
    m = p.match(duration)
    groups = m.groups()
    hours = int(groups[0]) * 60 if groups[0] else 0
    minutes = int(groups[1]) if groups[1] else 0
    seconds = int(groups[2]) / 60 if groups[2] else 0
    return hours + minutes + seconds

def get_video_duration(video_id):
    response = service.videos().list(part='contentDetails', id=video_id).execute()
    duration = response['items'][0]['contentDetails']['duration']
    return format_duration(duration)


def get_channel_duration(data):
    global service
    service = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    results = []
    for channel in data:
        filters = dict()
        filters['id'] = channel['id'] if 'id' in channel else None
        filters['forUsername'] = channel['forUsername'] if 'forUsername' in channel else None

        uploads_id = get_uploads_playlist_id(id=filters['id'], forUsername=filters['forUsername'])
        videos = get_playlist_videos(uploads_id)
        durations = []
        for video in videos:
            durations.append(get_video_duration(video['contentDetails']['videoId']))
        results.append({
            'name': channel['name'],
            'total_duration': sum(durations)
        })
    return results
