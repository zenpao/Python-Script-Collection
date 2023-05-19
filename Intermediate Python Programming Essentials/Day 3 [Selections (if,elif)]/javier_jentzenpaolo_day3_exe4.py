purchaseQty = int(input("Enter Quantity of packages: "))

retailPrice = 99 #packageprice

cost = retailPrice * purchaseQty

if purchaseQty >= 0 and purchaseQty <= 9:
    finalCost = cost
    display = f"""\n
    Discount: 0%
    Cost: {finalCost}
    finalCost: {finalCost} 
    """
    print(display)
elif purchaseQty >= 10 and purchaseQty <= 19:
    finalCost = cost - (cost*0.1)
    display = f"""\n
    Discount: 10%
    Cost: {cost}
    finalCost: {finalCost} 
    """
    print(display)
elif purchaseQty >= 20 and purchaseQty <= 49:
    finalCost = cost - (cost*0.2)
    display = f"""\n
    Discount: 20%
    Cost: {cost}
    finalCost: {finalCost} 
    """
    print(display)
elif purchaseQty >= 50 and purchaseQty <= 99:
    finalCost = cost - (cost*0.3)
    display = f"""\n
    Discount: 30%
    Cost: {cost}
    finalCost: {finalCost} 
    """
    print(display)


#cost = retailPrice*quantity

#final cost = cost - (cost*percent)
