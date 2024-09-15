# module_1_6.py
my_dict = {"Luda": 1985, "Nata": 1992, "Roma": 1980}  # создания списка ключ-значение
print(my_dict) # вывод словаря  на экран
print(my_dict["Luda"]) # вывод одного значения по ключу
print(my_dict.get("Kirill")) # вывод отсутствующего ключа
my_dict["lily"] = 1976 # добавление пары ключа 1
my_dict["Sahsa"] = 1985 # добавление пары ключа 2
print(my_dict) #
my_dict.pop("Nata") # удаление елемента
print(my_dict) # вывод словаря  на экран

my_set = {1, 2, 3, 4.5, "кoмпот", True, (1, 1, 1), 2, 4.5,} #
print(my_set) #
my_set.add(9) #
my_set.add(8.6) #
my_set.remove(4.5) #
print(my_set) #
