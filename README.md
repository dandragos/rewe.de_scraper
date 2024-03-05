# rewe.de_scraper
Scraper for rewe.de (german marketplace) -> Returns Product Name, Brand, Price and GTIN of products.

## Description
The script utilizes the requests library to interact with the REWE online shop API. It sends a GET request with specified headers and parameters, including the search term. Upon receiving a successful response (status code 200), it extracts product information from the JSON response and prints details such as product name, brand, price, and GTIN (Global Trade Item Number). If there are validation errors, it displays them accordingly.
