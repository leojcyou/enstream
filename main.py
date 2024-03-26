import os
from termcolor import colored

from services.tac_query import getModel
from services.utils import validateCode, writeToFile
from services.price_query import getProductData
from services.display_results import display


if __name__ == "__main__":
    
    done = False
    
    #Welcome Sequence
    while(not done):
        os.system('cls')
        print(colored("+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+\n", color="cyan"))

        print("Welcome! To retrieve Canadian shopping prices for your device, please enter your TAC code below.\n")
        code = input("Enter your 8-digit TAC code or 'exit' to quit: ")
        if code == "exit": break
        while(not validateCode(code=code)):
            code = input("Invalid input: Enter your 8-digit TAC code: ")

        os.system('cls')
        print(colored("+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+\n", color="cyan"))
        model = getModel(code=code)
        if model is None: pass
        else:
            os.system('cls')
            print(colored("+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+\n", color="cyan"))
            productArray = getProductData(model=model)

            os.system('cls')
            print(colored("+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+\n", color="cyan"))
            saved = display(productArray)
            writeToFile(saved)

        os.system('cls')
        print(colored("+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+\n", color="cyan"))
        done = True if input("Press Enter to query another code. Enter 'exit' to quit the program: ") == 'exit' else False