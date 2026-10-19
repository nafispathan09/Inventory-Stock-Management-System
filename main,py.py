import inventory,storage,reports

print("---------------------INVENTRY STOCK MANAGEMENT ----------------------")
products=storage.load_products()

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
            break 


        elif choice==1 :
            inventory.add_product(products)
        elif choice==2:
            inventory.show_product(products)
        elif choice==3:
            inventory.search_product(products)
        elif choice==4:
            inventory.update_product(products)
        elif choice==5:
            inventory.delete_product(products)
        else:
            print("invalid choice please enter valid choice again ")


def stock_managent():
    print("Welcomet to the stock management function !!!!!! ")
   
    while True :
        print("1 for add stock \n2 for sale stock\n !!  7 for exit ")
        while True:
            try:
                choice=int(input("enter your choice .......  "))
                break
            except ValueError:
                print("invalid input \ninput must be integer number !!!!! ")
        if choice==7:
            print("thanks for chosing us .. ")
            break



        elif choice==1:
            inventory.add_stock(products)
        elif choice==2:
            inventory.sell_product(products)
       
       
        else:
            print("enter valid input\nyour choice is not valid !!!!! ")


def statistics_report():
    while True:
        print("Enter 1 for inventry statistics \n2for inventry value \n3for low stock report\n4 for exit")
        while True:
            try:
                choice=int(input("Enter your choice here :-  "))
                break
            except ValueError:
                print("Enter valid choice in integer formate !!! ")
        if choice==4:
            print("thanks for visiting !!!! ")
            break
        elif choice==1:
            reports.inventry_statistics(products)
        elif choice==2:
            reports.inventry_vlaue(products)
        elif choice==3:
            reports.low_stock_report(products )
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

    
    
