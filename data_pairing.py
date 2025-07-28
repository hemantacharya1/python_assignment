products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [999.99, 25.50, 75.00, 299.99]
quantities = [5, 20, 15, 8]

def zip_function():
    zip={}
    for i,product in enumerate(products):
        zip[product]=prices[i]
    return zip

def calculate_total_value():
    zip={}
    for i,product in enumerate(products):
        zip[product]=prices[i]*quantities[i]
    return zip

def build_category():
    zip = {}
    for i,product in enumerate(products):
        zip[product]={"price":prices[i],"quantity":quantities[i]}
    return zip

print(zip_function())
print(calculate_total_value())
print(build_category())