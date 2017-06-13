dimensions = (200,10)

#print(dimensions[0])
#print(dimensions[1])

#better way
for dimension in dimensions:
	print(dimension)

#This is not possible
#dimensions[0]=300

#This is possible because it assign a new tuble to be pointed by dimensions object reference
dimensions = (300,200)
print("\nNew dimensions :")
for dimension in dimensions:
	print(dimension)