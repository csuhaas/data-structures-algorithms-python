import json
import pandas as pd

# Recursive function to flatten nested JSON
def flatten(obj, parent_key='', sep='.'):
    items = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            items.extend(flatten(v, new_key, sep=sep).items())
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            new_key = f"{parent_key}[{i}]"
            items.extend(flatten(v, new_key, sep=sep).items())
    else:
        items.append((parent_key, obj))
    return dict(items)

# Load JSON file
with open("input.json") as f:
    raw_data = json.load(f)

# Handle list of records or single record
if isinstance(raw_data, list):
    flat_data = [flatten(entry) for entry in raw_data]
else:
    flat_data = [flatten(raw_data)]

# Convert to DataFrame
df = pd.DataFrame(flat_data)

# Save to CSV
df.to_csv("output.csv", index=False)
