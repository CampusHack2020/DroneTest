from flask import Flask, request, jsonify, send_from_directory
import csv
from PIL import Image
import io
import json
import base64
import time


app = Flask(__name__)
port = 2000


@app.route('/signright')
def handright():
    return {"bruh2": "John Doe", "Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."}


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = port)