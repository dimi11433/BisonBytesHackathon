from flask import Flask, jsonify, request
from test import dr_name  # Import function from test.py
from model import predict
import evo2_api_call
import json

app = Flask(__name__)

@app.route('/doctor', methods=['GET'])
def get_doctor():
    return jsonify({"name": dr_name()})  # Returns updated doctor name

@app.route('/evo/<string:gene>', methods=['GET'])
def get_evo(gene):
    return jsonify({"mutations": evo2_api_call.evo_api_call(gene)})  # Returns updated gene mutations

@app.route('/analysis/<string:gene>', methods=['GET'])
def get_analysis(gene):
    mutations = evo2_api_call.evo_api_call(gene)
    return jsonify({"analysis": evo2_api_call.annotate_mutations_with_clinvar(mutations)})  # Returns updated gene analysis


@app.route('/predict', methods=['GET'])
def get_prediction():
    data = request.args.get('data')
    try:
        # Deserialize the JSON string into a Python dictionary
        dictionary = json.loads(data)
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 400
    print(data)
    predictions = predict(data)
    return jsonify({"prediction": predictions[0]})
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Runs on http://127.0.0.1:5000
