employees = [
("Alice", 50000, "Engineering"),
("Bob", 60000, "Marketing"), 
("Carol", 55000, "Engineering"), 
("David", 45000, "Sales")
]

def sort_by_salary():
    asc_sort_list=sorted(employees,key=lambda x:x[1])
    desc_sort_list=sorted(employees,key=lambda x:x[1],reverse=True)
    print(asc_sort_list)
    print(desc_sort_list)

def sort_by_salary_and_department():
    sorted_list=sorted(employees,key=lambda x:(x[1],x[2]))
    print(sorted_list)

def reverse_list():
    reversed_list=employees[::-1]
    print(reversed_list)

def sort_by_name_length():
    sort_list=sorted(employees,key=lambda x:len(x[0]))
    print(sort_list)

sort_by_salary()
sort_by_salary_and_department()
reverse_list()
sort_by_name_length()

# to change the original list like in place sorting then we use .sort() method 
# and when we need to not modify the original list then we use sorted() method this gives new list