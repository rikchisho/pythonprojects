#===============================================
#     this pgm demos the IF-ELIF-ELSE stmt
#===============================================

print("Display a message, based on temp")
print()

temp = int( input("enter temperature: "))

if( temp < 60 ):
    print( temp, "is chilly")
    print("Wear your coat")
elif(temp < 70):      #60-70
    print( temp, "is a nice day")
    print("Take your sister to playground")
elif(temp < 80):      #70-80
    print("Wear cool clothing")
 
else:                   # all other values
    #print ("All other values")
    print(temp, "is HOT")
    print("Drink plenty of water")

    
    
print("\nHave a nice day")
