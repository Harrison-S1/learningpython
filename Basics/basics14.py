#For Loops
colors = [11, 34, 98, 43, 45, 54, 54]
for colors in colors:
    print (colors)

#Print if over 50
colors = [11, 34, 98, 43, 45, 54, 54]
for colors in colors:
    if colors > 50:
        print (colors)

#Print if a int
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
    if isinstance(color, int):
        print (color)

#Print if both above 50 and int
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if isinstance(color, int) and color > 50:
        print(color)