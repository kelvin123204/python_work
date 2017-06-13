#this can show you how "sorted()" , list."sort()" and 

brands = ["Razer","Corsair","Logitech","Steelseries"]
print("The list contains :"+ str(brands) + "\n")
print("The sorted version will be like :"+ str(sorted(brands)))
print("")
print("But the list has not been sorted :"+ str(brands))
brands.sort()
print("")
print("Now the list is sorted :" + str(brands))
print("")
brands.reverse()
print("The reverse version be like :" + str(brands))
