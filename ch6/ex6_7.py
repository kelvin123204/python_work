kelvin = {"first": "kelvin", "last": "kong", "location": "Hong Kong"}
Eli = {"first": "Eli", "last": "Thompson", "location": "US"}
people = [kelvin, Eli]
for person in people:
    print("Person :" + person["first"].title())
    print("Full name :" + person["first"].title() +
          " " + person["last"].title())
    print("location :".title() + person["location"])
    print("")
