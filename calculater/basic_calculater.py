number_1=float(input("enter first number : "))
op=input("enter oprater : ")
number_2=float(input("enter second number : "))

if op=="+" :
    print(number_1 + number_2)
elif op=="-" :
    print(number_1-number_2)
elif op== "/":
    print(number_1 / number_2)
elif op=="*" :
    print(number_1 * number_2)
else:
    print("invalid orpration")