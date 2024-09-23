import math

# def cotangent(x):
#     return 1 / math.tan(x)

a = 0.6
b = 0.9
h = 0.02
x = a

while x <= b:
    if x < 0.6:
        result = math.cos(math.sqrt(x))
    elif 0.6 <= x < 0.7:
        result = 1/math.tan(x**2)
    else:
        result = math.atan(x ** 3)

    print(f"x = {x:.2f}, f(x) = {result:.6f}")
    x += h
