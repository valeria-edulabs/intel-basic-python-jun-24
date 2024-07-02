import csv

# Replace with your CSV file path
csv_file_path = "../fab_equipment_data.csv"

with open(csv_file_path, 'r', newline='') as file:
    csv_reader = csv.reader(file, delimiter=';')

    # Read the header row (optional)
    header = next(csv_reader, None)
    if header:
        print(f"Column names: {', '.join(header)}")

    # Process the rest of the data
    for row in csv_reader:
        a = row[0]
        b = row[1]
        c = float(row[2])  # Assuming uptime is a numeric value

        print(f"Equipment ID: {a}, Status: {b}, Uptime: {c:.1f}%")
