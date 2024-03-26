import os
from termcolor import colored

from services.utils import validateCode, writeToFile #general utilities for I/O and validation
from services.tac_query import getModel #getting the device model from the TAC
from services.price_query import getProductData #getting the prices and product stats given the device model 
from services.display_results import display #sequence for displaying results


if __name__ == "__main__":
    
    #Loop control
    done = False
    
    while(not done):
        os.system('cls')
        print(colored("+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+\n", color="cyan"))

        #Welcome sequence
        print("Welcome! To retrieve Canadian shopping prices for your device, please enter your TAC code below.\n")
        code = input("Enter your 8-digit TAC code or 'exit' to quit: ")
        if code == "exit": break
        while(not validateCode(code=code)):
            code = input("Invalid input: Enter your 8-digit TAC code: ")

        os.system('cls')
        print(colored("+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+\n", color="cyan"))
        
        #Querying swappa.com with user's browser (Chromium) for TAC to device model conversion
        model = getModel(code=code)
        if model is None: pass
        else:
            os.system('cls')
            print(colored("+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+\n", color="cyan"))
            
            #If the device model is defined, scrape Google shopping for the top 30 products 
            productArray = getProductData(model=model)

            os.system('cls')
            print(colored("+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+\n", color="cyan"))
            
            #Display and save items of interests and write to a file in the folder saved-results. A template is shown there
            saved = display(productArray)
            writeToFile(saved)

        os.system('cls')
        print(colored("+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+\n", color="cyan"))
        done = True if input("Press Enter to query another code. Enter 'exit' to quit the program: ") == 'exit' else False