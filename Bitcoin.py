import requests
import time
#global valiables
api_key='a4f020ce-db80-4185-9675-1103905b798f'
bot_token='5290328434:AAFF4Y7EaTatUUXBiH-GDpIfsfGHFj96R0s'
chat_id='1207241655'
limit=59000
time_interval =5*60
def get_price():
    url='https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }
    response = requests.get(url,headers=headers).json()
    btc_price=response['data'][0]['quote']['USD']['price']
    return btc_price

def send_update(chat_id,msg):
    url=f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)
def main():
    while True:
        price = get_price()
        if price < limit:
            send_update(chat_id, f"bitcoin price : {price}")
        time.sleep(time_interval)

main()

