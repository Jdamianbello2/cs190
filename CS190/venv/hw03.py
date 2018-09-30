first = float(input("Enter a number. "))
math_operator = input("Enter a mathematical operation (+,-,*,/,//,**,^, or %). ")
sec = float(input("enter a second number "))

if math_operator == "+":
    print(float(first) , "+" , float(sec) , "=" , first + sec)
elif math_operator == "-":
    print(float(first) , "-" , float(sec) , "=" , first - sec)
elif math_operator == "*":
    print(float(first) , "*" , float(sec) , "=" , first * sec)
elif math_operator == "/":
    print(float(first) , "/" , float(sec) , "=" , first / sec)
elif math_operator == "//":
    print(float(first) , "//" , float(sec) , "=" , first // sec)
elif math_operator == "^":
    print(float(first) , "^" , float(sec) , "=" , first ^ sec)
elif math_operator == "**":
    print(float(first) , "**" , float(sec) , "=" , first ** sec)
elif math_operator == "%":
    print(float(first) , "%" , float(sec) , "=" , first % sec)
else:
    print("Invalid operator")