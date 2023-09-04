import random

User = -1
PC = -1

UserPoint = 0
PCPoint = 0

print("game start")
print("x = paper")
print("y = rock")
print("z = scissors")
print("input only x,y,or z")
for round in range(10):
  weapon = ['x', 'y', 'z']
  PC_weapon = weapon[random.randint(0, 2)]
  User_weapon = input('Choose your weapon : ')

  winner = 1
  loser = 0

  if User_weapon == PC_weapon:
    UserPoint = UserPoint + 1
    PCPoint = PCPoint + 1
    print("Tie ")
  elif User_weapon == 'x' and PC_weapon == 'y':
    User = winner
    PC = loser
  elif User_weapon == 'y' and PC_weapon == 'z':
    User = winner
    PC = loser
  elif User_weapon == 'z' and PC_weapon == 'x':
    User = winner
    PC = loser
  else:
    PC = winner
    User = loser

  if User == winner:
    UserPoint = UserPoint + 1
    print("User wins this round")
  else:
    PCPoint = PCPoint + 1
    print("PC wins this round")
  print(f"UserPoint: {UserPoint}, PCPoint: {PCPoint}")
if PCPoint > UserPoint:
  print("PC wins this game")
else:
  print("User wins this game")
