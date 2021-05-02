counts=dict()  #crea el diccionario
print('Enter a line of text:')
line= input('')

words= line.split() #divide la linea en palabras
print('Words',words) #muesta las palabras

print('Counting...')
for word in words:  #loop through the words
    counts[word]= counts.get(word,0)+1 #cuenta las palabras y el numero de veces que se repite cada una
print('Counts',counts)
