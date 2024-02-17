def popular_words(text: str, words: list) -> dict:
    text = text.strip()
    """ This function returns a dictionary that shows words and their popularity in a string """
    # Створили за доп. dict comprehencion dict з key (слова в даному рядку) та value (0, початкова кільк. шуканих слів).
    popularity_dict = {k.lower(): v for (k, v) in zip(text.split(), [0 for element in range(len(text.split()))])}
    # Додаємо у створений dict слова з шуканих, якщо їх немає у ньому.
    for s_w in range(len(words)):
        if words[s_w].lower() not in popularity_dict:
            popularity_dict[words[s_w].lower()] = 0

    # Підраховуємо "популярність" шуканих слів.
    for s_w in range(len(words)):
        for w in range(len(text.split())):
            if text.lower().split()[w] == words[s_w]:
                popularity_dict[words[s_w]] = popularity_dict.get(words[s_w]) + 1

    # Видаляємо з dict елементи, які не є шуканими.
    elements_to_delete = set(popularity_dict.keys()).difference(words)
    for elem in elements_to_delete:
        del popularity_dict[elem]
    return popularity_dict


assert popular_words('''Hi! When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')