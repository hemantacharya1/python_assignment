def main():
    print("Program started:")
    celsiusTofahrenheit(0)
    fahrenheitToKelvin(32)
    kelvinToCelsius(300)


def celsiusTofahrenheit(temp):
    print(str(temp)+"'C","=",round(temp*9/5 +32 ,2),"'F")

def fahrenheitToKelvin(temp):
    print(str(temp)+"'F","=",round((temp-32)*5/9+273.15 ,2),"K")

def kelvinToCelsius(temp):
    print(str(temp)+"K","=",str(round(temp-273.15, 2))+"'C")

if __name__=="__main__":
    main()