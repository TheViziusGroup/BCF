import csv

def read_and_extract_unique_ips(input_file_path, output_file_path):
    # Initialize a set to keep track of unique IPs
    seen_ips = set()

    # Open the input CSV file for reading
    with open(input_file_path, 'r') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        # Open the output CSV file for writing
        with open(output_file_path, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            # Iterate over each row in the input CSV file
            for row in reader:
                ip = row['IP']
                # Check if the IP has already been encountered
                if ip not in seen_ips:
                    # Write the row to the output file if the IP is unique
                    writer.writerow(row)
                    # Add the IP to the set of seen IPs
                    seen_ips.add(ip)

# Specify the path to your input and output files
input_file_path = 'Sentinels_Report_20240506_021220_UTC.csv'
output_file_path = 'Sentinel-unique-ip.csv'

# Call the function with the specified file paths
read_and_extract_unique_ips(input_file_path, output_file_path)