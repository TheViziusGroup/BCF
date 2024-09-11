import pandas as pd

# Load the CSV files
file1_path = 'Sentinels_Report_20240506_021220_UTC.csv'
file2_path = 'Vulnscan-UniqueIPs-output.csv'
file1 = pd.read_csv(file1_path, low_memory=False)
file2 = pd.read_csv(file2_path, low_memory=False)

# Merge the two files on the 'IP' column
merged = pd.merge(file1, file2, on='IP', how='outer', indicator=True)

# Save the merged file
merged.to_csv('merged.csv', index=False)

# Filter rows that were only in file1 (left_only)
sentinal_unique = merged[merged['_merge'] == 'left_only']
sentinal_unique.to_csv('sentinal-unique-IPs.csv', index=False)

# Filter rows that were only in file2 (right_only)
qualys_unique = merged[merged['_merge'] == 'right_only']
qualys_unique.to_csv('qualys-unique-IPs.csv', index=False)