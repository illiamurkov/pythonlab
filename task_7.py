minuti = float(input("введите израсходованные минуты: "))
sms = float(input("введите кол-во израсходованных сообщений: "))
inet = float(input("введите ол-во израсходованных мг: "))

price = float(24.99)
new_price = float
new_price = price

new_price_minuti = float
new_price_sms = float
new_price_inet = float

print (f"ваш базовый тариф: {price:.2f}")

if minuti > 60 :
    new_minuti = minuti - 60
    new_price_minuti = new_minuti * 0.89
    new_price += new_price_minuti
    print(f"ваше превышение: {new_minuti} минут, что составит {new_price_minuti:.2f}BYN")

if sms > 30 :
    new_sms = sms - 30
    new_price_sms = new_sms * 0.59
    new_price += new_price_sms
    print(f"ваше превышение: {new_sms} сообщений, что составит {new_price_sms:.2f}BYN")


if inet > 1000 :
    new_inet = inet - 1000
    new_price_inet = new_inet * 0.79
    new_price += new_price_inet
    print(f"ваше превышение: {new_inet} мг, что составит {new_price_inet:.2f}BYN")

new_price = new_price * 0.02 + new_price

print(f"итоговая стоимость к оплате тарифа учитывая налог составит: {new_price:.2f}BYN")