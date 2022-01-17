# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, added_cash):
    added_cash_amount = 10
    pet_shop["admin"]["total_cash"] += added_cash_amount
    return add_or_remove_cash




# def add_or_remove_cash(pet_shop, subtracted_cash):
    subtracted_cash_amount = -10
    pet_shop["admin"]["total_cash"] -= subtracted_cash_amount
    return add_or_remove_cash
    



def get_pets_sold(pet_shop):
     return pet_shop["admin"]["pets_sold"]
        

def increase_pets_sold(pet_shop, add_sold):
    add_sold_pet = 2
    pet_shop["admin"]["pets_sold"] =+ add_sold_pet
    return increase_pets_sold




     
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

   



def get_pets_by_breed(pet_shop, find_breed):
    pet_breed = []
    for pb in pet_shop["pets"]:
        if pb["breed"] == find_breed:
            pet_breed.append(pb)
    return pet_breed
    
    
  

def find_pet_by_name(pet_shop, find_name):
    pet_name_find = None
    for pn in pet_shop["pets"]:
        if pn["name"] == find_name:
            pet_name_find = pn
            
    return pet_name_find


# def remove_pet_by_name(pet_shop, remove_p):
  
    
    
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
    
  
    
def get_customer_cash(customers):     
    return customers["cash"]   


def remove_customer_cash(customer, cash_r_amount):
    remove_cash_customer = 100
    customer["cash"] -= remove_cash_customer
    return remove_customer_cash
    
def get_customer_pet_count(customers):
    return len(customers["pets"])

# def add_pet_to_customer(customer, new_pet):
    return get_customer_pet_count(customer)
    