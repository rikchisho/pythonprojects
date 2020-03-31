#============================================================
#   Sho Tanaka                   CMP112-E
#   Due Oct. 3, 2019
#   Assign-08                    pgm: Grader
#============================================================

print("- - - - Welcome to Grader - - -")
print()
#---------------- Getting I/P -------------------
name=input("Enter your name: ")

print(name, "please enter your scores")
test1=int(input("\t Enter your test score-1: "))
test2=int(input("\t Enter your test score-2: "))

avg = (test1 + test2)/2

print("Your average is: ", avg)

#---------------- Determining Category ----------
if(avg>=90):
    print("  Your grade is: A")
elif(avg<90):
    print("  Your grade is: B")
elif(avg<80):
    print("  Your grade is: C")
elif(avg<70):
    print("  Your grade is: D")
else:
    print("  Your grade is: F")
        
print("\n keep studying", name, "knowledge is your forever!")
print()
print(". . . . pgm ended succesfully . . .")
    
