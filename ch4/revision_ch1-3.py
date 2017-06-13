a_list = ["a","A","aAaaA"]
print(a_list[0].upper())
print(a_list[1].lower())
print(a_list[2].title())

del a_list[0]
del a_list[1]
a_list.pop()

a_list.insert(0,'B')
print(a_list)