favourite_name = {"James": {"number1": 1, "number2": 3, "number3": 6}, "Mary": {
    "number1": 2, "number2": 10, "number3": 99}, "Eli": {"number1": 69, "number2": 96}}
for name, numbers in favourite_name.items():
    print("Name :" + name)
    # print("F. Numbers :" + str(numbers["number1"]) + " " +
    #      str(numbers["number2"]) + " " + str(numbers["number3"]))
    print("F. Numbers :")
    i = 1
    key = "number" + str(i)
    while numbers.has_key(key):
        print(str(numbers[key]))
        i = i + 1
        key = "number" + str(i)
    i = 1
    key = "number" + str(i)
    print("")
