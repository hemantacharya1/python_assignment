name,age,city=input("Enter your name:"),input("Enter your age:"),input("Enter your city:")
print(f"My name is {name}, I am {age} years old, and I live in {city}")
print("My name is {fname}, I am {fage} years old, and i live in {fcity}".format(fname=name,fage=age,fcity=city))
print("My name is %s, I am %s years old, and i live in %s" % (name,age,city))