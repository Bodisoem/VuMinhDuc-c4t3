mass = float(input("Nhap can nang:"))
height = float(input("Nhap chieu cao:"))

h = height/100

bmi = mass/(h**2)

if bmi < 16:
   print("Severely underweight")
elif bmi < 18.5 and bmi > 16:
   print("Underweight")
elif bmi < 25 and bmi > 18.5:
   print("Normal")
elif bmi < 30 and bmi > 25:
   print("Overweight")
else :
   print("Obese")

