Months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
Days=[31,28,31,30,31,30,31,31,30,31,30,31]
userMonth=input("Gimme a month:")
i=0
while i<=11:
    if userMonth==Months[i]:
        print(Months[i], "has",Days[i],"days.")
    i=i+1
