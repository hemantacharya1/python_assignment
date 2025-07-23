list=[]
for i in range(1,4):
    price = int(input("Enter price for item "+str(i)+":"))
    quantity = int(input("Enter quantity of item "+str(i)+":"))
    list.append((i,price,quantity))
subtotal=0
print("------------------------------------------------------------------")
for i,price,quantity in list:
    total = price*quantity
    print("Item",str(i)+":",str(price),"x",str(quantity),"=",total)
    subtotal+=total
    
print("Subtotal:",subtotal)
tax = round((subtotal*8.5)/100,2)
subtotal+=tax
print("Tax (8.5%):",tax)
print("Total:",subtotal)