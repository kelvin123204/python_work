pets = {"Fox": {"Owner": "Mary", "Kind": "Dog"}, "Finkone": {
    "Owner": "Eli", "Kind": "Dog"}, "Meme": {"Owner": "Kelvin", "Kind": "Cat"}}
for pet_name, pet_info in pets.items():
    print("Pet name :" + pet_name)
    print("Pet's kind :" + pet_info["Kind"])
    print("Pet's owner :" + pet_info["Owner"])
    print("")
