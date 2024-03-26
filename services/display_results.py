import os
from termcolor import colored

def display_data_one_by_one(productData):
    total_items = len(productData)
    current_item = 0

    for item in productData:
        os.system('cls')
        current_item += 1

        print(colored("+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+", color="cyan"))  
        print(current_item+"/"+total_items+"\n")
        print("Item Description:", item["title"])
        print("Price:", item["price"])
        print("Delivery:", item["delivery"])
        print("Store:", item["store"])
        print("Store Link:", item["store_link"])
        print("Product Link:", item["product_link"])
        
        next_item = input("Press Enter to view the next item, or type 'exit' to quit: ")
        if next_item.lower() == 'exit':
            break
    return