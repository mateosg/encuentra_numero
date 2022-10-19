from pip import main


def encuentra_numero(txt):
    '''
    Dado un texto, devuelve todos los números enteros (sin signo) que encuentre. Dichos números pueden tener un número
    indeterminado de dígitos
    '''
    numeroTxt=''
    numeros=[]
    i=0
    while i<len(txt):
        if txt[i].isdigit():
            while i<len(txt) and txt[i].isdigit():
                numeroTxt+=txt[i]
                i+=1
            numeros.append(int(numeroTxt))
            numeroTxt=''
        i+=1

    return numeros

################### prueba ##################
if __name__ == '__main__':
    print(encuentra_numero('hola 123 456 78adsf9 adios'))   

    