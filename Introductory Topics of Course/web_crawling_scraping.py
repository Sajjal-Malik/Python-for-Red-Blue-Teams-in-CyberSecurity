from bs4 import BeautifulSoup
import requests

# Fetch HTML content from a URL
response = requests.get("https://elhacker.info/Cursos/")
html_content = response.content

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, "html.parser")

# Extract the title of the page
title = soup.title.string
print(f"Page Title: {title}")

# Find all paragraph tags
courses_links = soup.find_all("a")
for course_link in courses_links:
    print(course_link.get_text())
