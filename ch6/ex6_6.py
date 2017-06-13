favourite_language = {"Tim": "C", "Sam": "Python",
                      "Mary": "Java", "Eli": "Python"}
targets = ("Sam", "Tim", "parker", "john",
           "timmy", "paul", "james", "Mary", "Eli")
for target in targets:
    if target in favourite_language.keys():
        print("Thank you " + target.title() +
              " for taking part in the poll!\n")
    else:
        print(target.title() + ", you should take pary in the poll!\n")
