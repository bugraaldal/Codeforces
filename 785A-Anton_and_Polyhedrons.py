sumSurface = 0
dices = {"Icosahedron": 20, "Dodecahedron": 12,
         "Octahedron": 8, "Cube": 6, "Tetrahedron": 4}
count_dices = int(input())
for _ in range(count_dices):
    dice = input()
    if dice in dices:
        sumSurface += dices[dice]
print(sumSurface)
