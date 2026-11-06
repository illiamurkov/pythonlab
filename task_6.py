day = int(input("введите дату рождения: "))
month = int(input("введите месяц: "))
year = int(input("введите год рождения: ")) #для красоты)

print(f"ваша дата рождения: {day}.{month}.{year}")

birthday = month * 100 + day
if birthday >= 120 and birthday <= 218:
    print("ваш знак: водолей")
elif birthday >= 219 and birthday <= 320:
    print ("ваш знак: рыбы")
elif birthday >= 321 and birthday <= 420:
    print ("ваш знак: овен")
elif birthday >= 420 and birthday <= 520:
    print ("ваш знак: телец")
elif birthday >= 521 and birthday <= 620:
    print ("ваш знак: близнецы")
elif birthday >= 621 and birthday <= 722:
    print ("ваш знак: рак")
elif birthday >= 723 and birthday <= 822:
    print ("ваш знак: лев")
elif birthday >= 823 and birthday <= 922:
    print ("ваш знак: дева")
elif birthday >= 923 and birthday <= 1022:
    print ("ваш знак: весы")
elif birthday >= 1023 and birthday <= 1121:
    print ("ваш знак: скорпион")
elif birthday >= 1122 and birthday <= 1221:
    print ("ваш знак: стрелец")
elif birthday >= 1222 and birthday <= 119:
    print ("ваш знак: козерог")
