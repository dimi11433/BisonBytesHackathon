from flask import Flask, jsonify
from test import dr_name  # Import function from test.py
import evo2_api_call

app = Flask(__name__)

@app.route('/doctor', methods=['GET'])
def get_doctor():
    return jsonify({"name": dr_name()})  # Returns updated doctor name

@app.route('/evo/<string:gene>', methods=['GET'])
def get_evo(gene):
    return jsonify({"mutations": evo2_api_call.evo_api_call(gene)})  # Returns updated gene mutations

    
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Runs on http://127.0.0.1:5000
