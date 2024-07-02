import json

# with open("data.json") as f:
#     data_as_str = f.read()
#     data = json.loads(data_as_str)

dates = []
with open("data.json") as f:
    data = json.load(f)

for dataEntry in data["maintenanceSchedule"]:
    dates.append(dataEntry["date"])

print(f"Dates: {dates}")

# print(data)
# print(f"Num of maintenences: {len(data['maintenanceSchedule'])}")