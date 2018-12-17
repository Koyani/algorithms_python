#task_8
#8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
year = int(input('Enter year number to check if it\'s leap year: '))
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print("usual year")
else:
    print("leap year")