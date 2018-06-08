import random

    print("Welcome to the Jumble game ! ")

    tu = ["chuyenthaibinh","phamvietduc","hatrisy","12ly","tranduyphuong","future","boicodon"]

    tuvatu = tu[random.randint(0, len(tu) - 1)]
    chucai = list(tuvatu)


    random.shuffle(chucai)
    print(chucai, sep=",")
    traloi = input("Your answer :")

    if traloi == tuvatu:
        print("Hura!")
    else :
        print(":)")
