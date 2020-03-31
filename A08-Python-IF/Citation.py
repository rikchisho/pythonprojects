#============================================================
#   Sho Tanaka                   CMP112-E
#   Due Oct. 3, 2019
#   Assign-08                    pgm: Citation
#============================================================

print("- - - - TRAFFIC STOP: Citations - - -")
#---------------- Getting I/P -------------------
speed=int(input("Enter the excess speed (amount over limit): "))
age=int(input("Enter drivers age: "))

#---------------- Calcs ----------  
print()

if(age>=65):
    print("You were speeding, doing", speed, "over the limit")
    print("I am reminding to say safe and slow down")
else:
    if(speed<8):
        print("Issue a Warning ticket, $35")
    elif(speed<15):
        print("Isuee a Speeding ticket, $75")
    else:
        print("Issue a Reckless ticket, $150")

print(". . . . pgm ended sucessfully ...")
