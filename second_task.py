a = 0.5
b = 0.7
h = 0.05
k = 1
tolerance = 0.001
series_sum = 0

x = a

while x <= (b + 1e-8):

    while True:
        value = (x + 2) / (k * (k + 2))
        if abs(value) <= tolerance:
            break
        series_sum += value
        k += 1

    print(f"x = {x:.2f}, сума ряду = {series_sum:.6f}")
    x += h
