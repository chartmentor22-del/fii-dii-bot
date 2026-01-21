
import requests

# आपकी डिटेल्स
TOKEN = "8358591937:AAFx0QhlswIGkn0Ell8Be8ueV4RKRRUUFiQ"
CHAT_ID = "-1002340328243"
API_KEY = "683bfbea1d8f4efe8e1df7e35e64653f" # आपकी नई API Key

def get_live_market_news():
    try:
        # Google News और टॉप बिजनेस सोर्स से खबरें लाने के लिए
        url = f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={API_KEY}"
        response = requests.get(url).json()
        
        articles = response.get('articles', [])
        if not articles:
            return None

        # पहली 3 बड़ी खबरें चुनना
        news_message = "🚀 *Market News Update:*\n\n"
        for art in articles[:3]:
            title = art.get('title')
            description = art.get('description')
            if title:
                news_message += f"🔹 *{title}*\n"
                if description:
                    news_message += f"_{description[:100]}..._\n\n"
        
        news_message += "✅ *Stay Updated with @Chartmentor_News_bot*"
        return news_message
    except Exception as e:
        print(f"Error fetching news: {e}")
        return None

def send_news(message):
    if message:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
        requests.post(url, json=payload)

if __name__ == "__main__":
    content = get_live_market_news()
    send_news(content)

