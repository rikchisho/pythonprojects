#===============================================
#     this pgm demos the IF-ELSE stmt
#===============================================

print("Display a message, based on temp")
print()

temp = int( input("enter temperature: "))

if( temp < 60 ):
    print( temp, "is chilly")
    print("Wear your coat")
else:                   # all other values
    print(temp, "is a nice day")
    print("take your sister to the playground")
print("\nHave a nice day")
