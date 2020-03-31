#=============== Functions =========================
def chkWindChill(realTemp):
    wind = int (  input("Enter the wind speed: ")  )

    if (wind < 5):
        adjTemp = realTemp
    else:
        windFactor = wind * 0.25
        print( "Wind affects what you feel by negative: ",windFactor  )
        adjTemp = realTemp - windFactor

    return adjTemp

    
def chkOpression(realTemp):
    # uses outside humidity level as the dew point
    humidity= float( input("Enter the humidity (eg. 0.2 is 20%): ") )

    if (humidity < 0.25):
        adjTemp = realTemp

    elif (humidity <= 0.75):
        hFactor = humidity * 10
        print( "Humidity affects what you feel by additonal: " , hFactor )
        adjTemp = realTemp + hFactor

    else:
        hFactor = (humidity * 15) + 2
        print("Humidity affects what you feel by additonal: " , hFactor)
        adjTemp = realTemp + hFactor

    return adjTemp
    
#=========== main program ========================
print(" Is the temperature outside what you really feel?")
print()

actualTemp = float(  input("Enter the temperature: ") )

if ( actualTemp < 35):
    perceivedTemp = chkWindChill(actualTemp)
elif (actualTemp <= 75):
    perceivedTemp = actualTemp    
else:
    perceivedTemp = chkOpression(actualTemp)

print()
print( " - -  Weather Summary - -" )
print( "   Actual  Temperature: ", actualTemp )
print(" Preceived Temperature: ", perceivedTemp )

