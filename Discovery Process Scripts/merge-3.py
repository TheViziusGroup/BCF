import pandas as pd

# Load the CSV files
file1_path = "qualys-unique-ips-output.csv"
file2_path = "itglue-configurations.csv"
file3_path = "Sentinel-unique-ip.csv"

# Read the CSV files
file1 = pd.read_csv(file1_path)
file2 = pd.read_csv(file2_path)
file3 = pd.read_csv(file3_path)

# Standardize the IP column names for merging
file1 = file1.rename(columns={"IP": "IP"})
file2 = file2.rename(columns={"IP": "IP"})
file3 = file3.rename(columns={"IP": "IP"})

# Merge the dataframes on the 'IP' column
merged = pd.merge(file1, file2, on='IP', how='outer', suffixes=('_file1', '_file2'))
merged = pd.merge(merged, file3, on='IP', how='outer', suffixes=('', '_file3'))

# Create the new column to indicate the presence in files
merged['Files_Presence'] = (
    merged.apply(lambda row: f"{'file1' if pd.notnull(row['DNS']) else ''}"
                              f"{'&file2' if pd.notnull(row['name']) else ''}"
                              f"{'&file3' if pd.notnull(row['Endpoint Name']) else ''}".strip('&'), axis=1)
)

# Save the merged dataframe to a new CSV file
merged.to_csv("merged_output.csv", index=False)

print("Merged file created successfully with presence indicators.")
