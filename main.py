import os
from termcolor import colored

from services.tac_query import getModel
from services.utils import testing, getUserConfirmation
from services.price_query import getProductData


if __name__ == "__main__":
    
    done = False
    
    #Welcome Sequence
    while(not done):
        os.system('cls')
        print(colored("+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+", color="cyan"))

        print("\nWelcome! To retrieve Canadian shopping prices for your device, please enter your TAC code below. \nIf you are here by mistake and would like to exit the program, enter 'exit'.\n")
        code = input("Enter your 8-digit TAC code: ")
        if code == "exit": done = True
        else:
            confirm = getUserConfirmation(f"TAC code: {code}. Is this correct? (Y/N): ")
            while confirm == "N":
                code = input("Please enter your code again again: ")
                confirm = getUserConfirmation(f"TAC code: {code}. Is this correct? (Y/N): ")

            os.system('cls')
            print(colored("+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+", color="cyan"))
            model = getModel(code=code)

            os.system('cls')
            print(colored("+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+", color="cyan"))
            productArray = getProductData(query=model)

            os.system('cls')
            print(colored("+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+", color="cyan"))
            getProductData(query=model)

            os.system('cls')
            print(colored("+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+_-_-_+", color="cyan"))
            repeat = input("Press Enter to query , or type 'exit' to quit: ")
            if repeat.lower() == 'exit':
                done = True
            
        # done = True