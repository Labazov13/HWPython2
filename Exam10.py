import random
# На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

countCoin=int(input("Введите количество монеток: "))
eagle=1
tails=0
countTails=0
countEagle=0

for i in range(countCoin):
    i=random.randint(tails,eagle)
    if i==tails:
        countTails=countTails+1
    else:
        countEagle=countEagle+1
    print(i)
print(countTails,countEagle)

if countTails>=countEagle:
    print('Необходимо перевернуть монеты вверх орлом '+str(countEagle)+' раз')
else:
    print('Необходимо перевернуть монеты вверх решкой '+ str(countTails) +' раз')
