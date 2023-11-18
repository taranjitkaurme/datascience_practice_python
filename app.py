from flask import Flask, jsonify
from src.models.user_profile import UserProfile

app = Flask(__name__)

# Define a route for the API endpoint
@app.route('/api/data', methods=['GET'])
def get_data():
    # Hardcoded response
    data = {
        'message': 'Hello, this is your API response!',
        'status': 'success'
    }
    return jsonify(data)

if __name__ == '__main__':
    # Run the application on http://localhost:5000
    app.run(debug=True)