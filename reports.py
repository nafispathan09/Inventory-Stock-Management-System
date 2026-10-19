# stock reports 
# almost done & bug free




def low_stock_report(products):
    found=False
    print("Welcome to the low stock reprt function ")
    print("low stock product list is >>>  ")
    for  product in products :
        if product["Quantity"]<=5:
            found=True
            print("name:- ",product["Name"],"product_id :- ",product["Id"],"Quantity :- ",product["Quantity"])
    if found!=True:
        print("Empty !!!!!!!! ")





def inventry_statistics(products):
    if len(products)==0:
        print("the inventry is empty !!! ")
        return
    total_product=0
    total_quentity=0
    for_average=0
    most_expensive=products[0]["Price"]
    chepest=products[0]["Price"]

    for product in products:
        total_product+=1
        total_quentity+=product["Quantity"]
        for_average+=product["Price"]
        if most_expensive<product["Price"]:
            most_expensive=product["Price"]
        if chepest>product["Price"]:
            chepest=product["Price"]


        
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
        total=product["Quantity"]*product["Price"]
        print("product :- ",product["Name"])
        print("Quentity:-",product["Quantity"],"Price :- ",product["Price"])
        print("total of this product is :- ",total )
        print()
        grand_total+=total
    print("The grand total of the whole inventry is :-- ",grand_total)
