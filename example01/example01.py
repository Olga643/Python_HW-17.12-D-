# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def InputNumbers(Text):
    test = False
    while not test:
        try:
            number = float(input(f"{Text}"))
            test = True
        except ValueError:
            print("Это не число!")
    return number


def sumNums(number):
    sum = 0
    for i in str(number):
        if i != ".":
            sum += int(i)
    return sum


num = InputNumbers("Введите число: ")

print(f"Сумма цифр = {sumNums(num)}")
