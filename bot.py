import requests

# आपका पुराना Telegram सेटअप
TOKEN = "8358591937:AAFx0QhlswIGkn0Ell8Be8ueV4RKRRUUFiQ"
CHAT_ID = "-1002340328243"

def get_fii_dii():
    try:
        url = "https://www.nseindia.com/api/fiidiiTradeReact"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br'
        }
        session = requests.Session()
        session.get("https://www.nseindia.com", headers=headers)
        response = session.get(url, headers=headers).json()
        
        data = response[-1]
        msg = f"📊 *FII / DII Data Update*\n📅 Date: {data['date']}\n\n"
        msg += f"🏦 *FII Net:* {data['fiiNetValue']} Cr\n"
        msg += f"🏠 *DII Net:* {data['diiNetValue']} Cr\n\n"
        msg += "✅ *@Chartmentor_News_bot*"
        return msg
    except:
        return "⚠️ NSE वेबसाइट पर अभी डेटा अपडेट नहीं हुआ है।"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

if __name__ == "__main__":
    message = get_fii_dii()
    send_message(message)


