import json

with open("data.json") as f:
    data_as_str = f.read()
    data = json.loads(data_as_str)

print(data)
print(f"Num of maintenences: {len(data['maintenanceSchedule'])}")