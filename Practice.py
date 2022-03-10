## Exercise No. 1: Number guessing name

import random

def guessing_game():
    
    n = random.randint(0,100)
    
    while p!=n:
        
        p = int(input(print("Digita el número que crees")))
        
        if p>n:
            
            print("Too low")
            
        elif p<n:
            
            print('Too high')
    
    return (n,p)

guessing_game()
