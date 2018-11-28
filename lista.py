meny = 0

print("***Välkommen till programet***\n")
print("1. Skriv ut")
print("2. Mata in")
print("3. Resna")
print("4. Avsluta")

while meny != 4:

    try:
        meny = int(input("Gör ett val: "))
    except:
        print("Du måste gör ett korekt val")
    
    if meny == 1:
        print("1")
    elif meny == 2:
        print("2")
    elif meny == 3:
        print("3")
    else:
        print("hej då")