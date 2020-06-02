from flask import Flask, jsonify
from cow_say.models import Quote
from cow_say.extensions import db

def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    db.init_app(app)

    @app.route('/api')
    def index():
        """
        Backend API response

        :return: Flask response
        """
        import random

        quotes = random.sample(Quote.query.all(), k=1)

        return jsonify({
            "author": quotes[0].author,
            "quote": quotes[0].quote
        })


    return app
