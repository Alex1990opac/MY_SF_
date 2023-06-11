""" Игра угадай число 
Итоговая версия
Компьютер угадывает число менее чем за 20 попыток"""

import numpy as np

def quessing_the_number(number) -> int:
    """Функция отгадывает загаданное число менее чем за 20 попыток

    Args:
        number (int): Загаданное число

    Returns:
        int: Количество попыток
    """
    estimated_number = np.random.randint(1, 101)
    max_number = 100
    min_number = 0
    count = 0 
    
    while True:
        count += 1
        
        if estimated_number > number:
            max_number = estimated_number - 1
            estimated_number = (max_number + min_number)//2
        
        
        elif estimated_number < number:
            min_number = estimated_number + 1
            estimated_number = (max_number + min_number)//2
        
        
        else:
            break
    
    return count

if __name__ == '__mane__':
    
    print(quessing_the_number())
            
        
