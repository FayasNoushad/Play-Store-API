# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Play-Store-API/blob/main/LICENSE

from flask import Flask, redirect, request, jsonify, json 
from play_scraper import *


app = Flask(__name__)


@app.route("/")
def main():
    return "Documentation:- <a href='https://github.com/FayasNoushad/Play-Store-API'>Play-Store-API</a>"


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000, use_reloader=True, threaded=True)
