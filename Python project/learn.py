num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
action = str(input("Choose action: Add(a), Sub(s), Mult(m), Modul(mo) Div(d)-> "))

print("The result is ",end="")
if action == "a":
    print(num1+num2)
elif action == "s":
    print(num1-num2)
elif action == "m":
    print(num1*num2)
elif action == "mo":
    print(num1*num2)
else:
    print(num1/num2)
  
