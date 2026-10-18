last_name = input("введите фамилию: ")
first_name = input("введите имя: ")
middle_name = input("введите отчество: ")

fixed_last_name = last_name[0].upper() + last_name[1:].lower()

print (f"{fixed_last_name} {first_name[0].upper()}.{middle_name[0].upper()}.")
