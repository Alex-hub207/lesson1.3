example = 'смородина'
print(example[0])
print(example[-1])
print(example[int(len(example)/2):len(example)]) # Здесь я воспользовался тем, что знаю, количество символов в исходной строка.
# Иначе придется оператор ветвления ставить.
print(example[::-1])
print(example[1::2])