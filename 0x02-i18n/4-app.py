#!/usr/bin/env python3
""" Force locale with URL parameter"""
from flask import Flask
from flask_babel import Babel
from flask import render_template, request


class Config:
    """Represents a Flask Babel configuration."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page."""
    requested_locale = request.args.get('locale')
    app.config["LANGUAGES"]

    if requested_locale and requested_locale in app.config["LANGUAGES"]:
        return requested_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """The index page."""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
