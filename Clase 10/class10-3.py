filehandler= open('romeo.txt')
counts=dict()
for line in filehandler:
    words=line.split()
    for word in words:
        counts[word]= counts.get(word,0)+1

lst=list()
for key,val in counts.items():
    newtup= (val,key) #creo una nueva tupla value, key y la pongo en una variable llamada newtup
    lst.append(newtup) #añado a la lista la tupla

lst= sorted(lst,reverse=True)    #se ordena la lista al revés (de mayor a menor)

for val,key in lst[:10]: #cortamos y solo usamos los primeros 10 valores (list slicing)
    print(key,val) #se imprime en el orden en el que queriamos verlo desde el inicio (se cambia el orden en como se iteró la estructura de datos y como se va a imprimir realmente)

'''
TOP TEN MOST COMMON WORDS ON A FILE
'''
