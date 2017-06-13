#this can show you how to add elements to the list/drop elements from the list

a_list = []
target = "haHAA"
a_list.append(target)		#1
print(target + " has been added to the list.\n")
print(a_list)
target = "PogChamp"
a_list.append(target)	#2
print(target + " has been added to the list.\n")
print(a_list)
target = "Kappa"
a_list.append(target)		#3
print(target + " has been added to the list.\n")
print(a_list)
a_list.append(1)			#4
print(str(1) + " has been added to the list.\n")
print(a_list)
a_list.append(0.1232)		#5
print(str(0.1232) + " has been added to the list.\n")
print(a_list)
target = "Keepo"
a_list.insert(0,target)		#0
print(target + " has been added to the list.\n")
print(a_list)
target="LUL"
a_list.insert(6,target)		#6
print(target + " has been added to the list.\n")
print(a_list)
#delete element from list
del a_list[5]
print(str(0.1232) + " has been deleted to the list.\n")
print(a_list)
a_list.pop(4)
print(str(1) + " has been deleted to the list.\n")
print(a_list)
a_list.pop()
print("LUL" + " has been deleted to the list.\n")
print(a_list)
target = "Keepo"
a_list.remove(target)
print(target + " has been deleted to the list.\n")
print(a_list)
target = "haHAA"
a_list.remove(target)
print(target + " has been deleted to the list.\n")
print(a_list)