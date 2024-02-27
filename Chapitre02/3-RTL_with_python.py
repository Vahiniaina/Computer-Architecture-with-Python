mem = [4,5,7,0,0,5,5,8]+[0]*8         # predefinie la memeoire
source1 = mem[mem[1]]          
source2 = mem[mem[2]]          
resultat = source1 + source2      
mem[mem[0]] = resultat          
print('La memoire: \n', mem)          