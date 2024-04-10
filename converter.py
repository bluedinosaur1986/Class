def Main():
    distance="null"
    print("1. Convert inches to centimeters")
    print("2. Convert feet to meters")
    print("3. Convert miles to kilometers")
    print("4. End program")
    print()
    selection=input("Enter your selection: ")
    if selection=="4":
        exit(1)
    while not distance.isnumeric():
        distance=input("Input distance to convert: ")
    distance=float(distance)
    if selection=="1":
        Inches(distance)
    elif selection=="2":
        Feet(distance)
    elif selection=="3":
        Miles(distance)
    else:
        print ("Invalid selection, please try again:")
        Main()
def Inches(distance):
    print("The distance in centimeters is:",distance*2.54)
def Feet(distance):
    print("The distance in meters is:",distance*0.3048)
def Miles(distance):
    print("The distance in kilometers is:",distance*1.609)
Main()