def windchill_calculation ():
    for x in range (0, 60, 5 ):
        x += 5  
        if temp == "C":
            new_temp = (temperature *9/5) + 32
            Wind_Chill = 35.74 + (0.6215*new_temp) - 35.75*(x**0.16) + (0.4275*new_temp *(x**0.16))
            print (f"At temperature {new_temp}F, wind speed at {x}MPH. The windchill is: {Wind_Chill:.2f}F")
        elif temp == "F":
            Wind_Chill = 35.74 + (0.6215*temperature) - (35.75* (x**0.16)) + (0.4275*temperature*(x**0.16))
            print (f"At temperature {temperature}F, and wind speed at {x}MPH. The windchill is: {Wind_Chill:.2f}F. ")
    

    
temperature = float(input("What is the temperature? "))
temp= input ("Fahrenheit or Celsius (F/C)? " ).upper()
print()
windchill_calculation()