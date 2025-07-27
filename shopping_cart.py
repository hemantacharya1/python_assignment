cart=[]

def add_item(str):
    cart.append(str)

def remove_item(str):
    for i,char in enumerate(cart):
        if char==str:
            cart.pop(i)


def remove_last_item():
    if len(cart)>0:
        cart.pop()

def alphabetical_order():
    sort=sorted(cart)
    print('-------------sorted----------------')
    cart_content(sort)
    print('-----------------------------------')

def cart_content(data):
    for i,str in enumerate(data):
        print(f"{i+1}:{str}")


def main():
    add_item("shampoo")
    add_item("harpic")
    add_item("facewash")
    add_item("wax")
    remove_item("wax")
    remove_last_item()
    add_item("laptop")
    add_item("keypad")
    alphabetical_order()
    cart_content(cart)

if __name__=="__main__":
    main()




# output
# -------------sorted----------------
# 1:harpic
# 2:keypad
# 3:laptop
# 4:shampoo
# -----------------------------------
# 1:shampoo
# 2:harpic
# 3:laptop
# 4:keypad