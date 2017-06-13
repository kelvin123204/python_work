dictionary = {"nile": "ehypt", "amstel": "Netherlands",
              "tigris": "Iraq", "chao phraya": "Thailand", "danube": "hungary"}
for key, value in dictionary.items():
    print("The " + key.title() + " runs through " + value.title())
print("")
print("Rivers :")
for river in dictionary.keys():
    print(river.title())
print("")
print("Country :")
for country in dictionary.values():
    print(country.title())
