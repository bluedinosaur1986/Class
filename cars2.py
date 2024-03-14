cars=["Buick","Chevy"]
addAcar=""
while addAcar!="Q":
    addAcar=input("Add a car or Q to quit: ")
    if addAcar!="Q":
        cars.append(addAcar)
    for N in cars:
        print(N)
