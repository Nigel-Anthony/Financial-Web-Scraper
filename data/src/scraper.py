import os
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_stock_price(url):
    """
    this is example of docstring
    """

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    try:
        price_element = driver.find_element(
            By.XPATH, '//fin-streamer[@data-field="regularMarketPrice"]'
        )
        price = price_element.text
    except Exception as e:
        print("Error scraping stock price", e)
        price = None

    driver.quit()
    return price


def get_crypto_price(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    crypto_price = soup.find("div", class_="priceValue")
    return crypto_price.text.strip() if crypto_price else None


def get_financial_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = []
    for tag in soup.find_all("h2", class_="news-headline"):
        headlines.append(tag.get_text(strip=True))
    return headlines


def save_data(data, filename, file_format="csv"):
    import os

    df = pd.DataFrame(data)
    # Adjust path to use project root's data folder
    filepath = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", filename
    )

    # Ensure the directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    if file_format == "csv":
        df.to_csv(filepath, index=False)
    elif file_format == "json":
        df.to_json(filepath, orient="records", indent=4)
    print(f"Data saved to {filepath}")
