grades = [85, 92, 78, 90, 88, 76, 94, 89, 87, 91]
slice=grades[2:7]
print(slice)
above_85=[i for i in grades if i>85]
print(above_85)
grades[3]=95
print(grades)
grades.extend([96,97,98])
print(grades)
grades.sort(reverse=True)
print(grades)
sorted_5=grades[:5]
print(sorted_5)

