import re
from datetime import datetime

EXIT_CODE = 'exit'

def getUserConfirmation(prompt:str):
    while True:
        response = input(prompt).strip().upper()
        if response in ('Y', 'N'):
            return response
        else:
            print("Please enter 'Y' for Yes or 'N' for No.")

def validateCode(code:str):
    if re.match(r'^\d{8}$', code):
        return True
    else:
        return False
    
def writeToFile(savedItems):
    current_date = datetime.now().strftime("%Y%m%d")
    filename = f"saved-results-{current_date}.txt"

    with open(f'./saved-results/{filename}', "w") as file:
        for index, item in enumerate(savedItems, start=1):
            file.write(f"Item {index}:\n")
            file.write(f"Item Description: {item['description']}\n")
            file.write(f"Price: {item['price']}\n")
            file.write(f"Product Rating: {item['rating']}\n")
            file.write(f"Store: {item['store']}\n")
            file.write(f"Store Link: {item['store_link']}\n")
            file.write(f"Product Link: {item['product_link']}\n\n")
