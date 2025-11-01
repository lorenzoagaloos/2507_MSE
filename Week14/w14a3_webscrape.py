"""Web scrape the number of upcoming events from the Commevents Hub website."""

import requests
from bs4 import BeautifulSoup

url = "https://commeventshub.onrender.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

"""Find the number of upcoming events"""
event_count = soup.find('span', class_='badge bg-primary').text
print(f"Number of upcoming events: {event_count}")
