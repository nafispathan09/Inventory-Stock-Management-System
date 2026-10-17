# storage 

import json

def save_products(products):
    with open("data/inventory.json","w") as file:
        json.dump(products,file)       
def load_products():
    try:
        with open("data/inventory.json","r") as file:
          products=json.load(file)
        return products
    
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
