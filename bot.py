import requests
import json

# आपका टोकन और चैनल आईडी
TOKEN = "8342805103:AAGt3Z4sFm5OGKTMastLXdU3Noq3KzuSsDw"
CHAT_ID = "@chartmentor22"

def get_fii_dii_data():
    try:
        # FII/DII डेटा के लिए API
        response = requests.get("https://api.stockedge.com/api/v1/content/fii-dii-activity")
        data = response.json()[0] 
        
        date = data['DateString']
        fii_net = data['FiiNet']
        dii_net = data['DiiNet']
        
        status_fii = "🟢 Buy" if fii_net > 0 else "🔴 Sell"
        status_dii = "🟢 Buy" if dii_net > 0 else "🔴 Sell"

        msg = f"📊 *FII & DII Daily Activity*\n"
        msg += f"📅 *Date:* {date}\n\n"
        msg += f"🚀 *FII Net:* {fii_net} Cr ({status_fii})\n"
        msg += f"🏠 *DII Net:* {dii_net} Cr ({status_dii})\n\n"
        msg += f"✅ Data shared by @chartmentor22"
        return msg
    except Exception as e:
        return "❌ डेटा अभी अपडेट नहीं हुआ है। कृपया शाम 7:30 के बाद चेक करें।"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

if __name__ == "__main__":
    content = get_fii_dii_data()
    send_telegram(content)
