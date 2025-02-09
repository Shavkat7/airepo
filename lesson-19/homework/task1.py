import sqlite3
import pandas as pd

# Load the chinook.db database
conn = sqlite3.connect('chinook.db')

# Read the customers and invoices tables into DataFrames
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
invoices_df = pd.read_sql_query("SELECT * FROM invoices", conn)

# Perform an inner join on the CustomerId column
merged_df = pd.merge(customers_df, invoices_df, on='CustomerId', how='inner')

# Find the total number of invoices for each customer
invoice_count = merged_df.groupby('CustomerId')['InvoiceId'].count()

print(invoice_count.head())

# Close the connection
conn.close()



# Load the movie.csv file
movie_df = pd.read_csv('movie.csv')

# Create two smaller DataFrames
df1 = movie_df[['director_name', 'color']]
df2 = movie_df[['director_name', 'num_critic_for_reviews']]

# Perform a left join on director_name
left_join_df = pd.merge(df1, df2, on='director_name', how='left')

# Perform a full outer join on director_name
outer_join_df = pd.merge(df1, df2, on='director_name', how='outer')

# Count the rows in each resulting DataFrame
left_join_rows = left_join_df.shape[0]
outer_join_rows = outer_join_df.shape[0]

print(f"Left Join Rows: {left_join_rows}")
print(f"Outer Join Rows: {outer_join_rows}")



# Load the titanic.xlsx file
titanic_df = pd.read_excel('titanic.xlsx')

# Group passengers by Pclass and calculate the average age, total fare, and count of passengers
grouped_titanic = titanic_df.groupby('Pclass').agg(
    average_age=('age', 'mean'),
    total_fare=('fare', 'sum'),
    passenger_count=('age', 'size')
)

# Save the result to a new DataFrame
print(grouped_titanic)



# Group the movies by color and director_name
grouped_movie = movie_df.groupby(['color', 'director_name']).agg(
    total_num_critic_for_reviews=('num_critic_for_reviews', 'sum'),
    average_duration=('duration', 'mean')
)

print(grouped_movie)





# Load the Flights dataset (assuming you have the file 'Flights.parquet')
flights_df = pd.read_parquet('Flights.parquet')

# Group flights by Year and Month and calculate the total number of flights, average arrival delay, and maximum departure delay
grouped_flights = flights_df.groupby(['Year', 'Month']).agg(
    total_flights=('FlightNum', 'count'),
    avg_arrival_delay=('ArrDelay', 'mean'),
    max_departure_delay=('DepDelay', 'max')
)

print(grouped_flights)



# Create a function to classify passengers as Child (age < 18) or Adult
def classify_age_group(age):
    if age < 18:
        return 'Child'
    else:
        return 'Adult'

# Apply the function to create a new column, Age_Group
titanic_df['Age_Group'] = titanic_df['age'].apply(classify_age_group)

print(titanic_df[['age', 'Age_Group']].head())



# Load the employee.csv file
employee_df = pd.read_csv('employee.csv')

# Normalize the salaries within each department
employee_df['normalized_salary'] = employee_df.groupby('department')['salary'].transform(lambda x: (x - x.mean()) / x.std())

print(employee_df[['department', 'salary', 'normalized_salary']].head())





# Create a function to classify the duration of a movie
def classify_duration(duration):
    if duration < 60:
        return 'Short'
    elif 60 <= duration <= 120:
        return 'Medium'
    else:
        return 'Long'

# Apply this function to classify movies in the movie.csv dataset
movie_df['duration_category'] = movie_df['duration'].apply(classify_duration)

print(movie_df[['name', 'duration', 'duration_category']].head())




from sklearn.pipeline import Pipeline

# Create a pipeline to filter passengers who survived, fill missing Age values, and create a new Fare_Per_Age column
def create_fare_per_age(df):
    df['Fare_Per_Age'] = df['fare'] / df['age']
    return df

titanic_pipeline = Pipeline([
    ('filter_survived', lambda df: df[df['survived'] == 1]),
    ('fill_missing_age', lambda df: df.fillna({'age': df['age'].mean()})),
    ('create_fare_per_age', create_fare_per_age)
])

# Apply the pipeline to the Titanic DataFrame
titanic_transformed = titanic_pipeline.fit_transform(titanic_df)

print(titanic_transformed.head())




# Create a pipeline to filter flights with a departure delay greater than 30 minutes
# and add a column Delay_Per_Hour by dividing the delay by the scheduled flight duration

def add_delay_per_hour(df):
    df['Delay_Per_Hour'] = df['DepDelay'] / df['ScheduledDuration']
    return df

flights_pipeline = Pipeline([
    ('filter_delayed_flights', lambda df: df[df['DepDelay'] > 30]),
    ('add_delay_per_hour', add_delay_per_hour)
])

# Apply the pipeline to the Flights DataFrame
flights_transformed = flights_pipeline.fit_transform(flights_df)

print(flights_transformed.head())




