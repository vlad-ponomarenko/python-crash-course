alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])


alien_0 = {"color": "green", "points": 5}

new_points = alien_0["points"]
print(f"You just earned {new_points} points!")


alien_0 = {"color": "green", "points": 5}
print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)


alien_0 = {}

alien_0["color"] = "green"
alien_0["points"] = 5

print(alien_0)

alien_0 = {"color": "green"}
print(f"The alien is {alien_0['color']}.")

alien_0["color"] = "yellow"
print(f"The alien is now {alien_0['color']}.")


alien_0 = {"color": "green", "points": 5}
print(alien_0)

del alien_0["points"]
print(alien_0)

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}.")


alien_0 = {"color": "green", "speed": "slow"}

point_value = alien_0.get("points", "No point value assigned.")
print(point_value)


point_value = alien_0.get("points")
print(point_value)
