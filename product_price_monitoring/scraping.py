import lxml.html as parser
import requests
import csv
from urllib.parse import urlsplit, urljoin
import pandas as pd
import numpy as np
from datetime import datetime
import pytz

products = pd.read_csv('products.csv')

products['product_title'] = [str.replace(x, ' ', '-') for x in products['product_title']]
products['product_title'] = [str.replace(x, '.', '-') for x in products['product_title']]
products['product_title'] = [str.replace(x, ',', '-') for x in products['product_title']]

product_prices = pd.DataFrame(columns = ['created_at', 'product_title', 'url', 'source_code', 'prices', 'stores'])

for i, p in enumerate(products['product_title']):

    url = 'https://www.buscape.com.br/' + p
    r = requests.get(url, stream=True)
    html = parser.fromstring(r.text)

    prices = html.xpath("//span[@class='secondary-price']/text()")
    prices = [float(x.replace(',', '').replace('.', '')) / 100 for x in prices if x != "Total a prazo R$ "]
    
    stores = html.xpath("//div[@class='offer__seller']/img/@alt")
    
    for price, store in zip(prices, stores):
        product_prices = product_prices.append(
            {
            'created_at': datetime.utcnow().replace(tzinfo=pytz.UTC),
            'product_title': products.loc[i, 'product_title'],
            'url': url,
            'source_code': r.text,
            'prices': price,
            'stores': store,
            },
            ignore_index=True,
        )


product_prices.to_csv('prices.csv', index=False)
