import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

#Optener las opciones desde base de datos
def load_options():
    with open('options.json', 'r') as file:
        return json.load(file)

options = load_options()

#Elegir modelo
@app.route('/choose-model', methods=['POST'])
def choose_model():
    model_data = request.json.get('model_data')
    if model_data in options["models"]:
        print(f"Model selected: {model_data}")
        return jsonify({"status": f"Model '{model_data}' selected"}), 200
    return jsonify({"error": "Invalid model selection"}), 400

#Elegir el Hardware
@app.route('/choose-hardware-simulation', methods=['POST'])
def choose_hardware_simulation():
    hardware_data = request.json.get('model_data')
    if hardware_data in options["hardware"]:
        print(f"Hardware selected: {hardware_data}")
        return jsonify({"status": f"Hardware '{hardware_data}' selected"}), 200
    return jsonify({"error": "Invalid hardware selection"}), 400

#Elegir la optimizacion
@app.route('/choose-optimization', methods=['POST'])
def choose_optimization():
    optimization_data = request.json.get('model_data')
    if optimization_data in options["optimizations"]:
        print(f"Optimization selected: {optimization_data}")
        return jsonify({"status": f"Optimization '{optimization_data}' selected"}), 200
    return jsonify({"error": "Invalid optimization selection"}), 400

#Correr Simulacion.
@app.route('/run-simulation', methods=['POST'])
def run_simulation():
    model_id = request.json.get('model_id')
    hardware_type = request.json.get('hardware_type')
    optimization = request.json.get('optimization')

    #Captar errores
    if model_id not in options["models"]:
        return jsonify({"error": "Invalid model selected"}), 400
    if hardware_type not in options["hardware"]:
        return jsonify({"error": "Invalid hardware selected"}), 400
    if optimization not in options["optimizations"]:
        return jsonify({"error": "Invalid optimization selected"}), 400

    #Simulari Corer simulacion.
    print(f"Running simulation with Model: {model_id}, Hardware: {hardware_type}, Optimization: {optimization}")
    return jsonify({"status": "Simulation started successfully", "model": model_id, "hardware": hardware_type, "optimization": optimization}), 200

@app.route('/get-options', methods=['GET'])
def get_options():
    return jsonify(options), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
