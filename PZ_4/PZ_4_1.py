#Дано целое число N (>0). Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей).
def product_number(N):
    try:
        if N < 0:
            raise ValueError("N не должен быть отрицательным")
        product = 1.0
        i = 1
        while i <= N:
            product *= 1 + i / 10
            i += 1
        return product
    except ValueError as e:
        print(f"Увы, произошла ошибка: {e}")
        return 0
N = int(input("Введите число N: "))
result = product_number(N)
if result != 0:
    print(result)