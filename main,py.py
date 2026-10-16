import json 


def add_product():
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
        save_products(products)



        agian=input("press ''ENTER fot other entry 'n' for exit  " ).lower()
        if agian =="n":
            break 
def show_product(products):
    print()
    print("welcome to the show product functiion ")
    if products.len()==0:
        print("the products in enventry is zero \nno prduct available !!!!!!!!!   ")
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
            if choice>=0:
                print("product id must be positive and non zero !!!")
                continue
            else:
                break 
        except ValueError:
            print("product id must be positive int ")

                

    for product in products :
        if choice==product["Id"]:
            found=True
            con=input("Press 'ENTER' for update "+choice+" Product 'n' for exit ").lower()
            if con=="n":
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
            product["Quentity"]=new_quentity
            product["Supplier"]=new_supplier 
            product["Categary"]-new_categary 
    save_products()

    if found==False:
        print("Student not dound !!!!!!")
def delete_student(products):
    print("welcome to the deleate product function ")
    found=False
    while True:
        try:
            choice=int(input("Enter a product id for deleate student "))
            if choice>=0:
                print("prododuct id cannot be negative nor zero ")
                continue
            else:
                break
        except ValueError:
            print("product id should be positive integere ")

    
    for product in products :
        if choice==product["Id"]:
            found=True
            print("product found ")
            con=input("press 'ENTER' for deleate id no "+choice+"product 'n' for EXIT").lower()
            if con=="n":
                products.remove(product)
                print("successfully deleated product ")
    if found==False:
        print("Student didnt found !!!")
    save_products(products)
def add_stock(products):
    print("welcome to add stock function ")
    while True:
        id=int(input("enter product id for add stock  .... "))
        found=False
        for product in products :
            if product["Id"]==id:
                found=True
                print("product found ")
                print("product name is ",product["Name"])
                new_stock=int(input("enter quentity of new stock "))
                print("current stock = ",product["Quentity"])
                print("added stock = ", new_stock)
                product["Quentity"]+=new_stock
                print("new stock = ",product["Quentity"])
                break
        if found!=True:
            print("invalid id or product not found !!!! ")
        save_products(products)
def sell_product(products):
    print("welcome to the sell prdict function ")
    found=False
    while True:
        try:
            id=int(input("enter product id for sell product : "))
            break 
        except ValueError:
            print("invalid input try again !!!!! ")

    
    for product in products :
        if product["Id"]==id:
            found=True
            print("product found ")
            while True:
                try:
                    sell=int(input("enter number of quentity for sell :  "))
                    break
                except ValueError:
                    print("invalid input \ninput must be in integer formate !!!!!!!! ")

            
            if product["Quentity"]>=sell:
                print("the sell is valid !!! ")
            else:
                print("invalid quentity for sell ")
            product["Quentity"]-=sell
            print("after sell available stock is ",product["Quentity"])

    if found==False:
        print("invalid id or product didnt found !!!!! ")
    save_products(products)


def low_stock_report(products):
    found=False
    print("Welcome to the low stock reprt function ")
    print("low stock product list is >>>  ")
    for  product in products :
        if product["Quentity"]<=5:
            found=True
            print("name:- ",product["Name"],"product_id :- ",product["Id"],"Quentity :- ",product["Quentity"])
    if found!=True:
        print("Empty !!!!!!!! ")
def inventry_statistics(products):
    total_product=0
    total_quentity=0
    for_average=0
    most_expensive=products[0]["Price"]
    chepest=products[0]["Price"]

    for product in products:
        total_product+=1
        total_quentity+=product["Quentity"]
        for_average+=product["Price"]
        if most_expensive<product["Price"]:
            most_expensive=product
        if chepest>product["Price"]:
            chepest=product

    if product==0:
        print("the inventry is clean / empty ")
        return 
        
    print("total number of product is :- ",total_product)
    print("Total number of quentity is :- ",total_quentity)
    print("average cost of a product is :- ",for_average/total_product)
    print("the most expensive product is :-" ,most_expensive)
    print("the chepest product is :- ",chepest)
def inventry_vlaue(products):
    print("welcome to the inventry management system statestics function ")
    if len(products)==0:
        print("the inventry is empty ")
        return 
    grand_total=0

    for product in products:
        total=product["Quentity"]*product["Price"]
        print("product :- ",product["Name"])
        print("Quentity:-",product["Quentity"],"Price :- ",product["Price"])
        print("total of this product is :- ",total )
        print()
        grand_total+=total
    print("The grand total of the whole inventry is :-- ",grand_total)


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

    
print("---------------------INVENTRY STOCK MANAGEMENT ----------------------")
products=load_products()


def product_management(products):
    while True:

        print("enter 1 for add product \nenter 2 for show all products \n3 for search product" \
        "\n4 for update product\n5 for delete student \n9 for EXIT ")
        while True:
            try:
                choice=int(input("enter a choice ......"))
                break
            except ValueError:
                print("Enter choice in int formate \ninvalid choice ")

        if choice==9:
            with open ("inventy.json","w")as file:
                json.dump(products)
            break 


        elif choice==1 :
            add_product()
        elif choice==2:
            show_product(products)
        elif choice==3:
            search_product(products)
        elif choice==4:
            update_product(products)
        elif choice==5:
            delete_student(products)
        else:
            print("invalid choice please enter valid choice again ")
def stock_managent():
    print("Welcomet to the stock management function !!!!!! ")
   
    while True :
        print("1 for add stock \n2 for sale stock\n3 for show low stack report !!  7 for exit ")
        while True:
            try:
                choice=int(input("enter your choice .......  "))
                break
            except ValueError:
                print("invalid input \ninput must be integer number !!!!! ")
        if choice==7:
            print("thanks for chosing us .. ")

            with open ("inventy.json","w")as file:
              json.dump(products)
            break 


        elif choice==1:
            add_stock(products)
        elif choice==2:
            sell_product(products)
        elif choice==3:
            low_stock_report(products )
        else:
            print("enter valid input\nyour choice is not valid !!!!! ")
def statistics_report():
    while True:
        print("Enter 1 for inventry statistics \n2for inventry value \n3 for exit")
        while True:
            try:
                choice=int(input("Enter your choice here :-  "))
                break
            except ValueError:
                print("Enter valid choice in integer formate !!! ")
        if choice==3:
            print("thanks for visiting !!!! ")
            break
        elif choice==1:
            inventry_statistics(products)
        elif choice==2:
            inventry_vlaue(products)
        else:
            print("invalid input try agin !!!! ")
            print()

    
while True:
    while True:

        try:
            choice=int(input("enter a choice ........\n1 for PRODUCT MANAGEMENT \n2 for STOCK MANAGEMENT" \
            "\n3for exit \n4 for statestics report  "))
            break
        except ValueError:
            print("invalid input enter a integer choice !!!!!!! ")
    if choice==3:
        print("thanks for your time .... ")
        break 
    elif choice==1:
        product_management(products)
    elif choice==2:
        stock_managent()
    elif choice==4: 
        statistics_report()

    else:
        print("invalid input please try again !!!!!!!!!!   ")

    
    














