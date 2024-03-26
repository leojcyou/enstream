import json

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

def testing():
    config = load_config()
    return config['testing']

#---------- Testing Functions ----------#
def tprint(arg):
    if testing(): print(arg)
    return

#---------- Useful Human Functions ----------#
def getUserConfirmation(prompt):
    while True:
        response = input(prompt).strip().upper()
        if response in ('Y', 'N'):
            return response
        else:
            print("Please enter 'Y' for Yes or 'N' for No.")