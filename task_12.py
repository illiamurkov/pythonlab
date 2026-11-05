text = input("введите предложение: ").lower()
znaki_prepinaniya = [',', '.', '?', '!', '-', ':', ';']

for znaki in znaki_prepinaniya:
    text = str(text.replace(znaki, ''))

words = text.split()
print(f"разбиение текста на отдельные слова: {words}")

kolichestvo = len(words)
print(f"общее кол-во слов: {kolichestvo}")

slovarik = {}

for word in set(words) :
    chastota = words.count(word)
    slovarik[word] = chastota
    print(f"слово: {word} встречается {chastota} раз(а))")

most_common = max(slovarik, key=slovarik.get)
print(f"встречается чаще всего: {most_common}, конкретно: {slovarik[most_common]} раз(а)")

max_len_word = max(slovarik, key=len)
print(f"самое длинное слово: {max_len_word} длинна: {len(max_len_word)} букв(ы)")

min_len_word = min(slovarik, key=len)
print(f"самое короткое слово: {min_len_word} длинна: {len(min_len_word)} букв(ы)")

filtr_words = [word for word in words if len(word) >= 3]
print(f"отфильтрованный список: {filtr_words} кол-во слов: {len(filtr_words)}")