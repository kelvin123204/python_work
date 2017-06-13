alien_0 = {"x_position": 0, "y_position": 25, "speed": "fast"}
print("Original x-position :" + str(alien_0["x_position"]))
# Move the alien to right (adding the x coordinate)
# Using speed to determine how far the alien go
if alien_0["speed"] == "slow":
    alien_0["x_position"] = alien_0["x_position"] + 1
elif alien_0["speed"] == "medium":
    alien_0["x_position"] = alien_0["x_position"] + 2
else:
    alien_0["x_position"] = alien_0["x_position"] + 3
print("New x-position :" + str(alien_0["x_position"]))
