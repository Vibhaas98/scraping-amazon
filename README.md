# Amazon Product Scraper
This is an Amazon Product Scraper built using scapy module of python

# Features
it scrape various things
- Product Title
- Product Image
- Product Price
- Product Rating
- Product Discount

By default it scrapes `Mobile Phones`  from `Amazon`.
In case you want to change it to scrape other product, follow the instructions
1. Open file `web-crawler-for-amazon/spiders/amazon_web.py`
2. Chnage the `urls` list

# Execute Amazon Scraper
you can execute the following command
```bash
scrapy crawl amazon_scraper -o data.json
```

It will create `data.json` file inside the `web-crawler-for-amazon ` folder containing all the scraped data in `JSON` format.

# Sample Data
Already fetched sample data is available in `web-crawler-for-amazon ` folder

# Preresuisites
- you have to install `scrapy`
