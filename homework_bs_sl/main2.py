from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.banki.ru/products/currency/usd/"

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)

# Delete current country cookie
driver.delete_cookie('usrIpCountry')
# Set a cookie with country France
driver.add_cookie({'name': 'usrIpCountry', 'value': 'usd', 'domain': 'www.banki.ru'})

# Refresh before proceeding
driver.refresh()

soup = BeautifulSoup(driver.page_source, 'lxml')
price = []
for price_tag in soup.find_all('span', class_='product-preview__old-price'):
    price.append(price_tag.text)
