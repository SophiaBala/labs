def compute_simplified_series(x, d=0.001):
    k = 1  # Початковий індекс
    series_sum = 0  # Початкова сума ряду

    # Обчислюємо ряд, доки поточний член ряду більше за похибку
    while True:
        term = (x + 2) / (k * (k + 2))  # Обчислення k-го члена ряду
        if abs(term) < d:  # Перевірка, чи задовольняє похибка
            break
        series_sum += term  # Додаємо член до суми
        k += 1  # Переходимо до наступного члена ряду

    return series_sum


x_values = [0.5 + i * 0.05 for i in range(5)]  # Створюємо список значень x
results_no_numpy = [(x, compute_simplified_series(x)) for x in x_values]  # Обчислення суми ряду для кожного x

# Виведення результатів
for x, result in results_no_numpy:
    print(f"x = {x}, сума ряду = {result}")
a = 0.5
b = 0.7
h = 0.05
tolerance = 0.001
x = a

while x <= (tolerance + 1e-8):
    series_sum = 0
    k = 1
    while True:
        value = (x + 2) / (k * (k + 2))
        if abs(value) <= tolerance:
            break
        k+=1
        series_sum += value
    x += h
    print(f"x = {x:.2f}, сума ряду = {series_sum:.6f}")
    print(f"x = {x}, сума ряду = {series_sum}")
    # x+=h