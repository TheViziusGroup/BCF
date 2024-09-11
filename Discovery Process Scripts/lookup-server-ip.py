import csv
def read_server_list(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]
    except Exception as e:
        print(f"Error reading server list: {e}")
        return []

def read_csv_file(file_path):
    data = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
    except Exception as e:
        print(f"Error reading CSV file {file_path}: {e}")
    return data

def find_server_ip(server_name, data):
    server_name = server_name.lower()
    for row in data:
        for key, value in row.items():
            if key.lower() != 'ip' and server_name in value.lower():
                return row.get('IP', 'not found')
    return 'not found'

def create_serverlist_ip(server_list, file1_data, file2_data, file3_data, output_file):
    try:
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['servername', 'ip in File 1', 'ip in File 2', 'ip in File 3'])
            for server in server_list:
                ip1 = find_server_ip(server, file1_data)
                ip2 = find_server_ip(server, file2_data)
                ip3 = find_server_ip(server, file3_data)
                writer.writerow([server, ip1, ip2, ip3])
    except Exception as e:
        print(f"Error writing to output file {output_file}: {e}")

def main():
    server_list = read_server_list('serverlist.txt')
    file1_dict = read_csv_file('qualys-unique-ips-output.csv')
    file2_dict = read_csv_file('itglue-configurations.csv')
    file3_dict = read_csv_file('Sentinel-unique-ip.csv')
    create_serverlist_ip(server_list, file1_dict, file2_dict, file3_dict, 'serverlist-ip.csv')

if __name__ == "__main__":
    main()
