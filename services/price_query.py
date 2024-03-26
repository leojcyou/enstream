import time
import requests
from parsel import Selector
from yaspin import yaspin
import numpy as np

class ProductResults:
    def __init__(self):
        self.products = []

        self.max = None
        self.min = None
        self.ave = None

    def construct(self, product_list):
        prices = []

        for obj in product_list:
            self.products.append(obj)
            if obj['price']:
                prices.append(float(obj['price'].replace('$', '').replace(',', '')))
        
        #Using IQR to filter outliers at 10% margins
        q1, q3 = np.percentile(prices, [10, 90])
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        # Filter and remove prices within the bounds
        filteredProducts = []
        for obj, price in zip(self.products, prices):
            if lower_bound <= price <= upper_bound:
                filteredProducts.append(obj)

        self.products = filteredProducts

        # Set max, min, and average using filtered prices
        filteredPrices = [price for price in prices if lower_bound <= price <= upper_bound]
        self.max = max(filteredPrices) if filteredPrices else None
        self.min = min(filteredPrices) if filteredPrices else None
        self.ave = sum(filteredPrices) / len(filteredPrices) if filteredPrices else None

    def sortPrice(self, ascending=True):
        res = self.products.sort(key=lambda x: float(x['price'].replace('$', '').replace(',', '')) if x['price'] else float('inf'), reverse=not ascending)
        return res
    
    def sortRating(self, ascending=True):
        res = self.products.sort(key=lambda x: float(x['rating']) if x['rating'] else float('inf'), reverse=not ascending)
        return res
    
def getProductData(model: str):
    #assemble the query for Google's URL format
    query = model.split()
    query = '+'.join(query)
    params = {
        "q": query,
        "hl": "en",
        "gl": "ca", 
        "tbm": "shop"
    }

    #Headers with user-agent to prevent 403 error
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0" }

    with yaspin(text=f'Retrieving product prices for {model}.', color="cyan") as sp:
        time.sleep(1)
        sp.write("> Scraping the web for product prices.")
        html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
        selector = Selector(html.text)
        res = []

        #Parsing the returned results and mapping to object
        for index, result in enumerate(selector.css(".Qlx7of .i0X6df")):
            if index >= 30:
                break
            description = result.css(".tAxDx::text").get()        
            product_link = "https://www.google.com" + result.css(".Lq5OHe::attr(href)").get()   
            product_rating = result.css(".NzUzee .Rsc7Yb::text").get() 
            price = result.css(".a8Pemb::text").get()       
            store = result.css(".aULzUe::text").get()       
            store_link = "https://www.google.com" + result.css(".eaGTj div a::attr(href)").get()        

            obj = {
                "description": description,
                "price": price,
                "store": store,
                "rating": product_rating,
                "store_link": store_link,
                "product_link": product_link
            }
            res.append(obj)

        time.sleep(2)
        sp.write("> Search complete!")
        sp.ok("✔")

    #Load into class
    response = ProductResults()
    response.construct(res)
    return response
