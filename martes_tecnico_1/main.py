# Construir un programa que cuente la cantidad de palabras de una frase. 
# Por ejemplo, si se le ingresa la frase "desarrollar software es lo mejor que me pasó",
# la salida del programa debería ser 8.

def contadorPalabras(frase):
    fraseArr = frase.split(" ")
    longitud = len(fraseArr)
    return longitud

def testContadorPalabras():
    assert contadorPalabras("desarrollar software es lo mejor que me pasó") == 8, "Deberia ser 8"
    assert contadorPalabras("messi capo") == 2, "Deberia ser 2"
    print("todo salio bien")
    

testContadorPalabras()