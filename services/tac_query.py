import time
from DrissionPage import ChromiumPage, ChromiumOptions
from yaspin import yaspin

from services.utils import getUserConfirmation

def getModel(code: str):  
    model = None
    response = None
    with yaspin(text="Retrieving device from TAC (Windows will open and close)", color="cyan") as sp:
        try: 
            #Assemble URL for querying device model
            URL = f'https://swappa.com/imei/tac/{code}'
            time.sleep(1)
            sp.write("> Accessing TAC index: Human verification required, please do not close the pop-up window.")
            

            # Initialize ChromiumPage and fetch page elements with DrissionPage
            co = ChromiumOptions().auto_port()
            page = ChromiumPage(co)
            page.get(URL)
            page.wait.ele_loaded('tag:div@@class=col-7') #wait for cloudflare to check that user is human through user agent
            time.sleep(2)
            sp.write("> Site access granted: Human verification success.")

            # Query by static page element (Swappa standard)
            div = page.ele('tag:div@@class=col-7')
            model = div.ele('tag:h2').text
            
            # Split the text into an array of strings
            response = ' '.join(item.strip() for item in model.split('\n') if item.strip())
            time.sleep(3)
            sp.ok("✔")

            page.quit()

        except:
            page.quit()
            time.sleep(2)
            sp.write("> An error occurred!")
            sp.ok("X")

            print("\nAn error occured while attempting to determine your TAC's associated device. Please verify your number is correct and your Chrome runtime is up-to-date.\n")
            manual = getUserConfirmation("You may also elect to manually input your device model.\nWould you like to do so? (Y/N): ")
            if manual == "Y":
                model = input("Enter your device model: ")
                confirm = getUserConfirmation(f"You entered {model}. Is this correct? (Y/N): ")
                while confirm == "N":
                    model = input("Please enter your device model again: ")
                    confirm = getUserConfirmation(f"You entered {model}. Is this correct? (Y/N): ")
                response = model
            elif manual == "N":
                pass
            else:
                print("Invalid input.")
    
    return response