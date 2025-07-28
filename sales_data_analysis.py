sales_data =[
    ("Q1", [("Jan", 1000),("Feb", 1200),("Mar", 1100)]),
    ("Q2", [("Apr", 1300), ("May", 1250),("Jun", 1400)]),
    ("Q3", [("Jul", 1350), ("Aug", 1450),("Sep", 1300)])
]

def calculate_sales_and_highest_sale_month():
    highest_sale_month=None
    highest_sale=0
    for i in sales_data:
        q,list=i
        total=0
        for j in list:
            month,sale=j
            total+=sale
            if sale>highest_sale:
                highest_sale=sale
                highest_sale_month=month
        print(f'total sale in {q} = {total}')
    print(f'Higest sales month is {highest_sale_month} with {highest_sale} sale')

def flat_list():
    data=[]
    for i in sales_data:
        q,list=i
        for j in list:
            data.append(j)
    print(data)


calculate_sales_and_highest_sale_month()
flat_list()

