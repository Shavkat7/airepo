from bs4 import BeautifulSoup

# Read the HTML file
with open('weather.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the weather forecast data
forecast_table = soup.find('table').find('tbody')
rows = forecast_table.find_all('tr')

# Initialize a list to hold weather data
weather_data = []

# Extract the day, temperature, and condition from each row
for row in rows:
    cols = row.find_all('td')
    day = cols[0].text.strip()
    temperature = int(cols[1].text.strip().replace('°C', ''))
    condition = cols[2].text.strip()
    weather_data.append({'day': day, 'temperature': temperature, 'condition': condition})

# Display weather data
print("Weather Forecast:")
for entry in weather_data:
    print(f"{entry['day']}: {entry['temperature']}°C, {entry['condition']}")

# Find the day(s) with the highest temperature
max_temp = max(weather_data, key=lambda x: x['temperature'])
print(f"\nDay with the highest temperature: {max_temp['day']} ({max_temp['temperature']}°C)")

# Find the day(s) with the "Sunny" condition
sunny_days = [entry for entry in weather_data if entry['condition'] == 'Sunny']
print("\nDays with 'Sunny' condition:")
for sunny in sunny_days:
    print(sunny['day'])

# Calculate the average temperature
average_temp = sum(entry['temperature'] for entry in weather_data) / len(weather_data)
print(f"\nAverage temperature for the week: {average_temp:.2f}°C")
