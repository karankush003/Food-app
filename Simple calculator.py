#for simple calculation

a=int(input("enter the first number: " ))
x=input("enter the opertor like(+,-,*,/,%): ")
b=int(input("enter the second number: "))

if x =='+':
    print(a+b)
elif x == '-':
    print(a-b)
elif x =='*':
    print(a*b)
elif x == '/':
    print(a/b)
elif x == '%':
    print(a%b)

else:
    print("Invaild Opertors")    

            
