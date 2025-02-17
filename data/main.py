# main.py

from src import scraper, sentiment


def main():
    stock_url = "https://finance.yahoo.com/quote/AAPL"
    crypto_url = "https://coinmarketcap.com/currencies/bitcoin/"
    news_url = "https://www.reuters.com/finance"

    # Scrape stock price
    stock_price = scraper.get_stock_price(stock_url)
    print("Stock Price:", stock_price)

    # Scrape cryptocurrency data

    crypto_price = scraper.get_crypto_price(crypto_url)
    print("Cryptocurrency Price:", crypto_price)

    # Scrape financial news headlines
    headlines = scraper.get_financial_news(news_url)
    print("News Headlines:")
    for idx, headline in enumerate(headlines, start=1):
        print(f"{idx}. {headline}")

    # Analyze sentiment of headlines
    sentiment_results = sentiment.analyze_headlines(headlines)
    for result in sentiment_results:
        print(
            f"Headline: {result['headline']}\nSentiment Score: {result['sentiment']}\n"
        )

    # Combine data for saving (example for stock and crypto; expand as needed)
    data_to_save = [
        {
            "stock_price": stock_price,
            "crypto_price": crypto_price,
        }
    ]
    scraper.save_data(data_to_save, "financial_data.csv", file_format="csv")


if __name__ == "__main__":
    main()
