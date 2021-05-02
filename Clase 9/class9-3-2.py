name= input('Enter file:')
handle= open(name)

counts= dict() #crea el diccionario
for line in handle:
    words= line.split() #divide cada linea en palabras
    for word in words:
        counts[word]= counts.get(word,0)+1 #encuentra las palabras y el número de veces que se repite cada una

bigcount= None #no se puede 0 porque estamos trabajando con valores de texto (String)
bigword= None
for word,count in counts.items():   #key, value, dos variables de iteración   items= key,value pairs
        if bigcount is None or count>bigcount: #maximum loop
            bigcount=count
            bigword=word

print(bigword,bigcount)
