import requests
from datetime import datetime

# Fetch news
url = "https://inshortsapi.vercel.app/news?category=general"
response = requests.get(url)
data = response.json()

news_list = data.get("data", [])[:10]  # Top 10

# Format into HTML
items = ""
for article in news_list:
    items += f"<li><a href='{article['readMoreUrl']}' target='_blank'>{article['title']}</a></li>\n"

# Read and replace placeholder in index.html
with open("index.html", "r", encoding="utf-8") as file:
    html = file.read()

html = html.replace("<!-- NEWS_PLACEHOLDER -->", items)
html = html.replace("<!-- DATE_PLACEHOLDER -->", datetime.now().strftime("%B %d, %Y"))

# Save updated HTML
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html)

print("✅ News updated successfully")
