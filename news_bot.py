import requests

# --- सेटिंग्स ---
NEWS_TOKEN = "8358591937:AAFx0QhlswIGkn0Ell8Be8ueV4RKRRUUFiQ" # आपका नया न्यूज़ बॉट
CHAT_ID = "-1002340328243"
NEWS_API_KEY = "683bfbea1d8f4efe8e1df7e35e64653f"

def get_market_news():
    try:
        # हिंदी न्यूज़ सर्च करना
        url = f"https://newsapi.org/v2/everything?q=nifty+sensex+market&language=hi&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
        response = requests.get(url).json()
        articles = response.get('articles', [])

        if not articles:
            return "📢 बाज़ार में फिलहाल स्थिरता बनी हुई है।"

        msg = "🚀 *Market News Update (Hindi):*\n\n"
        for art in articles[:3]: # टॉप 3 खबरें
            msg += f"🔹 {art['title']}\n\n"
        
        msg += "━━━━━━━━━━━━━━━━━━\n✅ *Updates by @Chartmentor_News_bot*"
        return msg
    except:
        return "⚠️ न्यूज़ सर्वर से डेटा नहीं मिल पा रहा है।"

def send_telegram(text):
    url = f"https://api.telegram.org/bot{NEWS_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    r = requests.post(url, json=payload)
    print(f"Telegram Response: {r.status_code}")

if __name__ == "__main__":
    print("Fetching news...")
    news_text = get_market_news()
    send_telegram(news_text)
