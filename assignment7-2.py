# Use the file name mbox-short.txt as the file name
filename = input("Enter file name: ")
filehandle = open(filename)
n=0
count=0
for line in filehandle:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count=count+float(line[20:26])
    n=n+1
    #print(line)
    #print(count)
    #print(n)
print("Average spam confidence:",count/n)

'''
 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce
an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt
as the file name.
'''
