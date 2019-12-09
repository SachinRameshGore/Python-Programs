import  Arithmetic

num1 = int(input("Enter First Number :"))
num2 = int(input("Enter Second Number :"))

ans = Arithmetic.Add(num1, num2)
print("Addition is :", ans)

ans = Arithmetic.Sub(num1, num2)
print("Subtraction is :", ans)

ans = Arithmetic.Mult(num1, num2)
print("Multiplicstion is :", ans)

ans = Arithmetic.Div(num1, num2)
print("Division is :", ans)
