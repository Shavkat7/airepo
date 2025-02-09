import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('chinook.db')

# Read the customers table into a pandas DataFrame
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)

# Display the first 10 rows
print(customers_df.head(10))

# Close the connection
conn.close()



#iris

# Load the JSON file into a DataFrame
iris_df = pd.read_json('iris.json')

# Show the shape of the dataset and the column names
print("Shape of the dataset:", iris_df.shape)
print("Column names:", iris_df.columns)


#titanic

# Load the Excel file into a DataFrame
titanic_df = pd.read_excel('titanic.xlsx')

# Display the first 5 rows
print(titanic_df.head())


#Parquet

# Read the Parquet file into a DataFrame
flights_df = pd.read_parquet('Flights.parquet')

# Use info() to summarize the DataFrame
print(flights_df.info())


# movie

# Load the CSV file into a DataFrame
movie_df = pd.read_csv('movie.csv')

# Display a random sample of 10 rows
print(movie_df.sample(10))





#PART 2

# Rename the columns to lowercase
iris_df.columns = iris_df.columns.str.lower()

# Select only the sepal_length and sepal_width columns
iris_filtered = iris_df[['sepal_length', 'sepal_width']]

# Display the first 5 rows of the filtered DataFrame
print(iris_filtered.head())


# Filter rows where age is above 30
titanic_filtered = titanic_df[titanic_df['age'] > 30]

# Count the number of male and female passengers
gender_count = titanic_df['sex'].value_counts()

print(titanic_filtered.head())
print("Gender count:", gender_count)



# Extract origin, dest, and carrier columns
flights_filtered = flights_df[['origin', 'dest', 'carrier']]

# Find the number of unique destinations
unique_destinations = flights_df['dest'].nunique()

print(flights_filtered.head())
print("Number of unique destinations:", unique_destinations)




# Filter rows where duration is greater than 120 minutes
movie_filtered = movie_df[movie_df['duration'] > 120]

# Sort the filtered DataFrame by director_facebook_likes in descending order
movie_sorted = movie_filtered.sort_values(by='director_facebook_likes', ascending=False)

print(movie_sorted.head())




#PART 3

# Calculate mean, median, and standard deviation for each numerical column
iris_stats = iris_df.describe().T[['mean', '50%', 'std']]

# Rename the 50% column to 'median'
iris_stats.rename(columns={'50%': 'median'}, inplace=True)

print(iris_stats)



# Calculate the minimum, maximum, and sum of passenger ages
age_stats = titanic_df['age'].agg(['min', 'max', 'sum'])

print(age_stats)



# Group by director and sum the director_facebook_likes
director_likes = movie_df.groupby('director')['director_facebook_likes'].sum()

# Identify the director with the highest total likes
top_director = director_likes.idxmax()
top_director_likes = director_likes.max()

print(f"Top Director: {top_director}, Likes: {top_director_likes}")




# Sort by duration in descending order and get the top 5 longest movies
top_5_longest_movies = movie_df.sort_values(by='duration', ascending=False).head(5)

print(top_5_longest_movies[['name', 'duration', 'director']])




# Check for missing values in the dataset
missing_values = flights_df.isnull().sum()

# Fill missing values in numerical columns with the column’s mean
flights_df_filled = flights_df.fillna(flights_df.mean())

print("Missing values:", missing_values)
print(flights_df_filled.head())
