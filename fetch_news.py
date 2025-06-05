import requests
from datetime import datetime

API_KEY = "YOUR_NEWSAPI_KEY"  # Replace with your actual NewsAPI key
URL = f"https://newsapi.org/v2/top-headlines?country=in&category=general&pageSize=10&apiKey={API_KEY}"

def fetch_top_news():
    try:
        response = requests.get(URL)
        data = response.json()

        if data["status"] != "ok":
            print("❌ Failed to fetch news. Status:", data["status"])
            return []

        articles = data.get("articles", [])
        news_list = []

        for article in articles:
            title = article.get("title", "No Title")
            url = article.get("url", "#")
            news_list.append({"title": title, "url": url})

        print(f"✅ Total articles fetched: {len(news_list)}")
        return news_list

    except Exception as e:
        print("❌ Error while fetching news:", str(e))
        return []

def update_html(news_list):
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            html = f.read()

        today = datetime.now().strftime("%B %d, %Y")

        # Create the updated news list HTML
        news_items_html = "\n".join(
            f'<li><a href="{article["url"]}" target="_blank" rel="noopener">{article["title"]}</a></li>'
            for article in news_list
        )

        # Replace content inside <ul>...</ul> and date
        import re
        html = re.sub(r"<p class=\"date\">.*?</p>", f"<p class=\"date\">{today}</p>", html)
        html = re.sub(r"<ul>.*?</ul>", f"<ul>\n{news_items_html}\n</ul>", html, flags=re.DOTALL)

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)

        print("✅ index.html updated with top news.")

    except Exception as e:
        print("❌ Error while updating HTML:", str(e))

if __name__ == "__main__":
    news = fetch_top_news()
    if news:
        update_html(news)
