from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'])
def status():
    """Route that returns a JSON status."""
    return jsonify({"status": "OK"})