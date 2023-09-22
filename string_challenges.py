# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1:])


# Вывести количество букв "а" в слове
word = 'Архангельск'
count = word.lower().count("а")
print(count)


# Вывести количество гласных букв в слове
word = 'Архангельск'
count = 0
# А, Я, О, Ё, У, Ю, И, Ы, Э, Е 
vowels = 'аяоёуюиыэе'
for letter in word.lower():
    if letter in vowels:
        count += 1
print(count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words_count = len(sentence.split())
words_length = 0
for word in sentence.split():
    words_length += len(word)
print(words_length/words_count)