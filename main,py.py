

print("---------------------INVENTRY STOCK MANAGEMENT ----------------------")
products=load_products()

# main menu 
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

    
    














