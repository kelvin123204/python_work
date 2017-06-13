favourite_language = {"Tim": "C", "Sam": "Python",
                      "Mary": "Java", "Eli": "Python"}
print(favourite_language)
# key_list = ["Tim", "Sam", "Mary", "Eli"]
# Better version of the statement above
# key_list = favourite_language.keys()
# But we may not need key_list
# We can just use favourite_language.keys() instead
friends = ("Tim", "Mary")
for key in favourite_language.keys():
    print(key)
    if key in friends:
        print(" Hi " + key.title() + ", I see your favourite language is " +
              favourite_language[key.title()].upper() + "!")
