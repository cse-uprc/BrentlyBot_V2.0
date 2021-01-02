from flask import Flask, request
import logging
import json

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


@app.route("/print/", methods=['POST'])
def start_recording():
    status = parseString(request.get_data().decode())
    if status['recording']:
        log_message("Recording ...")
    else:
        log_message("Recording Stopped!")

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
