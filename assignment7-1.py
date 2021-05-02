# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
input1=fh.read()  #lee el archivo
input2= input1.upper() #Pone todo el texto en mayúscula
input3=input2.rstrip() #elimina los espacios en blanco
print(input3)

'''
 7.1 Write a program that prompts for a file name, then opens that file and reads through the file,
 and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
'''
