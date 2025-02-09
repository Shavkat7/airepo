import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

# SQLite setup
conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title TEXT,
    company_name TEXT,
    location TEXT,
    job_description TEXT,
    application_link TEXT,
    UNIQUE(job_title, company_name, location)
)
''')
conn.commit()

# Scrape job listings
url = 'https://realpython.github.io/fake-jobs/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all job listings
job_listings = soup.find_all('div', class_='card-body')

# Function to insert job into the database
def insert_job(job_title, company_name, location, job_description, application_link):
    try:
        cursor.execute('''
            INSERT INTO jobs (job_title, company_name, location, job_description, application_link)
            VALUES (?, ?, ?, ?, ?)
        ''', (job_title, company_name, location, job_description, application_link))
        conn.commit()
    except sqlite3.IntegrityError:
        # If the job already exists, skip inserting it
        pass

# Scrape and insert jobs
for job in job_listings:
    job_title = job.find('h2').text.strip()
    company_name = job.find('h3').text.strip()
    location = job.find('p', class_='location').text.strip()
    job_description = job.find('p', class_='description').text.strip()
    application_link = job.find('a', class_='apply')['href']
    
    # Insert job into the database
    insert_job(job_title, company_name, location, job_description, application_link)

# Function to filter jobs by location or company and export to CSV
def export_filtered_jobs(location=None, company=None, filename='filtered_jobs.csv'):
    query = 'SELECT * FROM jobs WHERE 1=1'
    params = []
    
    if location:
        query += ' AND location LIKE ?'
        params.append(f'%{location}%')
    if company:
        query += ' AND company_name LIKE ?'
        params.append(f'%{company}%')

    cursor.execute(query, params)
    filtered_jobs = cursor.fetchall()

    # Write filtered jobs to CSV
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Job Title', 'Company Name', 'Location', 'Job Description', 'Application Link'])
        writer.writerows(filtered_jobs)

# Close the connection to the database
conn.close()
