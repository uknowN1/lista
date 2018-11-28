bilar = []

while True:

    menu = input("Val: ")

    if menu == "1":
        for l in bilar:
            print(l)
    elif menu == "2":
        bilen = {}
        bilen["brand"] = input("Brand: ")
        bilen["model"] = input("Model: ")
        bilen["year"] = input("Year: ")

        bilar.append(bilen)

    else:
        break