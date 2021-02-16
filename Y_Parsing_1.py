# Добавить в список price цены товаров и названия товаров с сайта:
# https://store.data-analyst.praktikum-services.ru/.
# Определить имена тегов и их атрибуты в панели разработчика.
# Получить нужные элементы методом find_all()
# Сформировать таблицу

import pandas as pd
import requests # Импорт библиотеки для запросов к серверу
from bs4 import BeautifulSoup # Импорт библиотеки для автоматического парсинга странички

URL='https://store.data-analyst.praktikum-services.ru/'
req = requests.get(URL) # GET-запрос
soup = BeautifulSoup(req.text, 'html.parser')

name_products = [] # Список, в котором хранятся названия товаров
for row in soup.find_all('div', attrs = {'class':'t754__title t-name t-name_md js-product-name'}):
    name_products.append(row.text)

price = [] # Cписок, в котором хранятся цены на товар
for row in soup.find_all('div', attrs = {'class':'t754__price-value js-product-price'}):
    price.append(row.text)

products_data = pd.DataFrame({'name': name_products, 'price': price}) # Датафрейм с данными о названии и цене товара

print(products_data.head())