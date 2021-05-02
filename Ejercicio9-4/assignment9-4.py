'''
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they
appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to
find the most prolific committer.
'''
filename=input('Enter file name')
filehandler= open(filename)
counts=dict()
for line in filehandler:
    if not line.startswith('From:'):
        continue
    words=line.split() #divide cada linea (string total) en una lista de palabras (string por cada palabra) 
    words1=words[1] #toma la primera palabra unicamente
    counts[words1]= counts.get(words1,0)+1 #encuentra las palabras y cuenta el numero de veces que se repite cada una

maxcount= None
maxword= None
for word,count in counts.items():
    if maxcount is None or count>maxcount:
        maxcount=count
        maxword=word

print(maxword,maxcount)
