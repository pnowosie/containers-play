from flask import Flask, jsonify


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    @app.route('/api')
    def index():
        """
        Backend API response

        :return: Flask response
        """
        return jsonify({
            "author": 'Yoda', 
            "quote": 'Do or do not. There is no try.'
        })


    return app
