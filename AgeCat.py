#===============================================
#     this pgm determines a category
#===============================================

print("- - - Age Category - - -")
print()
#---------------- Getting I/P -------------------
age = int( input("Enter Age: "))

#---------------- Determining Category ----------
if(age<2):
    print(age,": infant")
elif(age<13):
    print(age,": child")
elif(age<20):
    print(age,": teenager")
else:
    print(age,": adult")

print("\n --- pgm ended ---")
