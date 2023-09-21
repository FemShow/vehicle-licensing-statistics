import pandas as pd

# Define the file path
file_path = "/Users/femisokoya/Documents/GitHub/Vehicle-licensing-statistics/result.csv"

# Load the CSV file into a DataFrame, only the first 50 rows
df = pd.read_csv(file_path, nrows=1000000)

# Create new columns 'Period1', 'Sorn', and 'SornValue'
df[:1000].pivot(values="Value", columns="LicenceStatus", index=["BodyType","Make","GenModel","Model","Fuel","Period"]).to_csv("result2.csv", index=False)

# Save the modified DataFrame to a new CSV file
# output_file = "result2.csv"
# df.to_csv(output_file, index=False)

print(f"Modified DataFrame saved to {output_file}")
