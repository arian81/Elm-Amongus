from flask import Flask, request
from uuid import uuid4
from flask_cors import CORS
import logging
import time

# log = logging.getLogger("werkzeug")
# log.setLevel(logging.ERROR)

app = Flask(__name__)
CORS(app)

data = {}
room = 1

# LOGIN SCHEMA
# id,posX,posY

logInOps = [
    (1, 1000, -758),
    (2, 1154, -761),
    (3, 1077, -822),
    (4, 1070, -710),
    (5, 1000, -758),
    (6, 1000, -758),
    (7, 1000, -758),
    (8, 1000, -758),
]


@app.route("/login")
def login():
    global logInOps
    if logInOps:
        # return ",".join(map(str, logInOps[0]))
        z = logInOps.pop(0)
        data[str(z[0])] = (z[1], z[2], 0, 0)
        return ",".join(map(str, z))

    else:
        return ("", 403)


@app.route("/moved")
def moved():
    data[request.args["id"]] = (
        round(float(request.args["x"])),
        round(float(request.args["y"])),
        int(request.args["a"]),
        int(request.args["f"]),
    )
    # Printing the data to the terminal.
    # print(data)
    return ""


@app.route("/getloc")
def getloc():
    s = ""
    for k in data:
        if k != request.args["id"]:
            mate = data[k]
            s += f"{k},{mate[0]},{mate[1]},{mate[2]},{mate[3]}\n"
    return s
    # return data.values().join


# @app.route("")
import os
print(os.environ['PORT'])
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=os.environ['PORT'])
