from flask import Flask, jsonify, request
from helper import productionize as prod
from flask_cors import CORS

app = Flask(__name__)
CORS(app, support_credentials=True)
# Global variables
model = None
counters = None
stats = None

def initialize_app():
    global model, counters, stats
    model = prod.load_model('/app/data/lol_prediction_model.sav')
    counters = prod.initialize_counters('/app/data/counters.json')
    stats = prod.read_and_prepare_stats('/app/data/League_of_Legends_Champion_Stats_13.1.csv', counters)

# Load the model and counters when the app starts
initialize_app()

@app.route('/hello', methods=['GET'])
def test_hello():
    # You can include more complex logic here if needed
    return jsonify({'message': 'Hello, world!', 'value': 42069})

@app.route('/', methods=['GET'])
def setup_model():
    initialize_app()
    return jsonify({'message': 'Model setup complete!'})

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.get_json()
    role = request.args.get('role')

    # Perform prediction using the global components
    predictions = prod.make_prediction(input_data, model, stats, counters, role)
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
