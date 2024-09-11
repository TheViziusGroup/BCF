import pandas as pd
import os

def find_ip_addresses(base_dir, ip_filename, csv_filename, output_filename):
    # Construct full paths for the files
    ip_file_path = os.path.join(base_dir, ip_filename)
    csv_file_path = os.path.join(base_dir, csv_filename)
    output_file_path = os.path.join(base_dir, output_filename)

    # Read IP addresses from the text file
    with open(ip_file_path, 'r') as file:
        ip_set = set(line.strip() for line in file)

    # Prepare to write found results
    results = []

    # Process the CSV in chunks
    chunk_size = 50000  # Adjust chunk size based on your system's memory capacity
    for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size, usecols=['IP']):
        to_remove = set()
        for ip in ip_set:
            # Find rows containing the IP address in the 'IP' column
            found_lines = chunk.index[chunk['IP'] == ip] + chunk.index.start + 1  # Correct line numbers
            for line in found_lines:
                results.append([ip, line])
            # If any IP is found, add it to to_remove set
            if not found_lines.empty:
                to_remove.add(ip)
        
        # Remove all collected IPs from ip_set after the loop
        ip_set.difference_update(to_remove)

    # Write results to CSV
    result_df = pd.DataFrame(results, columns=['IP Address', 'Found in Line'])
    result_df.to_csv(output_file_path, index=False)

# Example usage
base_directory = r"/Users/YOURPATH/"  # Update this path
find_ip_addresses(base_directory, 'qualys-only.txt', 'Sentinels_Report_20240506_021220_UTC.csv', 'found-in-sentinel.csv')
