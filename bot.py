import requests
import pandas as pd

# आपकी टेलीग्राम डिटेल्स
TOKEN = "8358591937:AAFx0QhlswIGkn0Ell8Be8ueV4RKRRUUFiQ"
CHAT_ID = "-1002340328243"

def get_fii_dii_data():
    try:
        url = "https://www.nseindia.com/api/fiidiiTradeReact"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        
        # NSE वेबसाइट को एक्सेस करने के लिए सेशन
        session = requests.Session()
        session.get("https://www.nseindia.com", headers=headers)
        response = session.get(url, headers=headers).json()
        
        # डेटा निकालना
        latest_data = response[-1] # सबसे नया डेटा
        date = latest_data['date']
        fii_net = latest_data['fiiNetValue']
        dii_net = latest_data['diiNetValue']
        
        msg = f"📊 *FII / DII Activity Update*\n📅 Date: {date}\n\n"
        msg += f"🏦 *FII Net:* {fii_net} Cr\n"
        msg += f"🏠 *DII Net:* {dii_net} Cr\n\n"
        
        # सेंटीमेंट चेक
        total = float(fii_net.replace(',', '')) + float(dii_net.replace(',', ''))
        if total > 0:
            msg += "🚀 *Market Sentiment: Bullish*"
        else:
            msg += "🐻 *Market Sentiment: Bearish*"
            
        return msg
    except Exception as e:
        return "⚠️ NSE वेबसाइट पर अभी आज का डेटा अपडेट नहीं हुआ है।"

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

if __name__ == "__main__":
    message = get_fii_dii_data()
    send_to_telegram(message)

