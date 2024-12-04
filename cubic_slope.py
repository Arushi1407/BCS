#cubic=ax3+bx2+cx+d

a = float(input("Coefficient of cubic term (a): "))
b = float(input("Coefficient of quadratic term (b): "))
c = float(input("Coefficient of linear term (c): "))
d = float(input("Constant term (d): "))
x = float(input("Value of x: "))

print(f"cubic is {a}x^3+{b}x^2+{c}x+{d}")
slope=(3*a*x*x)+(2*b*x)+c
print(f"slope is{slope}")
