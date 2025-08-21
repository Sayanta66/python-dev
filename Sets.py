players = {"Messi", "Ronaldo", "Neymar", "Aguero"}
print(players)
print(type(players))
print(len(players))

teams = {"Barcelona", "Real Madrid", "Manchester", "Manchester", "Chelsea"}
print(teams)

teams2 = set()
teams2.add(1)
teams2.add("Python is great")
print(teams2)
teams2.remove("Python is great")
print(teams2)
teams2.add((1,2,3,4))
print(teams2)

set_new={1, 2, 5, 5, 9, 2, "Good", "Nice"}
print(set_new)
set1 = set_new.clear()
print(set1)