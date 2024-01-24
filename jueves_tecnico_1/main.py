# Dada una frase, devolver en un arreglo todas las palabras que tienen la misma
# longitud que la mas corta de la frase.

#Ejemplo:
#"que lindo dia de sol en san antonio de areco no hay nuber en el cielo"

#de, en, no, el

def transformarTexto(frase):
    fraseFinal = frase.lower()
    fraseFinal = fraseFinal.replace(",", "")
    fraseFinal = fraseFinal.replace(".", "")

    return fraseFinal

def obtenerLogitudMasCorta(arreglo):
  longitudMasCorta = len(arreglo[0])
  for palabra in arreglo:
      if (len(palabra) < longitudMasCorta):
          longitudMasCorta = len(palabra)
    
  return longitudMasCorta

def obtenerPalabrasCortas(frase):
    fraseFinal = transformarTexto(frase)
    fraseArreglo = fraseFinal.split(" ")
    
    longitudMasCorta = obtenerLogitudMasCorta(fraseArreglo)

    listaPalabrasCortas = []

    for palabra in fraseArreglo:
        if ((len(palabra) == longitudMasCorta) and (palabra not in listaPalabrasCortas)):
            listaPalabrasCortas.append(palabra)
    
    return listaPalabrasCortas

def testTransformadorDeTexto():
    assert transformarTexto('QuE lindo dia de sol en .san, antonio de areco no hay nuber en el cielo') == 'que lindo dia de sol en san antonio de areco no hay nuber en el cielo', "Error: no se obtuvo el resultado esperado"
    assert transformarTexto('Sé el cambio que quieres ver en el mundo') == 'sé el cambio que quieres ver en el mundo', "Error: no se obtuvo el resultado esperado"
    
    print("Todas las pruebas pasaron correctamente")

#Para testear el transformador de textos
testTransformadorDeTexto()

def testPalabrasCortas():
    assert obtenerPalabrasCortas('que lindo dia de sol en san antonio de areco no hay nuber en el cielo') == ['de', 'en', 'no', 'el'], "Error: no se obtuvo el resultado esperado"
    assert obtenerPalabrasCortas('QuE lindo dia de sol en .san, antonio de areco no hay nuber en el cielo') == ['de', 'en', 'no', 'el'], "Error: no se obtuvo el resultado esperado"
    assert obtenerPalabrasCortas('Sé el cambio que quieres ver en el mundo') == ['sé', 'el', 'en'], "Error: no se obtuvo el resultado esperado"
    
    print("Todas las pruebas pasaron correctamente")

#Para testear la función que devuelve el arreglo de las palabras más cortas
testPalabrasCortas()