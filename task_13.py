vvod = input("введите числа через пробел: ").split()
chisla = []

for num in vvod:
    chisla.append(float(num))
unik = []
for num in set(chisla):
    if float(num).is_integer():  
        num = int(float(num))
    unik.append(num)  
print(unik)

povt = []
for num in unik:
   if chisla.count(num) >= 2:
      povt.append(num)
print(povt)

chet = []
nechet = []
for num in unik:
   if float(num).is_integer() and num % 2 == 0:
      chet.append(num)
   else:
      nechet.append(num)
print(f"четные: {chet}")
print(f"нечетные: {nechet}")

neg = []
for num in unik:
   if num < 0:
      neg.append(num)
print(f"отрицательные: {neg}")

float_num = []

for num in unik:
   if float(num).is_integer():
      continue
   else:
      float_num.append(num)
print(f"c плавающей точкой: {float_num}")


summ_5 = []
summa = 0
for num in unik:
   if float(num).is_integer() and num % 5 == 0:
      summa += num
print(f"сумма чисел кратных пятерке: {summa}")

slovarik = {}
for num in set(chisla):
   slovarik[num] = num 

max_num = max(slovarik, key=slovarik.get)
print(max_num)

min_num = min(slovarik, key=slovarik.get)
print(min_num)