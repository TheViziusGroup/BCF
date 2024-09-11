import csv
import os
import re
from collections import defaultdict

working_directory = os.path.expanduser('~/PATH/Documents/Discovery Process Scripts')
os.chdir(working_directory)

def safe_int_convert(value):
    """Safely convert a string to an integer, returning 0 if the conversion fails."""
    try:
        return int(value)
    except ValueError:
        return 0

def is_valid_ip(ip):
    """Check if a string is a valid IP address."""
    pattern = re.compile(r'^\d{1,3}(\.\d{1,3}){3}$')
    if pattern.match(ip):
        parts = ip.split('.')
        return all(0 <= int(part) <= 255 for part in parts)
    return False

# Read the input CSV file
input_file_path = 'Source-Networks - Authenticated.csv'
output_file_path = 'qualys-unique-highest-severity-output.csv'

with open(input_file_path, 'r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader if is_valid_ip(row['IP'])]

# Determine the fieldnames from the CSV header
fieldnames = reader.fieldnames

# Sort the data by IP and then by Severity (descending), handling empty or invalid Severity values
data.sort(key=lambda x: (x['IP'], -safe_int_convert(x['Severity'])))

# Create a dictionary to store the highest severity for each IP
highest_severity = defaultdict(lambda: {'Severity': 0, 'row': None})

# Iterate through the sorted data and update the highest severity for each IP
for row in data:
    ip = row['IP']
    severity = safe_int_convert(row['Severity'])
    if severity > highest_severity[ip]['Severity']:
        highest_severity[ip] = {'Severity': severity, 'row': row}

# Write the output CSV file with the highest severity for each IP
with open(output_file_path, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for ip, info in highest_severity.items():
        # Ensure info['row'] is not None before proceeding
        if info['row'] is not None:
            # Filter the dictionary to ensure it only contains the expected keys
            filtered_row = {key: info['row'][key] for key in fieldnames if key in info['row']}
            writer.writerow(filtered_row)
        else:
            print(f"Warning: No data for IP {ip}")
