import requests
import os
import json
from pathlib import Path
from dotenv import load_dotenv


def evo_api_call(sequence = None):
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


def annotate_mutations_with_clinvar(mutations, start_genomic_pos, chromosome):
    genomic_positions = map_indices_to_genomic_positions(mutations, start_genomic_pos)
    results = []

    for position, prob in genomic_positions:
        variant_info = query_clinvar(chromosome, position)
        results.append({
            "genomic_position": position,
            "probability": prob,
            "variant_info": variant_info
        })

    return results


def query_clinvar(chromosome, position, assembly="GRCh38"):
    """
    Query NCBI ClinVar API for a given chromosome and position.
    """
    url = (
        f"https://api.ncbi.nlm.nih.gov/variation/v0/beta/refsnp/"
        f"?assembly={assembly}&chromosome={chromosome}&position={position}"
    )

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("refsnp_id"):
            return {
                "variant_id": data["refsnp_id"],
                "conditions": [cond.get("preferred_name", "N/A") for cond in data.get("clinical_significance", [])],
            }
    else:
        print(f"No variant found at {chromosome}:{position}")
    return None

def map_indices_to_genomic_positions(mutations, start_genomic_pos):
    return [(start_genomic_pos + idx, prob) for idx, prob in mutations]

def main():
    mutations = [(5, 0.2), (25, 0.15)]
    start_pos = 117559593
    chrom = "7"
    annotations = annotate_mutations_with_clinvar(mutations, start_pos, chrom)
    print(annotations)
    
if __name__ == "__main__":
    main()