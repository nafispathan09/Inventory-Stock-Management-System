products=[]
sample_dict1={"PRODUCT ID ":123,"PRICE ":789,"SUPPLIER":"","NAME":"",
             "QUENTITY":13,"CATEGARY":"",}
sample_dict2={"PRODUCT ID ":13,"PRICE ":9,"SUPPLIER":"","NAME":"",
             "QUENTITY":143,"CATEGARY":"",}
sample_dict3={"PRODUCT ID ":124,"PRICE ":79,"SUPPLIER":"","NAME":"",
             "QUENTITY":153,"CATEGARY":"",}




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
                









print("---------------------INVENTRY STOCK MANAGEMENT ----------------------")
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









