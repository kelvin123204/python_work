glossry = {"tuble": "immutable list",
           "list": "array of things",
           "pop": "method that extract item from the list",
           "dictionary": "can be used to store key-value pairs",
           "sort": "method that sort the list"}
# key_list = ("tuble", "list", "pop", "dictionary", "sort")
# for key in key_list:
#    print(key.title() + "'s meaning :\n" +
#          str(glossry[key.lower()].capitalize()) + "\n")
# Better version
for key, value in glossry.items():
    print(key.title() + "'s meaning :\n" + value.capitalize() + "\n")
