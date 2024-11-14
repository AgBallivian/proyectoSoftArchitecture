from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/choose-model', methods=['POST'])
def upload_model():
    avialable_models = ["simple_nn"]
    #desplegar modelos disponibles
    model_data = request.json.get('model_data')
    if model_data:
        print("Model uploaded")
        return jsonify({"status": "Model uploaded successfully"}), 200
    
    return jsonify({"error": "No model data provided"}), 400

@app.route('/choose-hardware-simulation', methods=['POST'])
def upload_model():
    avialable_models = ["MRAM"]
    #desplegar tipos de hardware disponibles
    model_data = request.json.get('model_data')
    if model_data:
        print("Model uploaded")
        return jsonify({"status": "Model uploaded successfully"}), 200
    
    return jsonify({"error": "No model data provided"}), 400

@app.route('/choose-optimization', methods=['POST'])
def upload_model():
    avialable_models = ["Pruning", "Quantization", "Knowledge Distillation"]
    #desplegar optimizaciones disponibles
    model_data = request.json.get('model_data')
    if model_data:
        print("Model uploaded")
        return jsonify({"status": "Model uploaded successfully"}), 200
    
    return jsonify({"error": "No model data provided"}), 400

@app.route('/run-simulation', methods=['POST'])
def run_simulation():
    model_id = request.json.get('model_id')
    return jsonify({"status": "Simulation started", "model_id": model_id}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
