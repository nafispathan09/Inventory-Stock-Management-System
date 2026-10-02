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

        name=input("enter name of the product :- ")
        pro_id=int(input("enter product id :-"))
        price=int(input("enter price of the product :-  "))
        quentity=int(input("enter quentity of the product :- "))
        categaty=(input("enter name of categary "))
        supplier=(input("enter name of the supplier :-"))

        product={"Name":name,"Id":pro_id,"Price":price,"Quantity":quentity
                 ,"Categary":categaty,"Supplier":supplier}
        products.append(product)



        agian=input("press ''ENTER fot other entry 'n' for exit  " ).lower()
        if agian =="n":
            break 


def show_product(products):
    print()
    print("welcome to the show product functiion ")
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
    search=int(input("enter product id for search "))
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
    choice=int(input("Enter a prduct id for update a product .. :- "))

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
    print("welcome to the deleate student function ")
    found=False
    choice=int(input("Enter a product id for deleate student "))
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

    choice=int(input("enter a choice ......"))
    if choice==9:
        break 
    elif choice==1 :
        add_product()
    elif choice==2:
        show_product(products)
    elif choice==3:
        search_product(products)










