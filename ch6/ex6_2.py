favourite_numbers = {"Eli": 1, "Sam": 3, "Mary": 5, "Avon": 7, "Timmy": 9}
# Use tuble to prevent user editing the value inside
# key_list = ("Eli", "Sam", "Mary", "avon", "timmy")
# for key in key_list:
#    print(key.title() + "'s favourite number is :" +
#          str(favourite_numbers[key.title()]))
# Better version
for key, value in favourite_numbers.items():
    print(key.title() + "'s favourite number is :" + str(value))
