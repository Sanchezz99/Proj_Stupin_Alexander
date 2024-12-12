def forty_characters():
    characters = "QWERTYUIOP[]ASDFGHJKL;'ZXCVBNM,./`1234567890-=!@#$%^&*()_+<>?:"
    while True:
        try:
            num_characters = int(input("Введите количество символов для вывода (мвусимум 40): "))
            if num_characters < 1 or num_characters > 40:
                raise ValueError("Число должно быть от 1 до 40")
            print(characters[:num_characters])
            break
        except ValueError as e:
            print(f"Увы, произошла ошибка: {e}. Попробуйте снова.")
forty_characters()