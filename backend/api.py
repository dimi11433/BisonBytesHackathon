from flask import Flask, jsonify
from test import dr_name  # Import function from test.py

app = Flask(__name__)

@app.route('/doctor', methods=['GET'])
def get_doctor():
    return jsonify({"name": dr_name()})  # Returns updated doctor name

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Runs on http://127.0.0.1:5000
