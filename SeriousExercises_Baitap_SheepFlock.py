flock = [5,7,300,90,24,50,75]
print("Hello my name is Duc, here are sheep sizes:")
print(flock)


print("Now my biggest sheep has size", max(flock), ", let shear it")

flock[flock.index(max(flock))] = 8
print("After shearing here are my flock sizes: ")
print(flock)



for x in range(1,4):
    flock = [i + 50 for i in flock] #cong thuc chua hieu_can tim hieu them
    print("Month", x, ":")
    print("One month has passed, now here is my flock")
    print(flock)
    print("Now my biggest sheep has size", max(flock), ", let shear it")
    flock[flock.index(max(flock))] = 8
    print("After shearing it here are my flock sizes :")
    print(flock)


#tiep theo la phan tinh so tien ban cuu.


flock = [5,7,300,90,24,50,75]
print("Hello my name is Duc, here are sheep sizes:")
print(flock)


print("Now my biggest sheep has size", max(flock), ", let shear it")

flock[flock.index(max(flock))] = 8
print("After shearing here are my flock sizes: ")
print(flock)



for x in range(1,4):


    flock = [i + 50 for i in flock] #cong thuc chua hieu_can tim hieu them
    print("Month", x, ":")
    print("One month has passed, now here is my flock")
    print(flock)
    if x <= 2:

        print("Now my biggest sheep has size", max(flock), ", let shear it")
        flock[flock.index(max(flock))] = 8
        print("After shearing it here are my flock sizes :")
        print(flock)
    else :
        a = 0
        for num in flock:
            a += num

        print("Now my flock has sizes in total:", a)
        print("I would get ", "a * 2 $ =", a * 2, "$")





