# Video durations from Youtube channels

This script answers the question: *How long would it take to see all the videos from a channel?*

## How to use

* Rename the `config_example.py` to `config.py` and fill your API_KEY
* Put the channels that you want to get the total duration from in the `channels.json` file. Use the property _id_ or _forUsername_ depending whether the channel is a user or not (check the URL for that). Check the pre-existent examples in the file.
* Run `python main.py`. It should output the name of the channel along the total duration (in minutes)
