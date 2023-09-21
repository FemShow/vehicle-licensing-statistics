import pandas as pd

# Define the input and output file paths
input_csv_file = "/Users/femisokoya/Documents/GitHub/Vehicle-licensing-statistics/result3_headers.csv"
output_csv_file = "/Users/femisokoya/Documents/GitHub/Vehicle-licensing-statistics/result_normalized.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(input_csv_file)

# Normalize values in the 'GenModel' column
df['GenModel'] = df['GenModel'].str.strip()  # Remove leading and trailing spaces
df['GenModel'] = df['GenModel'].str.lower()  # Convert to lowercase
df['GenModel'].replace(['FARMTRAC', 'FARMTRAC '], 'farmtrac', inplace=True)  # Normalize 'farmtrac'
df['GenModel'].replace(['FORD', 'FORD '], 'ford', inplace=True)  # Normalize 'ford'
df['GenModel'].replace(['HARLEY DAVIDSON', 'HARLEY-DAVIDSON','harley davidson', 'harley-davidson'], 'harley-davidson', inplace=True)  # Normalize 'harley-davidson'
df['GenModel'].replace(['IVECO FORD', 'IVECO-FORD', 'iveco ford', 'iveco-ford'], 'iveco-ford', inplace=True)  # Normalize 'iveco-ford'
df['GenModel'].replace(['JCB', 'JCB '], 'jcb', inplace=True)  # Normalize 'jcb'
df['Make'] = df['Make'].str.strip()  # Remove leading and trailing spaces
df['Make'] = df['Make'].str.lower()  # Convert to lowercase
df['Make'].replace(['FARMTRAC', 'FARMTRAC '], 'farmtrac', inplace=True)  # Normalize 'farmtrac'
df['Make'].replace(['FORD', 'FORD '], 'ford', inplace=True)  # Normalize 'ford'
df['Make'].replace(['HARLEY DAVIDSON', 'HARLEY-DAVIDSON', 'harley davidson', 'harley-davidson'], 'harley-davidson', inplace=True)  # Normalize 'harley-davidson'
df['Make'].replace(['IVECO FORD', 'IVECO-FORD', 'iveco ford', 'iveco-ford'], 'iveco-ford', inplace=True)  # Normalize 'iveco-ford'
df['Make'].replace(['JCB', 'JCB '], 'jcb', inplace=True)  # Normalize 'jcb'

# Save the DataFrame to a new CSV file
df.to_csv(output_csv_file, index=False)

print(f"Normalized data saved to {output_csv_file}")
