word = input("введите слово: ")
new_word = word[::-1]

if word.lower() == new_word.lower() :
    print ("является полиндромом")
else :
    print ("не является полиндромом")