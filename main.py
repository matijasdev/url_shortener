from flask import Flask, render_template, request, redirect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from queries import get_original_link, increment_click_count, get_stats
from utils import process_url, extract_code
from config import DOMAIN
from db import metadata, engine
import models          # register tables

app = Flask(__name__)

limiter = Limiter(
    key_func=get_remote_address,
    app=app
    )

metadata.create_all(engine)

@app.route("/", methods=["GET", "POST"])
@limiter.limit("30/minute")
def home():
    if request.method == "GET":
        return render_template("index.html")

    url = request.form.get("url", "").strip()

    short_url = process_url(url)

    if short_url is None:
        return render_template("index.html", message="Invalid URL"), 400

    return render_template("index.html", short_url=short_url)


@app.route("/stats")
@limiter.limit("50/minute")
def check_stats():
    user_input = request.args.get("query", "").strip()

    code = extract_code(user_input)

    if not code:
        return render_template("stats_lookup.html")

    stats = get_stats(code)

    if not stats:
        return render_template("stats_lookup.html", message="Invalid code"), 404

    short_url = f"{DOMAIN}/{code}"

    return render_template("stats.html", stats=stats, short_url=short_url)



@app.get("/<code>")
def reroute(code):
    original_link = get_original_link(code)

    if not original_link:
        return render_template("error.html"), 404

    increment_click_count(code)
    return redirect(original_link)



if __name__ == "__main__":
    app.run(debug=False)