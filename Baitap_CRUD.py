R = ["T-Shirt", "Sweater"]

ask = input("Welcome to our shop, what do you want (C, R, U, D)?")

if ask.lower() == "r" :
    print("Our items :", *R, sep=",")
elif ask.lower() == "c" :
    new = input("Enter new item :")
    R.append(new)
    print("Our items :", *R, sep=",")
elif ask.lower() == "u":
    position = int(input("Update position ?"))
    new = input("New item :")
    R[position - 1] = new
    print("Our items :", *R, sep=",")
elif ask.lower() == "d":
    delete = int(input("Delete position ?"))
    if delete <= 2 :
        del R[delete - 1]
        print("Our items :", *R)
    else :
        print("Nhap lai so di !")
else :
    print("Just using 4 word : C,R,U,D only !")
