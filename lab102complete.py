with open('en-ru.txt', 'r', encoding='utf-8') as f:
    # Создаем пустой словарь для хранения русско-английских пар
    ru_en_dict = {}
    # Читаем файл построчно
    for line in f:
        # Удаляем лишние символы и разделяем строку на два слова
        en_word = line.strip()[0].split(' ')
        ru_words = line.strip()[1].split(' ')
        # Если встречаем слово, которое уже есть в словаре,
        # добавляем к его значению новое значение
        if en_word in ru_en_dict:
            ru_en_dict[en_word] += ', ' + ru_words
        # Иначе создаем новую запись в словаре
        else:
            ru_en_dict[en_word] = ru_words

    # Открываем файл для записи
with open('ru-en.txt', 'w', encoding='utf-8') as f:
    # Сортируем ключи по алфавиту
    for ru_word in sorted(ru_en_dict.keys()):
        # Записываем пары в выходной файл
        f.write('{} - {}\n'.format(ru_en_dict[ru_word], ru_word))