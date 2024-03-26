import time
from DrissionPage import ChromiumPage, ChromiumOptions
from yaspin import yaspin

from services.utils import tprint, testing, getUserConfirmation

def getModel(code: str):  
    model = None
    result = None
    response = None
    with yaspin(text="Retriving device from TAC (Windows will open and close)", color="cyan") as sp:
        try: 
            #Assemble URL for querying device model
            URL = f'https://swappa.com/imei/tac/{code}'
            tprint(URL)
            time.sleep(1)
            sp.write("> Accessing TAC index: Human verification required, please do not close the pop-up window.")
            

            # Initialize ChromiumPage and fetch page elements with DrissionPage
            co = ChromiumOptions().auto_port()
            page = ChromiumPage(co)
            page.get(URL)
            sp.write("> Verifying: Move your cursor about the page to expedite this process.")
            time.sleep(2)
            page.wait.ele_loaded('tag:div@@class=col-7') #wait for cloudflare to check that user is human through user agent
            time.sleep(3)
            sp.write("> Site access granted: human verification success")

            # Query by static page element (Swappa standard)
            div = page.ele('tag:div@@class=col-7')
            model = div.ele('tag:h2').text
            
            #testing mode prints
            tprint(div)
            tprint(model)

            # Split the text into an array of strings
            result = ' '.join(item.strip() for item in model.split('\n') if item.strip())
            time.sleep(4)
            sp.write("> Site access granted: human verification success")
            sp.ok("✔")

            page.quit()
        except:
            page.quit()
            time.sleep(3)
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
                result = model
            elif manual == "N":
                pass
            else:
                print("Invalid input.")
    
    response = result.split()
    response = '+'.join(response)
    return response