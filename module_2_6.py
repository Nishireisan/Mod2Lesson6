def single_root_words(root_word, *other_words):
    same_word = []
    root_word = root_word.lower()
    for i in other_words:
        k = i.lower()
        if k.count(root_word) == 1 or root_word.count(k) == 1:
            same_word.append(i)
        # пройти каунтом по слову
    return same_word


r = single_root_words('low', 'lower', 'follower', 'loadw')
print(r)
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
