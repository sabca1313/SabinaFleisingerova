dny = ["pondělí", "úterý", "středa", "čtvrtek", "pátek", "sobota", "neděle"]
vstup = input("Zadej číslo, které ti vypíše den v týdnu: ")
print(dny[int(vstup) - 1])


text = input("Zadej jméno: ")
for index in range(len(text) -1, -1, -1):
    print(text[index], end="")

print()

text1 = input("Zadej jméno: ")
print("Text pozpátku:")
for i in range(len(text1) -1, -1, -1):
    print(text1[i], end = "")

print()

platy = input("Zadejte platy: ").split(",")
soucet = 0
for plat in platy:
    soucet +=int(plat.strip())
prumer = soucet/len(platy)
print(f"Průměr platů je {prumer}")


text = input("Zadej text: ")
soucet = 0
for i in range(len(text)):
    znak = ord(text[i])
    if (int(znak) >= 48) and (int(znak) <= 57):
        soucet += znak - 48
print("Součet cifer je: " + str(soucet))



