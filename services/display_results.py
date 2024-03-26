import os
from termcolor import colored

def display(productObj):
    print("View discovered products:\n")

    sort = []
    sort.append(input("Sort by price [1] or rating [2]: "))
    sort.append(input("Sort ascending [1] or descending [2]: "))
    products = []
                
    sortKey = sort[0] if sort and sort[0] in ['1', '2'] else '2'
    sortOrder = sort[1] if len(sort) == 2 and sort[1] in ['1', '2'] else '2'
    order = sortOrder == '1' #if sort order is ascending

    if sortKey == '1':
        productObj.sortPrice(ascending=order)
    elif sortKey == '2':
        productObj.sortRating(ascending=order)

    total = len(productObj.products)
    itemIndex = 0
    savedItems = []

    while itemIndex < total:
        os.system('cls')
        current = productObj.products[itemIndex]

        print(colored("+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+\n", color="cyan"))  
        print(f"{itemIndex+1}/{total}")
        print(f'Min: ${productObj.min}, Max: ${productObj.max}, Average: ${round(productObj.ave, 2)}\n')
        print(colored("Item Description:", color="red"), current["description"])
        print(colored("Price:", color="red"), current["price"])
        print(colored("Product Rating:", color="red"), current["rating"])
        print(colored("Store:", color="red"), current["store"])
        print(colored("Store Link:", color="red"), current["store_link"])
        print(colored("Product Link:", color="red"), current["product_link"])
        
        action = input(colored("\nPress Enter to view the next item, 'b' to go back, 's' to save, and 'exit' to exit: ", color='green'))

        if action.lower() == 'exit':
            break
        elif action.lower() == 's':
            if current not in savedItems: savedItems.append(current)
        elif action.lower() == 'b':
            if itemIndex > 0:
                itemIndex -= 1
        else:
            itemIndex += 1

    return savedItems
