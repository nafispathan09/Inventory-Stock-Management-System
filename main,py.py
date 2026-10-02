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





print("---------------------INVENTRY STOCK MANAGEMENT ----------------------")
while True:

    print("enter 1 for add product \\enter 2 for show all products \\3 for search product" \
    "\\4 for EXIT ")

    choice=int(input("enter a choice ......"))
    if choice==4:
        break 
    elif choice==1 :
        add_product()
    elif choice==2:
        show_product(products)
    elif choice==3:
        search_product(products)










