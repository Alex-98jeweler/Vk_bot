from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import requests
import vk_api
from config import *

session = vk_api.VkApi(token=token1)
api = session.get_api()
users = [247982069, 244358555, 296362815]

for id_s in users:
    api.messages.send(user_id = id_s, random_id = 0, message = 'Господа, это тестовая рассылка, не пугайтесь, просто проверяю построенную теорию! Всех люблю!')









