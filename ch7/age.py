age = input("How old are you?")
# if age >= 18:
# Python can not compare a string, we need change the input to be int by
# using int()
if int(age) <= 18:
    print("Teenager!")
else:
    print("Adult!")
