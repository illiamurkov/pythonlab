summ = int(input("введите сумму: "))

n100 = 0
n50 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0

n100 = summ // 100
summ = summ % 100

n50 = summ // 50
summ = summ % 50

n10 = summ // 10
summ = summ % 10

n5 = summ // 5
summ = summ % 5

n2 = summ // 2
summ = summ % 2

n1 = summ

print (f"понадобится\n{n100} купюр(ы) номеналом 100BYN\n{n50} купюр(ы) номеналом 50BYN\n{n10} купюр(ы) номеналом 10BYN\n{n5} купюр(ы) номеналом 5BYN\n{n2} купюр(ы) номеналом 2BYN\n{n1} купюр(ы) номеналом 1BYN\n")