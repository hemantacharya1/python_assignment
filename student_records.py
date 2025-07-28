students = [
    (101, "Alice", 85, 20),
    (102, "Bob", 92, 19),
    (103, "Carol", 78, 21),
    (104, "David", 88, 20)
]

def highest_score():
    max_score=0
    name = None
    for s in students:
        if s[2]>max_score:
            max_score=s[2]
            name = s[1]
    print("Highest Scores student is",name,"with marks",max_score)

def name_grade_list():
    list = []
    for s in students:
        student = (s[1],s[2])
        list.append(student)
    print(list)

def update_student():
    for s in students:
        s[2]=88      #error    



highest_score()
name_grade_list()
update_student()

# tuple are meant to be constent as this is an imutable type of data structure 
# tuple uses less memory and are faster then list so in case of immutablity we use tuple