numero=0
total=0
while True:
    stringvalue= input('Ingrese el número :')
    if stringvalue == 'done' :
            break
    try:
        floatvalue= float(stringvalue)
    except:
        print('Entrada incorrecta')
        continue
    numero= numero+1
    total= total+floatvalue

print(total,numero,total/numero)
