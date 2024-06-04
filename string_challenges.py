# Вывести последнюю букву в слове
word = 'Архангельск'

print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'

print(word.count("а"))  #Только для строчных букв
print(word.lower().count("а"))  #Если надо посчитать все заданные буквы

# Вывести количество гласных букв в слове
word = 'Архангельск'

count = 0
vowels = set("АИОУЫЭЕЁЮЯ")
for letter in word.upper():
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

count = 0
for i in sentence.split():
    count += len(i)
print(count / len(sentence.split()))
