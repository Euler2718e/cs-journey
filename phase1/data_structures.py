'''
# Lists

scores = [67, 69, 420]

print(scores[0])        # First item in list scores (indexing starts at 0)
print(scores[-1])       # Last item
print(scores[1:3])      # Items at index 1 and 2 (1-3, ergo 1 and 2)
print(len(scores))      # How many items
scores.append(55)       # Adds 55 to the end of list
scores.sort()           # Sorts in place
print(max(scores))      # Highest value
print(min(scores))      # Lowest value
'''
'''
# Dictionaries

player = {"name": "Jakob", "score ": 0, "lives": 3}

print(player["name"])   # Gets a value from a key (value assigned in the dic)
player["score"] = 10    # Updates a value of an existing key
player["level"] = 1     # Adds new key and value
print("name" in player) # Checks if key exists in dic
print(player.keys())    # Prints all keys
print(player.values())  # Prints all values
'''
# Nested dictionary
'''
# Game has a player with keys name and score, and it has the level
game = {"player1": {"name": "Jakob", "score": 0}, "level": 1}

print(game["player1"]["name"]) # Here it is evident that you need to write the overriding key first, and then the nested key you want to access from the overriding key
'''

# A list of dictionaries

students = [
    {"name": "Jakob", "grade": 69},
    {"name": "Jakhobyr", "grade": 420},
    {"name": "J", "grade": 67},
    {"name": "A", "grade": 7},
    {"name": "K", "grade": 6},
    {"name": "O", "grade": 670},
    {"name": "B", "grade": 27},
    {"name": "Bokaj", "grade": 127},
]


# Claude's one:

best = {"name": "", "grade": 0}

for student in students:
    if student["grade"] > best["grade"]:
        best = student

print(
    f"The student with the highest grade is: {best['name']} with a grade of {best['grade']}")


# My one:

Num = -1
Latest = 0
Times = len(students)

for a in range(Times):
    Num += 1
    data = students[Num]
    i = data["grade"]

    if i > Latest:
        Latest = i
        name = data["name"]

print(
    f"The student with the highest grade is: {name} with a grade of {Latest}")
