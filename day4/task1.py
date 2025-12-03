from bs4 import BeautifulSoup

# Sample HTML content
html_doc = """
<html>
<head><title>My Title</title></head>
<body>
  <p class="intro">This is an <b>introduction</b>.</p>
  <div id="content">
    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
    </ul>
  </div>
</body>
</html>
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html_doc, 'html.parser')

# Find elements by tag name
title_tag = soup.title
print(f"Title: {title_tag.string}")

# Find an element by class
intro_paragraph = soup.find('p', class_='intro')
print(f"Intro paragraph text: {intro_paragraph.get_text()}")

# Find all list items
list_items = soup.find_all('li')
for item in list_items:
    print(f"List item: {item.string}")