def dict_merge(slovarik_1, slovarik_2):
    
    for key, chislo in slovarik_2.items():
        if key in slovarik_1 and isinstance(slovarik_1[key], dict) and isinstance(chislo, dict):
            dict_merge(slovarik_1[key], slovarik_2[key])
        else:
            slovarik_1[key] = chislo
    
    return slovarik_1

dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}

dict_merge(dict_a, dict_b)

print(dict_a)