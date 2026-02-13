import json

data = [
    {"id": 1, "name": "Item A", "value": 10},
    {"id": "2", "name": "Item B", "value": 20},
    {"id": 3, "name": 123, "value": 15.5}
]

valid = []
invalid = []

for item in data:
    if isinstance(item["id"], int) and isinstance(item["name"], str):
        valid.append(item)
    else:
        invalid.append(item)

with open("valid.json", "w") as f:
    json.dump(valid, f, indent=2)

with open("invalid.json", "w") as f:
    json.dump(invalid, f, indent=2)

print("Valid:", len(valid))
print("Invalid:", len(invalid))


