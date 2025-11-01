"""Web scrape the number of upcoming events from the Commevents Hub website."""

import requests
from bs4 import BeautifulSoup

url = "https://commeventshub.onrender.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

"""Find the number of upcoming events"""
event_count = soup.find('span', class_='badge bg-primary').text
print(f"\nTotal Number of upcoming events: {event_count}\n")

"""List the titles of upcoming events"""
event_titles = soup.find_all('h5', class_='fw-semibold mb-1')

for title in event_titles:
    print(f"Event Title: {title.get_text()}")

"""This script fetches the Commevents Hub webpage, parses the HTML content,
and extracts the number of upcoming events along with their titles."""

url="https://commeventshub.onrender.com/events/tag/māori"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

event_count_maori = soup.find('span', class_='badge bg-primary').text
print(f"\nNumber of Maori upcoming events: {event_count_maori}")

url="https://commeventshub.onrender.com/events/tag/pacific"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

event_count_pac = soup.find('span', class_='badge bg-primary').text
print(f"\nNumber of Pacific upcoming events: {event_count_pac}\n")

url="https://commeventshub.onrender.com/events/tag/general"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

event_count_gen = soup.find('span', class_='badge bg-primary').text
print(f"Number of General upcoming events: {event_count_gen}\n")