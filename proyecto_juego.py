# INICIO DEL JUEGO - BIENVENIDA
print("BIENVENIDO AL JUEGO DEL AHORCADO CON LA TERMINAL DE PYTHON\n ¿Estás preparado para comenzar?\n ¡A jugar! :D")

from random import choice      #importando este modulo se selecciona una plabra a partir de una lista de manera aleatoria
lista_de_palabras = ["ganador", "python", "programacion", "juego", "computador"]

letras_incorrectas = []
letras_correctas = []
intentos = 5
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_de_palabras): #Con esta funcion se va a eligir una palabra de forma aleatoria, esta será la palabra que el jugador deverá adivinar
    palabra_elegida = choice(lista_de_palabras)
    letras_unicas = len(set(palabra_elegida)) #Con el len sé la cantidad de letras y con el set, crea una lista de las letras sin repetir


    return palabra_elegida, letras_unicas

palabra = elegir_palabra(lista_de_palabras)
print(palabra)

def mostrar_nuevo_tablero(palabra_elegida):    #Esta función permite "ocultar" la palabra elegida al azar con guion bajo
    lista_oculta = []
    
    for l in palabra_elegida:  #recorremos la palabra 
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append("_")    

        
    print(lista_oculta) 

palabra_elegida, letras_unicas = elegir_palabra(lista_de_palabras)

mostrar_nuevo_tablero(palabra_elegida)


#while not juego_terminado: 
