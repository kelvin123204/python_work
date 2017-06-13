users = {"aeinstein": {"first": "albert", "last": "einstein", "location": "princeton"},
         "mcurie": {"first": "marie", "last": "curie", "location": "paris"}}

for username, userinfo in users.items():
    print("\nusername :".title() + username.title())
    fullname = userinfo["first"] + " " + userinfo["last"]
    location = userinfo["location"]
    print("fullname :".title() + fullname.title())
    print("location :".title() + location.title())
