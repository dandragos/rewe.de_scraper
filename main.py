import requests
import json

searchword = 'tomatenmark'

headers = {
    'accept': 'application/vnd.rewe.productlist+json',
    'referer': 'https://shop.rewe.de/productList?search=k%C3%A4se',
    'authority': 'shop.rewe.de',
    'sec-fetch-site': 'same-origin',
}

params = {
    'market': '231006',
    'objectsPerPage': '100',
    'page': '1',
    'search': searchword,
    'serviceTypes': 'DELIVERY,PICKUP',
    'sorting': 'RELEVANCE_DESC',
    'source': '',
}

response = requests.get('https://shop.rewe.de/api/products', headers=headers, params=params)

if response.status_code == 200:
    json_response = response.json()
    if "validationErrors" in json_response:
        print("Erori de validare existente:")
        for error in json_response["validationErrors"]:
            print(f'Camp: {error["name"]}, Motiv: {error["reason"]}')
    else:
        products = json_response.get('_embedded', {}).get('products', [])
        for product in products:
            product_name = product.get('productName', 'N/A')
            brand = product.get('brand', 'N/A')
            price = product.get('_embedded', {}).get('articles', [{}])[0].get('_embedded', {}).get('listing', {}).get('pricing', {}).get('currentRetailPrice', 'N/A')
            gtin = product.get('_embedded', {}).get('articles', [{}])[0].get('gtin', 'N/A')
            if isinstance(price, int) or isinstance(price, float):
                price = '{:.2f}'.format(price / 100).replace('.', ',') + " €"
            print(f'Product Name: {product_name}, Brand: {brand}, Price: {price}, GTIN: {gtin}')
else:
    print("Solicitare esuată:", response.status_code)


