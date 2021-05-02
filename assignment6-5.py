text = 'X-DSPAM-Confidence:    0.8475'
slicingpartone= text.find('0')
slicingparttwo= text.find('5')
finaltext=text[slicingpartone:slicingparttwo+1]
floatvalue=float(finaltext)
print(floatvalue)

'''
Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
 Convert the extracted value to a floating point number and print it out.
'''


'''
otra forma


text = 'X-DSPAM-Confidence:    0.8475'
slicing= text.find(':')
finaltext=text[slicing+5:]
floatvalue=float(finaltext)
print(floatvalue)
'''
