filehandler= open('mbox-short.txt')
counts=dict()
for line in filehandler:
    if not line.startswith('From '):
        continue
    words=line.split() #split, will convert the regular line, into an array, with each word, as an element of the array;
    time=words[5] #the 5th element is the hour in the array "line", which is what the problem is asking for
    hours=time[:2] #the word however is a string in the standard hour format, HH:MM:SS.. hence the stripping of the string from 0-> 2 , will result in HH only
    counts[hours]=counts.get(hours,0)+1
'''
increments the dictionary (with two elements, the key, value set, where the key (i.e. the hour),
is incremented each time there is an occurrenece. in other words, if there are emails sent 10 times by anyone,
 in that hour, the count of emails sent in "that hour" is incremented.
 However, the "get" function for a dictionary is used to for returning a ZERO, in case that particular "key" or the hour
 is being read for the first time., in which case the get function returns a ZERO, for the first occureence in the for loop.
  This is done in order to avoid the trace error mem overflow
'''
lista=list()
for value,key in counts.items():
    nuevatupla=(value,key)  #creo tupla
    lista.append(nuevatupla)  #añado a lista la tupla

lista=sorted(lista,reverse=False) #se ordena (sort) la lista de menor a mayor o da lo mismo que lista.sort()

for value,key in lista:
    print(value,key) #se imprime en el orden solicitado
