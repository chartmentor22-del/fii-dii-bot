import requests

# Aapka Setup
TOKEN = "8358591937:AAFx0QhlswIGkn0Ell8Be8ueV4RKRRUUFiQ"
CHAT_ID = "-1002340328243"

def get_fii_dii():
    try:
        url = "https://www.nseindia.com/api/fiidiiTradeReact"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Referer': 'https://www.nseindia.com/'
        }
        session = requests.Session()
        session.get("https://www.nseindia.com", headers=headers, timeout=10)
        response = session.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            latest = data[-1]
            msg = f"📊 *FII / DII Daily Activity*\n📅 *Date:* {latest['date']}\n\n"
            msg += f"🏦 *FII Net:* {latest['fiiNetValue']} Cr\n"
            msg += f"🏠 *DII Net:* {latest['diiNetValue']} Cr\n\n"
            msg += "✅ *Automated Update*"
            return msg
        return "⚠️ NSE site se data nahi mil raha."
    except:
        return "⚠️ Data update hone mein samay lag raha hai."

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"})

if __name__ == "__main__":
    message = get_fii_dii()
    send_to_telegram(message)

