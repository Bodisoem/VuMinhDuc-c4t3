num = int(input("Nhap so muon tinh :"))

factorial = 1

if num < 0:
    print(" Nhap the deo ai tinh duoc")
elif num == 0 :
    print(" Factorial = 0 !")
else:
    for i in range (1, num + 1):
        factorial = factorial * i
    print(" Factorial = ", factorial, "!")