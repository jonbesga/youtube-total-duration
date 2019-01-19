from flask import Flask, request
from youtube import get_channel_duration
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def index():
    data = request.get_json() 
    results = get_channel_duration(data)
    return json.dumps(results)