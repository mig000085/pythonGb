def check_rhythm(stroka):
    vowels = "аеёиоуыэюя"
    
    # Разделяем строку на фразы
    phrases = stroka.split()
    
    # Если фраза только одна, то ритм определить не получится
    if len(phrases) <= 1:
        return "Количество фраз должно быть больше одной!"
    
    # Функция для подсчета количества гласных в фразе
    def count_vowels(phrase):
        return sum(1 for char in phrase if char in vowels)
    
    # Получаем список количества гласных в каждой фразе
    syllable_counts = [count_vowels(phrase) for phrase in phrases]
    
    # Проверяем, одинаковое ли количество гласных в каждой фразе
    if all(count == syllable_counts[0] for count in syllable_counts):
        return "Парам пам-пам"
    else:
        return "Пам парам"

# Пример использования
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
result = check_rhythm(stroka)
print(result)
