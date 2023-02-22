# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number=int(input("Введите число: "))
stepen=2
countStepen=0
while stepen<=number:
    stepen*=2
    countStepen+=1
print(countStepen)


