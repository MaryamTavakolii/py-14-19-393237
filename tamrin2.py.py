#tamrine2

Salary=float(input("Hoghoghe khodra vared konid:"))


if Salary>100:
    Tax=Salary*0.35

elif 80<=Salary<=100:
    Tax=Salary*0.25

elif 70<=Salary<80:
    Tax=Salary*0.15

elif 60<=Salary<70:
    Tax=Salary*0.12

elif 50<=Salary<60: 
    Tax=Salary*0.10

elif 40<=Salary<50:
    Tax=Salary*0.5

else:
   Tax=0

print(Salary-Tax)
