## Exercise No. 1: Number guessing name

import random

def guessing_game():
    
    n = random.randint(0,100)
    p = 0
    print(n)
    while p!=n:
        
        p = int(input(print("Digita el número que crees")))
        
        if p>n:
            
            print("Too high")
            
        elif p<n:
            
            print('Too low')
    
    return f'Adivinaste que el número es: {n}'

guessing_game()
