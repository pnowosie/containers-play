from flask import Flask, Response
from cow_say import cowsay
import http.client as HTTP
import requests


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
        resp = requests.get(app.config['BACKEND_URL']+'/api')

        text = 'Sorry ;( Could get to the backend'
        if resp.status_code == HTTP.OK:
            data = resp.json()
            text = data['quote']
            if data['author']:
                text += "\n  -  {}".format(data['author']) 

        return Response(
            cowsay.cow(text),
            status=200, 
            mimetype='text/plain'
        )


    return app
