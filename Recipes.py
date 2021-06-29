from pprint import pprint

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = {}

    f = open('recipes.txt', encoding='utf-8')
    for line in f:
        dishe = line.strip()
        count = int(f.readline().strip())
        some_list = []
        for i in range(count):
            ingr = f.readline().strip().split("|")
            ingr_dict = {"ingredient_name": ingr[0]}
            ingr_dict["quantity"] = ingr[1]
            ingr_dict["measure"] = ingr[2]
            some_list.append(ingr_dict)
        f.readline().strip()
        cook_book[dishe] = some_list
    # pprint(cook_book)

    list_of_ing = {}

    for dish in dishes:
        if dish in cook_book:
            come_list = cook_book[dish]
            for var_a in come_list:
                var_a['quantity'] = int(var_a['quantity']) * person_count
                ing_name = var_a['ingredient_name']
                del (var_a['ingredient_name'])
                for var_b in list_of_ing:
                    if ing_name in list_of_ing:
                        f = list_of_ing[var_b]
                        var_a['quantity'] = var_a['quantity'] + int(f['quantity'])
                        break
                list_of_ing[ing_name] = var_a
        else:
            pprint ('Нет такого блюда')
            break

    pprint(list_of_ing)

get_shop_list_by_dishes(['Утка по-пекински', 'Омлет'], 2)