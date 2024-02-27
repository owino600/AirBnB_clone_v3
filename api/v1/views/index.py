#!/usr/bin/python3
""" Index """
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """Route that returns a JSON status."""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """
    Retrieves the number of each object by type
    """
    classes = {
        "Amenity": "amenities",
        "City": "cities",
        "Place": "places",
        "Review": "reviews",
        "State": "states",
        "User": "users"
    }
    counts = {}
    for cls in classes:
        counts[classes[cls]] = storage.count(cls)
    return jsonify(counts)


if __name__ == '__main__':
    app_views.run(host='0.0.0.0', port='5000')
