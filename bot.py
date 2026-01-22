import requests

# Setup
TOKEN = "7848682437:AAHJkk_uwhIJMdtVuTndsMupMiELraNCaIs"
CHAT_ID = "@chartmentor22"

def get_data():
    msg = ""
    # 1. FII / DII Data
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        session = requests.Session()
        session.get("https://www.nseindia.com", headers=headers, timeout=10)
        fii_res = session.get("https://www.nseindia.com/api/fiidiiTradeReact", headers=headers, timeout=10)
        if fii_res.status_code == 200:
            latest = fii_res.json()[-1]
            msg += f"📊 *FII / DII Activity ({latest['date']})*\n"
            msg += f"🏦 FII Net: {latest['fiiNetValue']} Cr\n"
            msg += f"🏠 DII Net: {latest['diiNetValue']} Cr\n\n"
    except:
        msg += "⚠️ FII/DII data abhi NSE pe update nahi hua.\n\n"

    # 2. Market News
    try:
        news_url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=768172c39547466885368a6234f9a066"
        news_res = requests.get(news_url, timeout=10)
        if news_res.status_code == 200:
            articles = news_res.json().get('articles', [])[:5]
            msg += "📰 *Market News:*\n"
            for art in articles:
                msg += f"• {art['title']}\n"
    except:
        msg += "⚠️ News fetch karne mein dikkat hui."
    return msg

def send(text):
    if text:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"})

if __name__ == "__main__":
    send(get_data())
