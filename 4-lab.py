from itertools import combinations, groupby

# Задача 1: Работа с кортежами

# 1.1 Создание кортежа из ввода пользователя (строка без пробелов)
user_input = input("Enter a string without spaces: ")
my_tuple = tuple(user_input)  
print("Created tuple:", my_tuple) 
"""
user_input = input("Enter a string without spaces: "): This line prompts the user to enter a string without spaces. The input() function reads the user's input and stores it in the variable user_input.

my_tuple = tuple(user_input): This line converts the string user_input into a tuple called my_tuple. In this case, the tuple will contain individual characters from the input string. Each character in the string becomes an element in the tuple.

print("Created tuple:", my_tuple): Finally, this line prints the created tuple my_tuple. You will see the characters of the input string separated by commas, enclosed in parentheses, indicating that they are part of a tuple.
"""

# 1.2 Преобразование кортежа в строку (используя кортеж из задачи 1.1)
my_tuple = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')
my_string = ''.join(my_tuple) 
print("String: ", my_string) 
"""
my_tuple = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n'): This line defines a tuple called my_tuple containing individual characters.

my_string = ''.join(my_tuple): This line joins the characters in the tuple my_tuple into a single string. The join() method is used to concatenate the characters without any separator (an empty string is used as the separator).

print("String: ", my_string): Finally, this line prints the resulting string stored in the variable my_string.
"""

# 1.3 Сцепление двух кортежей (первая половина кортежа A с второй половиной кортежа B)
tuple_A = (1, 2, 3, 4, 5, 6, 7)
tuple_B = (5, 6, 7, 9, 7, 1, 10, 10)
combined_tuple = tuple_A[:4] + tuple_B[4:]  
print(combined_tuple) 
"""
tuple_A = (1, 2, 3, 4, 5, 6, 7): This line defines tuple_A, which contains seven elements.

tuple_B = (5, 6, 7, 9, 7, 1, 10, 10): This line defines tuple_B, which contains eight elements.

combined_tuple = tuple_A[:4] + tuple_B[4:]: This line combines elements from both tuples to create combined_tuple. It takes the first four elements from tuple_A (index 0 to 3) and concatenates them with elements from tuple_B starting from the fifth element (index 4 and onwards).

print(combined_tuple): Finally, this line prints the combined_tuple.
"""

# 1.4 Подсчет и создание кортежа с количеством вхождений элементов
my_tuple = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
element_count = {} 
for element in my_tuple:
    element_count[element] = element_count.get(element, 0) + 1 
result_tuple = tuple((k, v) for k, v in element_count.items())  
print("Elements and their occurrences:", result_tuple) 
"""
my_tuple = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6): This line defines my_tuple, which contains various elements.

element_count = {}: An empty dictionary named element_count is created to store the count of each unique element in my_tuple.

The for loop iterates through each element in my_tuple:

element_count[element] = element_count.get(element, 0) + 1: For each element, it checks if the element already exists in the element_count dictionary. If it does, it increments the count by 1. If it doesn't exist, it initializes the count to 1.
result_tuple = tuple((k, v) for k, v in element_count.items()): This line creates a new tuple, result_tuple, by converting the key-value pairs from the element_count dictionary into tuples. Each tuple consists of an element and its count.

print("Elements and their occurrences:", result_tuple): Finally, this line prints the elements and their occurrences in the result_tuple.
"""

# 1.5 Создание кортежей для хранения разных типов данных
data = (55, 6, 777, 70.0, '7', 'A')
integers = tuple(x for x in data if isinstance(x, int))  
floats = tuple(x for x in data if isinstance(x, float))  
strings = tuple(x for x in data if isinstance(x, str)) 
print("Integers:", integers)  
print("Floats:", floats) 
print("Strings:", strings) 
"""
data = (55, 6, 777, 70.0, '7', 'A'): This line defines the data tuple, which contains a variety of elements, including integers, floats, and strings.

integers = tuple(x for x in data if isinstance(x, int)): This line creates a tuple integers by using a list comprehension to filter elements from data that are instances of integers (int data type).

floats = tuple(x for x in data if isinstance(x, float)): Similarly, this line creates a tuple floats by filtering elements from data that are instances of floats (float data type).

strings = tuple(x for x in data if isinstance(x, str)): Here, a tuple strings is created by filtering elements from data that are instances of strings (str data type).

print("Integers:", integers): This line prints the elements in the integers tuple.

print("Floats:", floats): This line prints the elements in the floats tuple.

print("Strings:", strings): Finally, this line prints the elements in the strings tuple.
"""

# Задача 2: Работа с множествами и генераторами множеств

