import requests
from bs4 import BeautifulSoup
import json

# URL of Demoblaze's Laptops section
url = 'https://www.demoblaze.com/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Navigate to the Laptops section (assuming it has a specific link)
laptops_section_link = soup.find('a', string='Laptops')['href']
laptops_url = 'https://www.demoblaze.com/' + laptops_section_link

# Function to scrape laptop data
def scrape_laptops(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    laptop_data = []
    
    # Find the laptop listings
    laptops = soup.find_all('div', class_='card')
    
    for laptop in laptops:
        name = laptop.find('h4').text.strip()
        price = laptop.find('h5').text.strip()
        description = laptop.find('p').text.strip()
        
        laptop_data.append({
            'name': name,
            'price': price,
            'description': description
        })
    
    return laptop_data

# Scrape the first page
laptops_data = scrape_laptops(laptops_url)

# If there are multiple pages, scrape the subsequent pages
# You can implement pagination logic to click "Next" and scrape additional pages

# Save the laptop data in JSON format
with open('laptops.json', 'w') as json_file:
    json.dump(laptops_data, json_file, indent=4)

print("Laptop data saved to laptops.json")
