import requests
from bs4 import BeautifulSoup as bs, BeautifulSoup
import pandas as pd

url = "https://www.chitai-gorod.ru/comics"
response = requests.get(url)

# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Находим все элементы с классом "product-card"
products = soup.find_all(class_="product-card slider__item-card")

print(products)

# Открываем файл для записи данных
with open("comics_data.txt", "w", encoding="utf-8") as file:
    for product in products:
        title = product.find(class_="product-title__head").text.strip()

        author_element = product.find(class_="product-title__author")
        if author_element:
            author = author_element.text.strip()
        else:
            author = ""

        rating_element = product.find(class_="star-rating__statistics")
        if rating_element:
            rating = rating_element.text.strip()
        else:
            rating = ""

        old_price_element = product.find(class_="product-price__old")
        if old_price_element:
            old_price = old_price_element.text.strip()
        else:
            old_price = ""

        sale_price_element = product.find(class_="product-price__value product-price__value--discount")
        if sale_price_element:
            sale_price = sale_price_element.text.strip()
        else:
            sale_price = product.find(class_="product-price__value").text.strip()

        file.write(f"Название: {title}\n")
        file.write(f"Автор: {author}\n")
        file.write(f"Рейтинг: {rating}\n")
        file.write(f"Старая цена: {old_price}\n")
        file.write(f"Новая цена: {sale_price}\n")
        file.write("\n")


