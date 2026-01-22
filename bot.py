import requests

TOKEN = "8342805103:AAGt3Z4sFnSOGKTMastLXdU3Noq3KzuSsDw"
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
            
            fii = latest['fiiNetValue']
            dii = latest['diiNetValue']
            
            msg = f"📊 *FII / DII Daily Activity*\n"
            msg += f"📅 *Date:* {latest['date']}\n\n"
            msg += f"🏦 *FII Net:* {fii} Cr\n"
            msg += f"🏠 *DII Net:* {dii} Cr\n\n"
            msg += "✅ *Shared by @chartmentor22*"
            return msg
        return "⚠️ NSE पर डेटा अभी उपलब्ध नहीं है।"
    except:
        return "⚠️ डेटा लोड करने में समस्या आई।"

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

if __name__ == "__main__":
    message = get_fii_dii()
    send_telegram(message)
