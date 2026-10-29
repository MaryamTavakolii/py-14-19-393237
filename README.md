

# py-14-19-393237



#tamrine1


Nomre=float(input("nomre khod ra vared konid:"))

if Nomre>0 or Nomre<20:
    print("adad vared shode eshtebah ast")

if 0>=Nomre>=5:
    print("in dars ra ba paeen tarin nomarat oftadin")

if 5>Nomre>10:
    print("nazdik be ghaboli in dars bodin")

if 10>=Nomre>=15:
    print("ghabol shodin")

if 15<Nomre<=20:
    print("ba bala tarin nomarat ghabol shodin")




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





#tamrine3


Name=str(input("name khod ra vared konid:"))
print(Name*10)







#tamrine4


Hajmebak=float(input("hajmebak khod ra vared konid:"))

Masrafesokht=float(input("mizane masrafesokht bar har 100km khod ra vared konid:"))

Masafat=(Hajmebak**Masrafesokht)*100

print(Masafat)





#tamrine5


Height=float(input("ghad khod ra vared konid:"))

Weight=float(input("vazn khod ra vared konid:"))

BMI=Weight/(Height**2)

if BMI<18.5:
    print("kambode vazn")

elif 18.5<=BMI<25:
    print("vazne monaseb")

elif 25<=BMI<30:
    print("ezafe vazn")





#tamrine6


Temperature=float(input("dama ra vared konid:"))

if Temperature<0:
    print("kapshen beposhid")

elif Temperature<=10:
    print("lebas garm beposhid")

elif Temperature<=25:
    print("hava khobe")

else:
    print("lebas khonak beposhid")
else:
    print("chaghi")










