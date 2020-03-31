#===============================================
#     this pgm determines a Ridead
#===============================================

print("- - - Fair Rides - - -")
print()
#---------------- Getting I/P -------------------
age=int(input("Enter Age       : "))
ht=int(input("Enter your height: "))

#---------------- Determining Category ----------
if(age>=13):
    print("Enjoy the Ride!")
else:            # Age under 14, Check Height
    if(ht<30):
        print("Sorry, You may not go on this ride")
    elif(ht<48):
        print("FInd an adult to join you on the ride")
    else:
        print("Hang on tightly and have fun")

print("Have fun at the Park")
    
