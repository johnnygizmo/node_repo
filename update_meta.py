import json

filepath = ".\\_asset-library-meta.json"

with open(filepath, "r") as f:
    data = json.load(f)

data["name"] = "Johnnygizmo's Node Library"
data["contact"] = {
    "name": "Johnny Matthews",
    "url": "https://youtube.com/@johnnymatthews",
    "email": "johnny.matthews+nodes@gmail.com"
}

with open(filepath, "w") as f:
    json.dump(data, f, indent=2)

print("Updated", filepath)
