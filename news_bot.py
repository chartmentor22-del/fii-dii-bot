import requests

# आपकी सही डिटेल्स
TOKEN = "8358591937:AAFx0QhlswIGkn0Ell8Be8ueV4RKRRUUFiQ"
CHAT_ID = "-1002340328243"
API_KEY = "683bfbea1d8f4efe8e1df7e35e64653f"

def get_live_market_news():
    try:
        # हम 'business' कैटेगरी में भारत की टॉप खबरें मांग रहे हैं
        url = f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={API_KEY}"
        response = requests.get(url).json()
        
        articles = response.get('articles', [])
        
        if not articles or len(articles) == 0:
            # अगर ताज़ा खबरें नहीं मिली, तो 'Stock Market' सर्च करके खबरें लाओ
            search_url = f"https://newsapi.org/v2/everything?q=stock+market+india&language=hi&sortBy=publishedAt&apiKey={API_KEY}"
            response = requests.get(search_url).json()
            articles = response.get('articles', [])

        if not articles:
            return "⚠️ बाज़ार में फिलहाल कोई बड़ी खबर अपडेट नहीं हुई है। अपडेट के लिए जुड़े रहें।"

        news_message = "🚀 *Market News Update:*\n\n"
        # पहली 4 बड़ी और काम की खबरें
        count = 0
        for art in articles:
            title = art.get('title')
            if title and "Removed" not in title and count < 4:
                news_message += f"🔹 *{title}*\n\n"
                count += 1
        
        news_message += "━━━━━━━━━━━━━━━━━━\n✅ *By @Chartmentor_News_bot*"
        return news_message
    except Exception as e:
        return f"❌ न्यूज़ लाने में तकनीकी दिक्कत आ रही है।"

def send_news(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

if __name__ == "__main__":
    content = get_live_market_news()
    send_news(content)

