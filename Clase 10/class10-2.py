c= {'a':10, 'b':1, 'c':22} #diccionario
tmp= list() #crea una lista
for k,v in c.items(): #key, value. Iteración que añade cada valor y llave en la lista
    tmp.append((v,k)) #se crea una lista de una tupla

tmp= sorted(tmp, reverse=True) #ordena de mayor a menor
print(tmp)

'''
SORT BY VALUES INSTEAD OF KEY
'''
