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
        short_url = generate_random_id()

        if long_url in shortened_urls.values():
            short_url = list(shortened_urls.keys())[list(shortened_urls.values()).index(long_url)]

        else:
            while short_url in shortened_urls:
                short_url = generate_random_id()
        
            shortened_urls[short_url] = long_url
            url_data[short_url] = {}
            url_data[short_url]["counter"] = 0
            url_data[short_url]["date"] = datetime.datetime.today().date().strftime("%m/%d/%Y")
        
        save_jsons()

        return fl.render_template("shortened.html",
                                  base_url = base_url,
                                  short_url = short_url,
                                  long_url_full = long_url,
                                  long_url = long_url[:40] + "..." if len(long_url) > 40 else long_url) # f"Shortened URL: {fl.request.root_url}{short_url}"
    
    return fl.render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True, port = 80)