inventory = {}

def add_product(str,data):
    inventory[str]=data

def update_product(product,rate):
    item=inventory[product]
    item["price"]=rate

def sell_item(product,quantity):
    item=inventory[product]
    item["quantity"]=item["quantity"]-quantity

def calculate_inventory_value():
    total = 0
    for details in inventory.values():
        total += details["price"]*details["quantity"]    
    print("Total value of inventory",total)

def print_low_stock():
    for product,details in inventory.items():
        if details["quantity"]<100:
            print("Low stock product",product,details["quantity"])


def main():
    add_product("apples",{"price":1.50,"quantity":100})
    add_product("bananas",{"price":0.75,"quantity":150})
    add_product("oranges",{"price":2.00,"quantity":80})
    print(inventory)
    update_product("bananas",25)
    print(inventory)
    sell_item("apples",25)
    print(inventory)
    calculate_inventory_value()
    print_low_stock()


if __name__ == "__main__":
    main()