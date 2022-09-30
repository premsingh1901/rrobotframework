player = ["Sachin", "Sehwag", "Dhoni", "Pant", "Kohli", "Pant"]
score = [10, 8, 8, 7, 2]

print("Player: ", player)
print("Score: ", score)

l = len(player)
print(l)
print(len(score))

player.append("Surya")
print("Player: ", player)

print(type(player))

player.insert(0, "Bradman")
print("Player: ", player)

player.extend(score)
print("Player: ", player)

player1 = ["Harmanpreet", "vaisali"]
player_all = player + player1
print(player_all)
print(player.index("Pant"))
player_all.remove("Surya")
print(player_all)
print(score)
score.sort(reverse=True)
print(score)

score.reverse()
print(score)

score.pop()
print(score)

score.pop(1)
print(score)

print(score.count(8))
set1 = set(score)
print(list(set1))

score.clear()
print(score)

score1 = [12, 13, 1, 4, 10, 3, 4, 5]
score2 = score1.copy()
print(score2)
score2.append(50)
print(score2)
print(score1)

score3 = score1
print(score3)
score1.append(100)
print(score1)
print(score3)
# del score1
print("Deleted", score1)

m = max(score1)
print(m)

mn = min(score1)
print(mn)

print(sorted(score1))
print(sum(score1))



