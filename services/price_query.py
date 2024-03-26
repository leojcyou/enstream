import time
import requests
from parsel import Selector
from yaspin import yaspin

def getProductData(query: str):
    params = {
        "q": query,
        "hl": "en",
        "gl": "ca", 
        "tbm": "shop"
    }

    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0" }
    with yaspin(text="Retriving device from TAC (Windows will open and close)", color="cyan") as sp:
        time.sleep(1)
        sp.write("> Scraping the web for product prices")
        html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
        selector = Selector(html.text)
        res = []

        for result in selector.css(".Qlx7of .i0X6df"):
            title = result.css(".tAxDx::text").get()        
            product_link = "https://www.google.com" + result.css(".Lq5OHe::attr(href)").get()   
            price = result.css(".a8Pemb::text").get()       
            store = result.css(".aULzUe::text").get()       
            store_link = "https://www.google.com" + result.css(".eaGTj div a::attr(href)").get()        
            delivery = result.css(".vEjMR::text").get()

            res.append({
                "title": title,
                "price": price,
                "delivery": delivery,
                "store": store,
                "store_link": store_link,
                "product_link": product_link
            })
        time.sleep(2)
        sp.write("> Search complete!")
        sp.ok("✔")
    return res