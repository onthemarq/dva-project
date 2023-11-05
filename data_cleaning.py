import pandas as pd
from unidecode import unidecode

csv_file_path = 'data.csv'

# Read the CSV file into a DataFrame
data = pd.read_csv(csv_file_path)

# Calculate the total count of records in the DataFrame
total_records = data.shape[0]

print(f"Total count of records in the DataFrame: {total_records}")

# Calculate the count of missing values for each column
missing_values_count = data.isnull().sum()

print("Missing values count for each column:")
print(missing_values_count)

# Check how many records only have a year value in the "release_date" field
year_only_records = data[data['release_date'].str.match(r'^\d{4}$', na=False)]

count_year_only_records = len(year_only_records)

print(f"Number of records with only a year value in 'release_date': {count_year_only_records}")

# Convert year-only records to the beginning of the year date for consitency
year_only_records.loc[:,('release_date')] = year_only_records['release_date'].astype(str) + '-01-01'

# Update the original DataFrame with the converted records
data.update(year_only_records)

# Apply unidecode to the "name" column to clean extraneous characters
data['name'] = data['name'].apply(unidecode)

# Split the "artists" column into separate columns
data['artists'] = data['artists'].apply(eval)  # Convert string representation of list to an actual list
data['artists'] = data['artists'].apply(lambda artist_list: [unidecode(artist) for artist in artist_list]) #clean extraneous characters
artist_columns = data['artists'].apply(pd.Series)  # Split into separate columns

# Rename the new columns (e.x. 'artist_1', 'artist_2', etc.)
new_column_names = [f'artist_{i+1}' for i in range(artist_columns.shape[1])]
artist_columns.columns = new_column_names

# Add a new column for the count of artists
data['artist_count'] = artist_columns.notna().sum(axis=1)

# Concatenate the new columns with the original DataFrame
new_data = pd.concat([data, artist_columns], axis=1)
new_data = new_data.rename(columns={'artists': 'artists_combined'})

# Save the modified DataFrame to a new CSV file
new_data.to_csv('cleaned_spotify_data.csv', index=False)
