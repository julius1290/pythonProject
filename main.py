import math
userInput = input("Please give a circle radius:\n")
radius = float(userInput)
area = (radius**2)*math.pi
print(area)

userInput = input("Give a comma seperatet list of numbers:\n")
userInputAsList = userInput.split(', ')
userInputAsTuple = tuple(userInputAsList)
print("List: ", userInputAsList)
print("Tuple: ", userInputAsTuple)

devisibleList = []
for number in range(1500, 2701):
    if not number%7 and not number%5: devisibleList.append(number)
print(devisibleList)

userInput = input("Give a temperatur and a scala Celsius or Fahrenheit, e.g. '20,f' :\n")
temperature = int(userInput.split(',')[0])
if userInput.split(',')[1] == 'f':
    newTemp = (9*temperature + (32 * 5)) / 5
    print('%d°C is %.0f in Fahrenheit' % (temperature, newTemp))
else:
    if userInput.split(',')[1] == 'c':
        newTemp = (5*(temperature - 32)) / 9
        print('%d°F is %.0f in Celsius' % (temperature, newTemp))
    else:
        print("Unkown scala. Please use f for Fahrenheit or c for Celsius.")