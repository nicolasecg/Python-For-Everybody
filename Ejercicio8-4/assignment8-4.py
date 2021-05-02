filename = input("Enter file name: ")
filehandler = open(filename)
mylist=list() #crea la lista
for line in filehandler:  #lee cada linea
    line= line.rstrip().split()  #elimina espacios en blanco y rompe el string(texto) en partes
    #words= line.split()
    for word in line:   #busca las palabras repetidas
        if word in mylist:
            continue
        else:
            mylist.append(word)

mylist.sort() #ordena alfabeticamente, recordar que para python las mayusculas son menores
print(mylist)

'''
Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
 The program should build a list of words. For each word on each line check to see if the word is already in the list
 and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
'''
