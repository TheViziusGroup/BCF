def subtract_ips(file_a, file_b, output_file):
    # Read IPs from file a
    with open(file_a, 'r') as f:
        ips_a = set(f.read().splitlines())

    # Read IPs from file b
    with open(file_b, 'r') as f:
        ips_b = set(f.read().splitlines())

    # Subtract IPs in file a from file b
    result_ips = ips_b - ips_a

    # Write the result to the output file
    with open(output_file, 'w') as f:
        for ip in sorted(result_ips):
            f.write(ip + '\n')

# Example usage
subtract_ips('nmap-successful.txt', 'ping-these.txt','result.txt')