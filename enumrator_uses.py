students = ["Alice", "Bob", "Carol", "David", "Eve"]
scores = [85, 92, 78, 88, 95]

def numbered_list():
    for i,s in enumerate(students):
        print(i+1,s)

def pair_with_marks():
    for i,s in enumerate(students):
        print(s,scores[i])

def print_high_score_position():
    for i,s in enumerate(students):
        if scores[i]>90:
            print(i)

def creat_dict():
    dictionary={}
    for i,s in enumerate(students):
        dictionary[students[i]]=scores[i]
    print(dictionary)

numbered_list()
pair_with_marks()
print_high_score_position()
creat_dict()