"""
for j in range(8):
    if j % 2 == 0:
        for i in range(8):
            if i % 2 == 0:
                print(" ", end="")
            else:
                print("#", end="")
    else:
        for i in range(8):
            if i % 2 == 1:
                print(" ", end="")
            else:
                print("#", end="")
    print()
"""

for j in range(8):
    for i in range(8):
        if (i + j) % 2 == 0:
            print(" ", end="")
        else:
            print("#", end="")
    print()

