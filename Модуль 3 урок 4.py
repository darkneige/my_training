def single_root_words(root_word, *other_words):
    same_words = []
    words = 0
    for i in other_words:
        if root_word.count(i) or i.count(root_word):
            same_words.append(i)
            words += 1
    if words == 0:
        print('Нет содержащихся слов')
    else:
        print(same_words)
    return same_words


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
