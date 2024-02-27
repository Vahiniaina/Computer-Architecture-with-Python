print('Bonjour.mettez une operation de la form 23 * 4. Taper Q pour quitter.')         
go = 1                                                                      
while go == 1: 
    while True:
        x = input('Taper le premier chiffre: ')  
        try:                                     
            x1 = int(x)
            break
        except erreur:
            continue                           
    while True:                                   
        op = input('Taper l\'operateur + ou - ou / ou *: ') 
        if op == 'Q' or op == '+' or op == '-' or op == '/' or op == '*':
            break  
                         
    if op == 'Q':                                                        
        go = 0                                                              
        print('Fin du programme')                                             
        break   
    while True:                                             
        y = input('Taper le second chiffre: ')  
        try:                                     
            y1 = int(y)
            break
        except erreur:
            continue                                                        
    if op == '+': 
        resultat = x1 + y1 
        print('Resultat = ', resultat, '\n')                                          
    if op == '-': 
        resultat = x1 - y1
        print('Resultat = ', resultat, '\n') 
    if op == '/': 
        resultat = x1 / y1
        print('Resultat = ', resultat, '\n')
    if op == '*': 
        resultat = x1 * y1
        print('Resultat = ', resultat, '\n')
                                        