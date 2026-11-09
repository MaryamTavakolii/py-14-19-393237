



Height=float(input("ghad khod ra vared konid(cm):"))

Weight=float(input("vazn khod ra vared konid(kg):"))

BMI=Weight/(Height**2)

if BMI<18.5:
    print("kambode vazn")

if 18.5<=BMI<25:
    print("vazne monaseb")

if 25<=BMI<30:
    print("ezafe vazn")

if BMI>=30:
    print("chaghi")

