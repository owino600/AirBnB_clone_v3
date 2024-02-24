from flask import jsonify
from api.v1.views import app_views

app = Flask(__name__)
@app_views.route('/status', methods=['GET'])
def status():
    """Route that returns a JSON status."""
    return jsonify({"status": "OK"})
app.run(host='0.0.0.0', port=5000)