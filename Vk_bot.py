import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import config
import json
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
}

class VkBot(object):

    def __init__(self, user_id):
        print('Bot has created!')
        self._USER_ID = user_id
        self._USERNAME = self.get_username(user_id)

        self._COMMANDS = ["ПРИВЕТ", "ПОКА","ПОГОДА","ВРЕМЯ","ПОДДЕРЖАТЬ💰","НОВИНКИ","О НАС",]
        self._CITIES = ['ПОГОДА НОВОСИБИРСК', 'ПОГОДА УЛАН-УДЭ' 'ПОГОДА МОСКВА']

    def get_username(self, user_id):
        r = requests.get('https://vk.com/id' + str(user_id), headers = HEADERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        user_name_string = soup.find('h1', class_='page_name').get_text(strip=True)
        user_name = ""
        for i in user_name_string:
            if i == ' ':
                break
            else:
                user_name += i

        return user_name


    def new_messg(self, message):

        if message.upper() == self._COMMANDS[0]:
            return f'Дороу уебок по имени {self._USERNAME}!'

        elif message.upper() == self._COMMANDS[1]:
            return f'Уходишь? Ну и пиздуй!'

        elif message.upper() == self._COMMANDS[2]:
            return f'Держи епта{self.get_weather("Улан-Удэ")}'

        elif message.upper() == self._COMMANDS[3]:
            return f'Московское время: {self.get_time()}'

        elif message.upper() == self._COMMANDS[4]:
            return f'Ссылка где ты можешь задотанить нам денюжку - '

        elif message.upper() == self._COMMANDS[5]:
            return f'Мы предоставляем тебе наши новинки:'

        elif message.upper() == self._COMMANDS[6]:
            return f'Наша группа состоит из двух людей \n ' \
                   f'@id244358555(Марк) - вокалист и играет на гитаре прикольные ритм партии \n' \
                   f'@id296362815(Саша) - играет на гитаре и иногда подпевает'

        else:
            return 'Иди-ка Нахуй педро!'

    def get_weather(self, city ):
        r = requests.get('https://sinoptik.com.ru/погода-' + city.lower(), headers = HEADERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        value_temp = soup.find('div', class_='weather__article_main_temp').get_text(strip=True)
        return value_temp


    def get_time(self):
        html = requests.get('https://time100.ru/', headers = HEADERS)
        soup = BeautifulSoup(html.text, 'html.parser')
        time = soup.find('div', class_='time').get_text()
        return str(time)

    def get_keyboard(self):
        keyboard = config.keyboard
        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))
        return keyboard