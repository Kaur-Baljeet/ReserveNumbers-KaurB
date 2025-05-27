import sys
import pandas as pd

def parse_query(query):
    conditions = {}
    for pair in query.split(','):
        if '=' in pair:
            field, value = pair.split('=', 1)
            conditions[field] = value
    return conditions

# Read the CSV file
df = pd.read_csv('data.csv')

# Get the query string from command-line arguments
query = sys.argv[1]
conditions = parse_query(query)

# Apply filters
for field, value in conditions.items():
    df = df[df[field].astype(str).str.strip() == value.strip()]

# Print the filtered results
print("Filtered Results:")
print(df.to_string(index=False))
