tovari = [
    {"name": "носки", "price": 50, "kolvo": 50},
    {"name": "кроссовки", "price": 400, "kolvo": 13},
    {"name": "майка", "price": 110, "kolvo": 19},
    {"name": "носки", "price": 150, "kolvo": 21},
          ]

viruchka = {}
for tovar in tovari:
   
    name = tovar["name"]
    price = tovar["price"]
    kolvo = tovar["kolvo"]

    summa = price * kolvo
    viruchka[name] = viruchka.get(name,0) + summa
print(f"выручка по товарам: \n{viruchka}")

max_viruchka = max(viruchka, key=viruchka.get)
print(f"товар с самой большой выручкой: {max_viruchka}")

unik_name = set(tovar["name"] for tovar in tovari)
print(f"кол-во уникальных наименований: {len(unik_name)}")