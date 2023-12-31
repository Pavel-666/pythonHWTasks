# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам


def rhythm_of_phrase(phrase):
    vowel_list = 'уеыаоэюия'
    phrase = phrase.split(' ')
    union = []
    for i in phrase:
        count = 0
        for j in i:
            if j.lower() in vowel_list:
                 count += 1
        union.append(count)
    if len(set(union)) > 1:
        return False
    return True
while True:
    poem = input('введите ваш стих: ')
    if poem != 'stop':
        if rhythm_of_phrase(poem):
            print('Парам пам-пам')
        else:
            print('Пам парам')
    else:
        break





