school = {
    "Math": {
        "teacher": "Mr. Smith",
        "students": [("Alice", 85), ("Bob", 92), ("Carol", 78)]
    },
    "Science": {
        "teacher": "Ms. Johnson",
        "students": [("David", 88), ("Eve", 94), ("Frank", 82)]
    }
}

def print_teacher():
    for i in school.values():
        print(i["teacher"])

def average_grade_and_top_student():
    topper=None
    max_marks=0
    for i in school.values():
        total=0
        list = i["students"]
        for j in list:
            total+=j[1]
            if j[1]>max_marks:
                max_marks=j[1]
                topper=j[0]
        print(f'average is {total/len(list)}')
    print(f'school topper is {topper}')
             
         

print_teacher()
average_grade_and_top_student()
