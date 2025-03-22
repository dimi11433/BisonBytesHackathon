#!/usr/bin/env python3
import requests
import os
import json
from pathlib import Path

key = "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"

r = requests.post(
    url=os.getenv("URL", "https://health.api.nvidia.com/v1/biology/arc/evo2-40b/generate"),
    headers={"Authorization": f"Bearer {key}"},
    json={
        "sequence": "GAATAGGAACAGCTCCGGTCTACAGCTCCCAGCGTGAGCGACGCAGAAGACGGTGATTTCTGCATTTCCATCTGAGGTACCGGGTTCATCTCACTAGGGAGTGCCAGACAGTGGGCGCAGGCCAGTGTGTGTGCGCACCGTGCGCGAGCCGAAGCAGGGCGAGGCATTGCCTCACCTGGGAAGCGCAAGGGGTCAGGGAGTTCCCTTTCCGAGTCAAAGAAAGGGGTGATGGACGCACCTGGAAAATCGGGTCACTCCCACCCGAATATTGCGCTTTTCAGACCGGCTTAAGAAACGGCGCACCACGAGACTATATCCCACACCTGGCTCAGAGGGTCCTACGCCCACGGAATC",
        "num_tokens": 102,
        "top_k": 4,
        "enable_sampled_probs": True,
    },
)

if "application/json" in r.headers.get("Content-Type", ""):
    print(r, "Saving to output.json:\n", r.text[:200], "...")
    Path("output.json").write_text(r.text)
elif "application/zip" in r.headers.get("Content-Type", ""):
    print(r, "Saving large response to data.zip")
    Path("data.zip").write_bytes(r.content)
else:
    print(r, r.headers, r.content)
    