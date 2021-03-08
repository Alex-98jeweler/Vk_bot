import requests
from bs4 import BeautifulSoup as bs

token = 'your token from vk'



group_id = 'id your group VK' 



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
