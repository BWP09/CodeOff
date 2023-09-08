import random, string, os, datetime, json, atexit

import flask as fl

app = fl.Flask(__name__)

@app.route("/favicon.ico")
def favicon():
    return fl.send_from_directory(os.path.join(app.root_path, "static"), "favicon.ico", mimetype = "image/vnd.microsoft.icon")

@app.route("/", methods = ["GET", "POST"])
def index():
    if fl.request.method == "POST":
        long_url = fl.request.form["long_url"]

    return fl.render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True, port = 80)