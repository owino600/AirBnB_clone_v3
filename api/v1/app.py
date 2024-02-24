#!/usr/bin/python3
""" Flask Application """
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import environ

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_db(error):
    """Close storage on teardown."""
    storage.close()
    
@app.errorhandler(404)
def not_found(error):
    """404 errors.
    responses:
    404:"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    app.run(host=host, port=port, threaded=True)