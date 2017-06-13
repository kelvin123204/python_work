string1 = "Bmw"
string2 = "Audi"
string3 = "bmw"
number1 = 32
number2 = 30
number3 = -2
number4 = 432
numList = [32, 30, -2, 432]
if string1 == string2:
    print("'" + string1 + "' == '" + string2 + "'")
else:
    print("'" + string1 + "' != '" + string2 + "'")

if string1.lower() == string3.lower():
    print("'" + string1.lower() + "' == '" + string3.lower() + "'")
else:
    print("'" + string1.lower() + "' != '" + string3.lower() + "'")

print("\nNumber checking")
print("\nNumbers are")
x = 0
for number in numList:
    print("Number" + str(x) + "\t:" + str(number))
    x = x + 1
print("")

if number1 > number2:
    print(str(number1) + " > " + str(number2))
else:
    print(str(number1) + " is not larger than " + str(number2))

if number4 < number1:
    print(str(number4) + " < " + str(number1))
else:
    print(str(number4) + " is not smaller than " + str(number1))

if number2 >= number3:
    print(str(number2) + " >= " + str(number3))
else:
    print(str(number2) + " is not larger or equal to " + str(number3))

if number4 <= number1:
    print(str(number4) + " <= " + str(number1))
else:
    print(str(number4) + " is not smaller or equal to " + str(number1))

if number1 >= number2 and number3 >= number4:
    print(str(number1) + " >= " + str(number2) +
          " and " + str(number3) + " >= " + str(number4))
else:
    print("!(" + str(number1) + " >= " + str(number2) +
          " and " + str(number3) + " >= " + str(number4) + ")")

if number1 >= number2 or number3 >= number4:
    print(str(number1) + " >= " + str(number2) +
          " or " + str(number3) + " >= " + str(number4))
else:
    print("!(" + str(number1) + " >= " + str(number2) +
          " or " + str(number3) + " >= " + str(number4) + ")")

if -2 in numList:
    print(str(-2) + " is in the list")
else:
    print(str(-2) + " is not in the list")

if 33 in numList:
    print(str(33) + " is in the list")
else:
    print(str(33) + " is not in the list")
