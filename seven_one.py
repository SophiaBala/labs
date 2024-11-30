def is_brackets_balanced(input):
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for char in input:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if stack and brackets[stack[-1]] == char:
                stack.pop()
            else:
                return False

    return len(stack) == 0

input = input("Введіть рядок із дужками, які ви хочете перевірити: ")
result = is_brackets_balanced(input)

print(f"Результат: {'Все правильно!' if result else 'Упс, ви пропустили дужки'}")
