#this program can how to call elements from the list and add new element to the list
a_list = ["Sam","Tom","Mary"]
print(a_list[0].title())
print(a_list[1].upper())
print(a_list[2])
# The instruction below will print Mary
print(a_list[-1])
# The instruction below will print ['Sam', 'Tom', 'Mary']
print(a_list)
print("My friend is "+a_list[0]+"!")
a_list[0]="Sammy"
print(a_list)
print("My friend is "+a_list[0]+"!")
a_list.append("Calvin")
print("'Calvin' has been added to the list")
print(a_list)