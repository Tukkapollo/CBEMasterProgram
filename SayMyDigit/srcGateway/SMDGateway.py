from flask import Flask
import requests

app = Flask(__name__)

# Define the endpoints for your microservices
MICROSERVICE_1_URL = "http://microservice1:5001"
MICROSERVICE_2_URL = "http://microservice2:5002"
MICROSERVICE_3_URL = "http://microservice3:5003"
MICROSERVICE_4_URL = "http://microservice4:5004"

@app.route('/gateway/<string:number>/<string:language>', methods=['GET'])
def gateway(number,language):
    # Parse the incoming request
    data = request.json
    action = data.get('action')

    # Route the request to the appropriate microservice
    if action == 'service1':
        response = requests.get(f"{MICROSERVICE_1_URL}/endpoint1", json=data)
    elif action == 'service2':
        response = requests.get(f"{MICROSERVICE_2_URL}/endpoint2", json=data)
    elif action == 'service3':
        response = requests.get(f"{MICROSERVICE_3_URL}/endpoint3", json=data)
    elif action == 'service4':
        response = requests.get(f"{MICROSERVICE_4_URL}/endpoint4", json=data)
    else:
        return jsonify({"error": "Invalid action"}), 400

    return response.json()