# 2.1 Создание множества из ввода пользователя (строка без пробелов) с использованием генератора множеств
user_input = input("Enter a string without spaces: ")
my_set = {char for char in user_input} 
print("Created set:", my_set) 
"""
user_input = input("Enter a string without spaces: "): This line prompts the user to enter a string without spaces and stores the input in the user_input variable.

{char for char in user_input}: This is a set comprehension that iterates through each character (char) in the user_input string. It creates a set by adding each unique character to the set. Sets automatically remove duplicates, so the resulting set contains only unique characters.

print("Created set:", my_set): Finally, this line prints the created set, my_set, which contains the unique characters from the user's input.
"""

# 2.2 Поиск различий между двумя множествами
set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}
difference_set = set_A.difference(set_B) 
print("Set difference:", difference_set) 
"""
set_A = {1, 2, 3, 4, 5}: This line defines the set_A set containing integers from 1 to 5.

set_B = {5, 7, 8, 9, 2, 10}: Similarly, this line defines the set_B set containing integers, some of which overlap with set_A.

difference_set = set_A.difference(set_B): This line calculates the set difference between set_A and set_B by using the difference method. It creates a new set, difference_set, which contains the elements that are in set_A but not in set_B.

print("Set difference:", difference_set): Finally, this line prints the elements in the difference_set, which represents the set difference between set_A and set_B.
"""

# 2.3 Удаление элементов из множества A, которые также присутствуют в множестве B
set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}
set_A.difference_update(set_B)  
print("Updated set A:", set_A) 
"""
set_A = {1, 2, 3, 4, 5}: This line defines the initial set, set_A, containing integers from 1 to 5.

set_B = {5, 7, 8, 9, 2, 10}: Similarly, this line defines another set, set_B, containing integers, with some overlapping elements with set_A.

set_A.difference_update(set_B): This line uses the difference_update method on set_A, passing set_B as an argument. This method modifies set_A by removing elements that are common between set_A and set_B.

print("Updated set A:", set_A): Finally, this line prints the modified set_A after the difference update operation.
"""

# 2.4 Обновление множеств на основе элементов в множестве C
set_A = {1, 2, 3, 4, 7}
set_B = {8, 7, 9, 4, 2, 0, 10}
set_C = {4, 0, 1}
set_C.update(set_A.intersection(set_C))  
set_A.difference_update(set_A.intersection(set_C))  
print("Updated set C:", set_C) 
"""
set_A = {1, 2, 3, 4, 7}: This line defines the set_A set containing integers.

set_B = {8, 7, 9, 4, 2, 0, 10}: Similarly, this line defines the set_B set with some overlapping elements with set_A.

set_C = {4, 0, 1}: This line defines the set_C set containing integers.

set_C.update(set_A.intersection(set_C)): This line updates set_C by adding the elements that are in both set_A and set_C. The intersection method finds the common elements, and update adds them to set_C.

set_A.difference_update(set_A.intersection(set_C)): This line modifies set_A by removing elements that are common between set_A and set_C using the difference_update method.

print("Updated set C:", set_C): Finally, this line prints the modified set_C.
"""
# 2.5 Создание списка множеств размера m из комбинаций из супермножества A
A = {1, 2, 3, 4, 5, 6}
n = 3 
m = 5 
result = [set(combo) for combo in combinations(A, n)][:m] 
print("List of sets:", result)  
"""
A = {1, 2, 3, 4, 5, 6}: This line defines the set A containing integers from 1 to 6.

n = 3: The variable n is set to 3, which represents the number of elements to select in each combination.

m = 5: The variable m is set to 5, which represents the number of combinations you want to include in the result.

result = [set(combo) for combo in combinations(A, n)][:m]: This line generates the list of sets. It uses a list comprehension and the combinations function from the itertools module to generate combinations of n elements from the set A. The list comprehension then converts these combinations into sets. Finally, it slices the list to include only the first m sets in the result.

print("List of sets:", result): This line prints the list of sets that were generated.
"""

# Задача 3: Группировка данных по производителю

cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]


sorted_cars = sorted(cars_list, key=lambda x: x[0])

for manufacturer, group in groupby(sorted_cars, key=lambda x: x[0]):
    group_list = list(group)  
    count = len(group_list)  
    models = [car[1] for car in group_list] 
    print(f"{manufacturer} {count} - {', '.join(models)}") 
    """
    cars_list is a list of tuples, where each tuple contains two elements: the car manufacturer (e.g., 'BMW') and the car model (e.g., 'X6').

sorted_cars sorts the cars_list based on the car manufacturer (the first element in each tuple) using the sorted function. This step is essential to group cars by manufacturer later.

groupby is used from the itertools module to group the sorted list of cars by the car manufacturer. It uses a lambda function as the key to extract the manufacturer (the first element of each tuple).

Within the loop over grouped cars, the following steps are performed for each manufacturer's group:

group_list is created by converting the group iterator to a list. This is done to access and count the cars in the group.
count is calculated as the length of the group_list, giving the count of cars from the same manufacturer.
models is a list comprehension that extracts the car models (the second element of each tuple) from the group_list.
Finally, a formatted string is printed, displaying the manufacturer's name, the count of cars, and the list of car models for that manufacturer.
    """