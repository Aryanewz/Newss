import requests
from datetime import datetime

# News API URL and key (replace YOUR_API_KEY with your actual key)
API_KEY = '99902109370b406f956f5617ec1fc138'
NEWS_API_URL = (
    f'https://newsapi.org/v2/top-headlines?country=in&pageSize=10&apiKey={API_KEY}'
)

def fetch_top_news():
    try:
        response = requests.get(NEWS_API_URL)
        response.raise_for_status()
        data = response.json()
        articles = data.get('articles', [])
        news_list = [
            {
                'title': article['title'],
                'url': article['url']
            }
            for article in articles
        ]
        return news_list
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []

def update_html(news_list):
    # Read the template.html
    with open('template.html', 'r', encoding='utf-8') as file:
        html = file.read()

    # Prepare news items as list elements with links
    news_items = "\n".join(
        f'<li><a href="{article["url"]}" target="_blank" rel="noopener noreferrer">{article["title"]}</a></li>'
        for article in news_list
    )

    # Replace placeholder with news items
    html = html.replace('<!-- NEWS_PLACEHOLDER -->', news_items)

    # Replace the date placeholder ({{date}}) with today's date in desired format
    today_str = datetime.now().strftime('%B %d, %Y')
    html = html.replace('{{date}}', today_str)

    # Write the updated HTML to index.html
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(html)

    print(f"✅ Total articles fetched: {len(news_list)}")
    print("✅ index.html updated with top news.")

if __name__ == "__main__":
    news = fetch_top_news()
    update_html(news)
