import csv
import os

# Define the path to your CSV file
csv_file_path = 'Source-Internal Vulnerability Scan - 04.11.24.csv'
output_file_path = 'source-servers.csv'

# Define the columns that contain the required information
os_column = 'OS'
ip_column = 'IP'
dns_column = 'DNS'
version_column = 'Title'

# Define the headers for the output CSV file
output_headers = ['IP Address', 'DNS', 'OS', 'Version']

# Define a list to store the extracted data
unique_servers = {}

# Read the CSV file
with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Iterate over each row in the CSV
    for row in reader:
        os_info = row[os_column]
        # Check if the OS is Windows or Linux
        if 'Windows' in os_info or 'Linux' in os_info:
            ip_address = row[ip_column]
            dns_info = row[dns_column]
            version_info = row[version_column]
            
            # Create a unique key for each server using IP, DNS, and OS as identifiers
            server_key = (ip_address, dns_info, os_info)
            
            # If the server is not already in the dictionary, add it
            if server_key not in unique_servers:
                unique_servers[server_key] = version_info

# Write the unique servers to the output CSV file
with open(output_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=output_headers)
    writer.writeheader()
    
    # Write each unique server to the CSV
    for server_key, version_info in unique_servers.items():
        writer.writerow({
            'IP Address': server_key[0],
            'DNS': server_key[1],
            'OS': server_key[2],
            'Version': version_info
        })

print(f"Output written to {output_file_path}")