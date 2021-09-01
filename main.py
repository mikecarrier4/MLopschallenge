from random import gauss

from flask import Flask, render_template

API = Flask(__name__)


@API.route("/")
def home():
    return render_template(
        "index.html",
        rand_value=gauss(3.14, 5),
    )


if __name__ == '__main__':
    API.run()