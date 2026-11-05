def pravka_spiska(lst):
    i = 0
    while i < len(lst):
        item = lst[i]
      
        if isinstance(item, list):
          pravka_spiska(item)
          lst[i:i+1] = item

        else:
           i += 1

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]

print(f"до правки: {list_a}")

pravka_spiska(list_a)

print(f"после правки: {set(list_a)}")