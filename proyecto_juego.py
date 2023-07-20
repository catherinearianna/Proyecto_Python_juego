# INICIO DEL JUEGO - BIENVENIDA
print("BIENVENIDO/A AL JUEGO DEL AHORCADO CON LA TERMINAL DE PYTHON\n ¿Estás preparado para comenzar?\n ¡A jugar! :D")

from random import choice      #importando este modulo se selecciona una palabra a partir de una lista de manera aleatoria
palabras = ["musica", "luna", "verano", "mesa", "playa"] #lista de palabras a adivinar 

letras_incorrectas = []
letras_correctas = []
intentos = 5
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_de_palabras): #Con esta funcion se va a eligir una palabra de forma aleatoria, esta será la palabra que el jugador deverá adivinar
    palabra_elegida = choice(lista_de_palabras)
    letras_unicas = len(set(palabra_elegida)) #Con el len sé la cantidad de letras y con el set, crea una lista de las letras sin repetir


    return palabra_elegida, letras_unicas

palabra = elegir_palabra(palabras)


def mostrar_nuevo_tablero(palabra_elegida):    #Esta función permite "ocultar" la palabra elegida al azar con guion bajo
    lista_oculta = []                          #Por cada letra de palabra_elegida voy a revisar si ya fue descubierta, en caso que así lo sea, muestro la letra, caso contrario muestro un guión bajo. 
    
    for l in palabra_elegida:  #recorremos la palabra 
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append("_")    

        
    print(lista_oculta) 

palabra_elegida, letras_unicas = elegir_palabra(palabras)


def pedir_letra():
    global intentos #al agregar "global" a la variable dentro de la funcion, hace que la variable haga referencia al valor definido de forma global (linea 9, "intentos = 5") 
    global aciertos
    '''
    Esta función se encarga de pedir una letra al jugador.
    También debe validar si la letra ingresada es valida(pertenezca al abecedario y que esté ingresando solo UNA letra)
    '''
    letra_usuario = input("Ingrese una letra: ")
    if len(letra_usuario) == 1 and letra_usuario.isalpha():    #Devuelve True si la cadena es alfabética, de lo contrario False
         if letra_usuario in palabra_elegida:
            letras_correctas.append(letra_usuario)
            aciertos +=1
         else:
             letras_incorrectas.append(letra_usuario)
             intentos-=1
    else: 
         print("ERROR, tiene que ser UNA letra y debe estar dentro del abecedario.\nIntente de nuevo.") 
         
    
def validar_ganador(palabra, letras_correctas):  #Esta función valida si cada una de las letras de la palabra_elegida esta dentro de la lista de letras_correctas
    encontradoTodasLasLetras = True              
    for i in range(len(palabra)):
        if(palabra[i] not in letras_correctas):  #Este if hace que: si la letra de la palabra_elegida NO esta dentro de la lista letras_correctas setea la variable en encontradoTodas las letras en False, y salgo de la funcion con el break
            encontradoTodasLasLetras = False
            break
    return encontradoTodasLasLetras

while not juego_terminado:    #Con el while ejecuto todas las funciones previamente ya armadas para que se muestren en el orden que necesito. 
    
    mostrar_nuevo_tablero(palabra_elegida)
    print("Estas son las letras incorrectas", letras_incorrectas)
    print("¡Atento, te quedan ", intentos, " intentos!")
    pedir_letra()
   
    if intentos == 0:
        juego_terminado = True
        print("¡AHORCADO! :(")

    ganador = validar_ganador(palabra_elegida, letras_correctas)

    if(ganador):
        print("¡EN HORA BUENA, HAS GANADO! :D ")
        juego_terminado = True

   
    

