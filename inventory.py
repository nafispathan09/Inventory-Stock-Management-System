# inventry 

# overall bug free >>>> 

import storage as file
products=file.load_products()

def add_product(products):
    print("welcome to add product function ")
    print()
    while True:
        product={}
        while True:
            name=input("enter name of the product :- ")
            if name.strip()=="":
                print("name cant be empty !!!! ")
                continue 
            else:
                break 

        while True:
                found=False
                try :
                    
                     pro_id=int(input("enter product id :-"))
                     for product in products:
                         if product["Id"]==pro_id:
                             found=True
                             print("this product id already exist try another one !!! ")
                             break
                     if found:
                         continue
                     if pro_id>0:
                         break
                     else:
                         print("product id cannot be nagative !! ")
                except ValueError:
                    print("Enter product id  in int format ")

        while True:
            try:
                price=int(input("enter price of the product :-  "))
                if price>=0:
                    break
                else :
                    print("price must be positive or 0 not nagative ")
                    continue 
            except ValueError:
                print("price must be in int formate !!!! ")

        while True:
            try:
                quentity=int(input("enter quentity of the product :- "))
                if quentity>=0:
                     break 
                else:
                    print("Quentity cannot be nagative !!!!! ")

                 
            except ValueError:
                print("enter input in int formate ")


        while True:
            categary=(input("enter name of categary "))
            if categary.strip()=="":
                print("categary cannot be empty !!!! ")
                continue
            else:
                break 

        while True:
            supplier=(input("enter name of the supplier :-"))
            if supplier.strip()=="":
                print("supplier can be empty !!!!")
                continue 
            else :
                break 
            

        product={"Name":name,"Id":pro_id,"Price":price,"Quantity":quentity
                 ,"Categary":categary,"Supplier":supplier}
        products.append(product)
        file.save_products(products)



        agian=input("press ''ENTER fot other entry 'n' for exit  " ).lower()
        if agian =="n":
            break 
def show_product(products):
    print()
    print("welcome to the show product functiion ")
    if len(products)==0:
        print("the products in enventry is zero \nno prduct available !!!!!!!!!   ")
        return
    for product in products:
        print("name",product["Name"])
        print("product id",product["Id"])
        print("price",product["Price"])
        print("quantity",product["Quantity"])
        print("categary ",product["Categary"])
        print("supplier",product["Supplier"])
def search_product(products):
    print("welcome to the product search function ")
    found=False
    while True:
        try:
            search=int(input("enter product id for search "))
            if search>0:
                break
            else:
                print(" product id must be posotive and non zero ")
                continue 
        except ValueError:
            print("product id must be int and positive ")

    
    for product in products:
        if search==product["Id"]:
            found=True
            print("name",product["Name"])
            print("product id",product["Id"])
            print("price",product["Price"])
            print("quentity",product["Quantity"])
            print("categary ",product["Categary"])
            print("supplier",product["Supplier"])
    if found==False:
        print("product not found !!!!!")
def update_product(products):
    print("Welcome to the update product function ")
    found=False 
    while True:
        try:
            choice=int(input("Enter a prduct id for update a product .. :- "))
            if choice<=0:
                print("product id must be positive and non zero !!!")
                continue
            else:
                break 
        except ValueError:
            print("product id must be positive int ")

                

    for product in products :
        if choice==product["Id"]:
            str_choice=str(choice)
            found=True
            confirm=input("Press 'ENTER' for update "+str_choice+" Product 'n' for exit ").lower()
            if confirm=="n":
                return 
            new_name=input("Enter new name         :-")
            new_id=int(input("enter new product id     :- "))
            new_price=int(input("enter new price       :- "))
            new_quentity=int(input("enter new quentity :- "))
            new_categary=input("enter new categary :- ")
            new_supplier=input("enter new supplier :- ")

            product["Name"]=new_name
            product["Id"]=new_id
            product["Price"]=new_price
            product["Quantity"]=new_quentity
            product["Supplier"]=new_supplier 
            product["Categary"]=new_categary 
    file.save_products(products)

    if found==False:
        print("Student not dound !!!!!!")
def delete_product(products):
    print("welcome to the deleate product function ")
    found=False
    while True:
        try:
            choice=int(input("Enter a product id for deleate student "))
            if choice<=0:
                print("prododuct id cannot be negative nor zero ")
                continue
            else:
                break
        except ValueError:
            print("product id should be positive integere ")

    
    for product in products :
        if choice==product["Id"]:
            str_choice=str(choice)
            found=True
            print("product found ")
            con=input("press 'ENTER' for deleate id no "+str_choice+"product 'n' for EXIT").lower()
            if con!="n":
                products.remove(product)
                print("successfully deleated product ")
                file.save_products(products)

            else:
                return 
    if found==False:
        print("Student didnt found !!!")
    








def add_stock(products):
    print("welcome to add stock function ")
    while True:
        while True:
            try:
                id=int(input("enter product id for add stock  .... "))
                if id<=0:
                    print("id cant be nagative nor zero try agian !!!  ")
                    pass
                else:
                    break
            except ValueError:
                print("only excepts positive integer values   ")
    
        found=False
        for product in products :
            if product["Id"]==id:
                found=True
                print("product found ")
                print("product name is ",product["Name"])

                while True:
                    try:
                        new_stock=int(input("enter quantity of new stock "))
                        if new_stock<=0:
                            print("the quantity must be positive ")
                           
                        else:
                            break
                    except ValueError:
                        print("enter positive integer number ")

                print("current stock = ",product["Quantity"])
                print("added stock = ", new_stock)
                product["Quantity"]+=new_stock
                print("new stock = ",product["Quantity"])
                break
        if found!=True:
            print("invalid id or product not found !!!! ")
           
        file.save_products(products)
        return



def sell_product(products):
    print("welcome to the sell prdict function ")
    found=False
    while True:
        try:
            id=int(input("enter product id for sell product : "))
            if id<=0:
                print("the Id cant be nagetive nor zero !!!!! ")
                pass
            else:
                break 
        except ValueError:
            print("invalid input try again !!!!! ")

    for product in products :
        if product["Id"]==id:
            found=True
            print("product found ")
            while True:
                try:
                    sell=int(input("enter number of quantity for sell :  "))
                    if sell<=0:
                        print("sell cant be nagative nor zero !!!!! ")
                        pass
                    else:
                        break
                    
                except ValueError:
                    print("invalid input \ninput must be in integer formate !!!!!!!! ")

            
            if product["Quantity"]>=sell:
                print("the sell is valid !!! ")
                product["Quantity"]-=sell
                file.save_products(products)

            else:
                print("invalid quantity for sell ")
            print("after sell available stock is ",product["Quantity"])

    if found==False:
        print("invalid id or product didnt found !!!!! ")

