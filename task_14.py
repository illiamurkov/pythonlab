vvod1 = input("введите первый список: ").split()
spisok_1 = []
for num in vvod1:
    spisok_1.append(float(num))
#print(spisok_1)

vvod2 = input("введите второй список: ").split()
spisok_2 = []
for num in vvod2:
    spisok_2.append(float(num))
#print("списки созданы")

odinakovi = []
netvovtorom = []
for num in set(spisok_1):
    for num1 in set(spisok_2):
        if num == num1:
            odinakovi.append(num)
        else:
            continue
print(f"список чисел которые есть в двух списках: {odinakovi}")

netvovtorom = [num for num in spisok_1 if num not in spisok_2]
print(netvovtorom)

netvpervom = [num for num in spisok_2 if num not in spisok_1]
print(netvpervom)

vsekromeobshego = [list(set(spisok_1) ^ set(spisok_2))]
print(vsekromeobshego)