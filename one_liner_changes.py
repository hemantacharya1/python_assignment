import math

# squre of odd numbers
list1=[i*i for i in range(1,21) if i%2!=0]
print(list1)

#lower the string in list
list2=list(map(str.lower,["THIS AND THAT","RAG AND ALL","TAgaya And Team"]))
print(list2)

#sum of a list
total = sum([1,2,3,4,5])
print(total)

#factorial a number
fact=math.factorial(5)
print(fact)

#count the vowel in a string
str="Misogi Ai"
vowelCount=sum(1 for c in str if c.lower() in "aeiou")
print(vowelCount)
