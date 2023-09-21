import pandas as pd

# Define the file path
file_path = "/Users/femisokoya/Documents/GitHub/Vehicle-licensing-statistics/result.csv"

# Load the CSV file into a DataFrame, only the first 50 rows
df = pd.read_csv(file_path, nrows=50)

# Create new columns 'Period1', 'Sorn', and 'SornValue'
df['Period1'] = ''
df['Sorn'] = ''
df['SornValue'] = ''

# Find rows where the next row has the same 'GenModel', 'Model', and 'Period'
mask = (df[['GenModel', 'Model', 'Period']] == df[['GenModel', 'Model', 'Period']].shift(-1)).all(axis=1)

# Update the corresponding rows based on the mask
df.loc[mask, 'Period1'] = df['Period']
df.loc[mask, 'Sorn'] = 'SORN'
df.loc[mask, 'SornValue'] = df['Value']

# Drop the second row of each pair
df = df[~mask]

# Reset the index
df.reset_index(drop=True, inplace=True)

# Save the modified DataFrame to a new CSV file
output_file = "result1.csv"
df.to_csv(output_file, index=False)

print(f"Modified DataFrame saved to {output_file}")
