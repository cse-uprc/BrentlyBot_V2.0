from flask import Flask, request
import logging
import json
import videoAudio

app = Flask(__name__)
recordingStatus = False

# --------------------------------------------------
# Starts up the UI
# @return none
# --------------------------------------------------


def serve_UI():
    app.run()

# --------------------------------------------------
# Logs a message to the console
#
# @param msg - Message to be logged to the console
# @return none
# --------------------------------------------------


@app.route("/")
def index():
    return home_page()

# --------------------------------------------------
# Logs a message to the console
#
# @param msg - Message to be logged to the console
# @return none
# --------------------------------------------------


@app.route("/record/", methods=['POST'])
def recording():
    status = parseString(request.get_data().decode())
    if status['recording']:
        # videoAudio.record_start()
        log_message("Recording ...")
    else:
        # videoAudio.record_stop()
        log_message("Recording Stopped!")

    return home_page()


@app.route("/saveFile/", methods=['POST'])
def save_file():
    # Add code to acutally save audio and video files
    data = parseString(request.get_data().decode())
    log_message("File's Saved As: " + data['fileName'] +
                ".avi & " + data['fileName'] + ".aud")

    return home_page()

# --------------------------------------------------
# Logs a message to the console
#
# @param msg - Message to be logged to the console
# @return none
# --------------------------------------------------


def home_page():
    file = open("index.html")
    return file.read()

# --------------------------------------------------
# Logs a message to the console
#
# @param msg - Message to be logged to the console
# @return none
# --------------------------------------------------


def log_message(msg):
    logging.basicConfig(format='%(asctime)s - INFO: %(message)s',
                        datefmt='%b-%d-%y %H:%M:%S')
    logging.warning(msg)


def parseString(value):
    return json.loads(value)
