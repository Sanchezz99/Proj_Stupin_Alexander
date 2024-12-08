#Дано целое число N (>0). Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей).
def product_number(n):
    try:
        if n < 0:
            raise ValueError("n не должен быть отрицательным")
        product = 1.0
        for i in range(1, n + 1):
            product *= 1 + i / 10
        return product
    except ValueError as e:
        print(f"Увы, произошла ошибка: {e}")
        return 0
n = int(input("Введите число n: "))
result = product_number(n)
if result != 0:
    print(result)