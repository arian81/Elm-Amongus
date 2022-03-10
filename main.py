from re import L
from flask import Flask, request
from uuid import uuid4
from flask_cors import CORS
import logging
import time

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

app = Flask(__name__)
CORS(app)

data = {}
room = 1


@app.route("/login")
def login():
    return str(uuid4())


@app.route("/moved")
def moved():
    data[request.args["id"]] = (
        round(float(request.args["x"])),
        round(float(request.args["y"])),
        int(request.args["a"]),
    )
    # Printing the data to the terminal.
    # print(data)
    return ""


@app.route("/getloc")
def getloc():
    d = (
        data.get("blah", (0, 0, 0))
        if request.args["id"] == "bruh"
        else data.get("bruh", (0, 0, 0))
    )
    return f"{d[0]},{d[1]},{d[2]}"


# @app.route("")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
