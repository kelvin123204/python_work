name_list = ["Sam", "Tom", "Admin", "Mary", "Eli"]
for name in name_list:
    if name.lower() == "admin":
        print("Hello " + name.title() +
              ", would you like to see a status report?")
    else:
        print("Hello " + name.title() + ", thank you for logging in again")
