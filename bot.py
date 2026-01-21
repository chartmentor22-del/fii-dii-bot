import requests

# आपका Telegram सेटअप
TOKEN = "8358591937:AAFx0QhlswIGkn0Ell8Be8ueV4RKRRUUFiQ"
CHAT_ID = "-1002340328243"

def get_fii_dii_data():
    try:
        # NSE API URL
        url = "https://www.nseindia.com/api/fiidiiTradeReact"
        
        # Fake Browser Headers (ताकि NSE ब्लॉक न करे)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.nseindia.com/reports/fii-dii'
        }
        
        session = requests.Session()
        session.get("https://www.nseindia.com", headers=headers, timeout=10)
        response = session.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            latest = data[-1] # सबसे ताज़ा डेटा
            
            msg = f"📊 *FII / DII Cash Activity*\n"
            msg += f"📅 *Date:* {latest['date']}\n\n"
            msg += f"🏦 *FII Net:* {latest['fiiNetValue']} Cr\n"
            msg += f"🏠 *DII Net:* {latest['diiNetValue']} Cr\n\n"
            msg += "✅ *Updates by @Chartmentor_News_bot*"
            return msg
        else:
            return "⚠️ NSE वेबसाइट से डेटा नहीं मिल पा रहा है (Status Code Error)।"
            
    except Exception as e:
        return f"⚠️ अभी डेटा अपडेट नहीं हुआ है या NSE साइट बिजी है।"

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

if __name__ == "__main__":
    content = get_fii_dii_data()
    send_to_telegram(content)
