from pprint import pprint
cook_book = {}

with open ('D:\Python\Task7_3\cook_book.txt') as file:
   
    for line in file:
        cook_name = line.strip()
        value = int(file.readline())
        lines2 = []
        for item in range(value):
            lines = []
            for i in file.readline().strip().split('|'):
               cook_ingridients = {}
               lines.append(i)
            cook_ingridients['ingredient_name'] = lines[0]
            cook_ingridients['quantity'] = lines[1]
            cook_ingridients['measure'] = lines[2]
            lines2.append(cook_ingridients)
        cook_book[cook_name] = lines2
        
        file.readline()
    pprint (cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    list_by_dishes = {}
    for cook_names in dishes:
        for cook, dish in cook_book.items():
            if cook in cook_names:

                    for i in dish:

                        ii  = i.copy()
                        ingridient = ii.pop('ingredient_name')

                        if ingridient not in list_by_dishes.keys():
                            ii['quantity'] = int (ii['quantity']) * person_count
                            list_by_dishes [ingridient] = ii
                        else:

                            double = list_by_dishes [ingridient]

                            double['quantity'] = (int(double['quantity'])) + (int (i['quantity']) * person_count)
                            list_by_dishes [ingridient] = double
                                     
    pprint ( list_by_dishes)
dishes = ['Омлет','Омлет','Фахитос']
person_count = 1
get_shop_list_by_dishes(dishes, person_count)