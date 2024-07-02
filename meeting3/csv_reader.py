import csv

# Replace with your CSV file path
csv_file_path = "fab_equipment_data.csv"

with open(csv_file_path, 'r', newline='') as file:
    csv_reader = csv.reader(file)

    # Read the header row (optional)
    header = next(csv_reader, None)
    if header:
        print(f"Column names: {', '.join(header)}")

    # Process the rest of the data
    for row in csv_reader:
        equipment_id = row[0]
        status = row[1]
        uptime = float(row[2])  # Assuming uptime is a numeric value

        print(f"Equipment ID: {equipment_id}, Status: {status}, Uptime: {uptime:.1f}%")
