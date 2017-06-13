favorite_places = {"Mary": {"place1": "Japan", "place2": "United Kingdom", "place3": "United State"}, "Tim": {"place1": "Hong Kong", "place2": "Singapore", "place3": "Thailand"},
                   "Tom": {"place1": "Hong Kong", "place2": "Thailand", "place3": "United Kingdom"}}
for name, places in favorite_places.items():
    print("Name :" + name)
    print("Favourite places :" +
          places["place1"] + ", " + places["place2"] + ", " + places["place3"])
    print("")
