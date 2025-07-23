while(True):
    try:
        age=int(input("Enter your age (1-120):"))
        if(age>=1 and age<=120):
            print("You entered valid age:",age)
            break
        else:
            print("Out of range. Please enter a valid number")
    except:
        print("Invalid input. Please enter valid number")
