vozrast = int(input("введите возраст: "))
is_HB = input("сегодня день рождения да/нет: ")
is_VIP = input("является ли клиент VIP да/нет: ")
chek = int(input("введите сумму вашего чека: "))

total_chek = chek

total_sale = int(0)

is_HB = True if is_HB.lower() == "да" else False
is_VIP = True if is_VIP.lower() == "да" else False

if vozrast >= 63:
    total_sale += 5
if is_HB == True:
    total_sale += 5
if is_VIP == True:
    total_sale += 15
if chek > 1000 and is_VIP == False:
    total_sale += 10

print(f"ваша итоговая скидка : {total_sale}")

total_sale = total_sale / 100

total_chek = chek - chek * total_sale

print (f"итоговая сумма чека составила: {total_chek}BYN")