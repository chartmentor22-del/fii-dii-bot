import requests

# Aapki Details
TOKEN = "8358591937:AAFx0QhlswIGkn0Ell8Be8ueV4RKRRUUFiQ"
CHAT_ID = "-1002340328243"
API_KEY = "683bfbea1d8f4efe8e1df7e35e64653f"

def get_news():
    try:
        # Market ki latest hindi news ke liye query
        url = f"https://newsapi.org/v2/everything?q=nifty+sensex+stock+market&language=hi&sortBy=publishedAt&apiKey={API_KEY}"
        response = requests.get(url).json()
        articles = response.get('articles', [])

        if not articles:
            return "📢 Abhi market ki koi nayi news nahi mili hai."

        msg = "🚀 *LIVE Market News Update:*\n\n"
        # Top 3 headlines
        for art in articles[:3]:
            title = art.get('title')
            if title:
                msg += f"🔹 {title}\n\n"
        
        msg += "━━━━━━━━━━━━━━━━━━\n✅ *By @Chartmentor_News_bot*"
        return msg
    except Exception as e:
        return "⚠️ News fetch karne mein dikkat aa rahi hai."

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

if __name__ == "__main__":
    content = get_news()
    send_to_telegram(content)
