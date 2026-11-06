vozrast = int(input("введите возраст: "))
dohod = float(input("введите ежемесячный доход: "))

zapros_kredita = float(input("введите запрашиваемую сумму: "))

srok_kredita = int(input("введите срок кредита в месяцах: "))
kredit_istoria = input("введите вашу кредитную историю (отличная/хорошая/удовлетворительная/плохая): ")

is_poruchitel = input("есть ли у вас поручитель да/нет: ")
is_zalog = input("произведен ли взнос залога да/нет: ")

is_odobrenie = int(0)

sootnoshenie = 0

if vozrast < 21:
    print("кредиты выдаются с 21, гуляй")
elif vozrast >= 58:
    print("кредиты не выдаются после 58")
else:
    is_odobrenie += 0


sootnoshenie = zapros_kredita / dohod
print (f"соотношение кредита к доходу: {sootnoshenie:.3f}")

if zapros_kredita <= 15000:
    print("процентная ставка составит 5%")
    is_odobrenie += 1
elif zapros_kredita > 15000 and zapros_kredita <= 40000:
    print("процентная ставка составит 7%")
    is_odobrenie += 2
else:
    print("процентная ставка составит 9%")
    is_odobrenie += 3

if dohod < 2500:
        is_odobrenie += 2
else:
        is_odobrenie += 1

if srok_kredita < 24:
     is_odobrenie += 1
else:
     is_odobrenie += 0

if is_zalog.lower() == 'да' :
     is_odobrenie += 0
else:
     is_odobrenie += 1

if is_poruchitel == 'да' :
     is_odobrenie += 0
else:
     is_odobrenie += 1

if kredit_istoria.lower() == 'отличная' : is_odobrenie += 0
if kredit_istoria.lower() == 'хорошая' : is_odobrenie += 1
if kredit_istoria.lower() == 'удовлетворительная' : is_odobrenie += 2
else: is_odobrenie += 3

if is_odobrenie < 3 :
     print(f"категория риска {is_odobrenie} балла, риск маленький")
     is_odobrenie += 0
elif is_odobrenie <= 7 and is_odobrenie > 3:
     print(f"категория риска {is_odobrenie} балла, риск средний")
     is_odobrenie += 1
elif is_odobrenie > 7 and is_odobrenie < 9:
    print(f"категория риска {is_odobrenie} балла, риск высокий")
    is_odobrenie += 2
else:
    print(f"категория риска {is_odobrenie} балла, риск критический")
    is_odobrenie += 3

if is_odobrenie < 9 :
     print("банк одобряет ваш запрос")
else:
     print("банк не одобрил ваш запрос")