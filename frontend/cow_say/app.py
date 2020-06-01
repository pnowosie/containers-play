from flask import Flask, Response
from cow_say import cowsay


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    @app.route('/')
    def index():
        """
        Render a Hello World response.

        :return: Flask response
        """
        return Response(
            cowsay.cow('Beatiful Flask development'),
            status=200, 
            mimetype='text/plain'
        )


    return app