"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

# колличество попыток
count = 0

while True:
    count+=1
    predict_number = int(input("Угадай число от 1 до 100: "))
    
    if predict_number < number:
        print("Число должно быть больше")
    
    elif predict_number > number:
        print("Число должно быть меньше")
    
    else:
        print(f"Вы угадали число, это число {number}, за {count} попыток") 
        break # конец игры выход из цикла
