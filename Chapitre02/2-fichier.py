
with open("fichier_source.txt",'r') as example:          
 theText = example.readlines()                      
print('LE fichier source: \n ',theText)                   
for i in range(0,len(theText)):                     
 theText[i] = theText[i].rstrip()                   
print('Le fichier source sans \\n ',theText)
