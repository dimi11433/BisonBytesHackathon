from flask import Flask, jsonify
from test import dr_name  # Import function from test.py

app = Flask(__name__)

@app.route('/doctor', methods=['GET'])
def get_doctor():
    return jsonify({"name": dr_name()})  # Returns updated doctor name

@app.route('/evo/<string:gene>', methods=['GET'])
def get_evo(gene):
    return jsonify({"mutations": evo_api_call(gene)})  # Returns updated gene mutations


def evo_api_call(sequence = None):
    import requests
    import os
    import json
    from pathlib import Path
    from dotenv import load_dotenv

    load_dotenv()
    
    if (sequence == None or len(sequence) == 0 or sequence == "None"):
        sequence = "GAATAGGAACAGCTCCGGTCTACAGCTCCCAGCGTGAGCGACGCAGAAGACGGTGATTTCTGCATTTCCATCTGAGGTACCGGGTTCATCTCACTAGGGAGTGCCAGACAGTGGGCGCAGGCCAGTGTGTGTGCGCACCGTGCGCGAGCCGAAGCAGGGCGAGGCATTGCCTCACCTGGGAAGCGCAAGGGGTCAGGGAGTTCCCTTTCCGAGTCAAAGAAAGGGGTGATGGACGCACCTGGAAAATCGGGTCACTCCCACCCGAATATTGCGCTTTTCAGACCGGCTTAAGAAACGGCGCACCACGAGACTATATCCCACACCTGGCTCAGAGGGTCCTACGCCCACGGAATC"

    key = os.getenv("EVO_API_KEY")

    r = requests.post(
        url=os.getenv("URL", "https://health.api.nvidia.com/v1/biology/arc/evo2-40b/generate"),
        headers={"Authorization": f"Bearer {key}"},
        json={
            "sequence": sequence,
            "num_tokens": 102,
            "top_k": 4,
            "enable_sampled_probs": True,
        },
    )
    mutations = []
    
    for i, prob in enumerate(r.json()['sampled_probs']):
        if prob < 0.9:
            mutations.append({"position": i, "probability":r.json()['sampled_probs'][i]})
            
    return mutations
        
    
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Runs on http://127.0.0.1:5000
