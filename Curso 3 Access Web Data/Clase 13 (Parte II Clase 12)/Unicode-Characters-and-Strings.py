#The ord() function tell us the numeric value of a simple ASCII character

print (ord('H'))

#Retrieving web pages

import urllib.request, urllib.parse, urllib.error

filehandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in filehandle:
    print(line.decode().strip())

#Like a file.. para que funcione debe comentar las lineas del for anterior

counts= dict()
for line2 in filehandle:
    words= line2.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

#Reading web pages
fhand= urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
