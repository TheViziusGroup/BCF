import csv

def load_server_names(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def search_server_in_csv(server_name, csv_data):
    server_name_lower = server_name.lower()
    for row in csv_data:
        for cell in row:
            if server_name_lower in cell.lower():
                return row
    return None

def main(server_names_file, input_csv_file, output_csv_file):
    server_names = load_server_names(server_names_file)
    
    # Read the input CSV file
    with open(input_csv_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_header = next(csv_reader)  # Read the header
        csv_data = list(csv_reader)
    
    # Prepare the output data with the header
    output_data = [csv_header]
    
    # Search for each server name and build the output data
    for server_name in server_names:
        found_row = search_server_in_csv(server_name, csv_data)
        if found_row:
            output_data.append(found_row)
        else:
            output_data.append([server_name] + ['not found'] * (len(csv_header) - 1))
    
    # Write the output CSV file
    with open(output_csv_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(output_data)


if __name__ == '__main__':
    server_names_file = 'serverlist.txt'
    input_csv_file = 'Sentinel-unique-ip.csv'
    output_csv_file = 'server-status-sentinel-status.csv'
    main(server_names_file, input_csv_file, output_csv_file)
