import json
import pandas as pd
from pandas import json_normalize

# Load JSON from file or string
with open("input.json") as f:
    data = json.load(f)

# Flatten JSON
def flatten_json(json_data):
    if isinstance(json_data, list):
        df = json_normalize(json_data)
    elif isinstance(json_data, dict):
        df = json_normalize([json_data])
    else:
        raise ValueError("Unsupported JSON format")
    return df

# Unnest and convert to CSV
df = flatten_json(data)

# Save to CSV
df.to_csv("output.csv", index=False)
