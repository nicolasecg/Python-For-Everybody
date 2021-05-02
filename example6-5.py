text = 'X-DSPAM-Confidence:    0.8475'
slicingpartone= text.find('0')
slicingparttwo= text.find('5')
finaltext=text[slicingpartone:slicingparttwo+1]
print(finaltext)
'''
se hicieron varias pruebas con este ejemplo
'''
