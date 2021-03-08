import requests
from bs4 import BeautifulSoup as bs

token = '991e5b3a5f38afff473be81ad9a4fb71e37dc79d382fc623b2141dff3dbf8205286b185263b7fb2030147'

token1 = '29d55d2fa26844cc115eaac59c3e1433722b5eb1b794c5aac529be8b2b083b812362f181bd599a0582a2a'

group_id = 151028628

group_id_1 = 149403717

keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "open_link",
                "link": 'https://vk.com/alexandr_yuvelir',
                 "label": "Поддержать💰",
                "payload": "{\"button\": \"1\"}",

            },
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Новинки"
            },
            "color": "default"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "О нас"
            },
            "color": "default"
            }
        ]
    ]
}




def get_time():
    html = requests.get('https://time100.ru/')
    soup = bs(html.text, 'html.parser')
    time = soup.find('div', class_='time').get_text()
    return str(time)

def get_weather():
    html = requests.get('https://weather.rambler.ru/v-moskve/')
    soup = bs(html.text, 'html.parser')
    weather = soup.find('div', class_='_1HBR').get_text()
    return str(weather)