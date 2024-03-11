import numpy as np

# Creamos el tablero

def colocacion_de_barcos(dimension_barco:int, tablero:np) -> np:
    '''
    Función que coloca números en un numpy array simulando barcos, cada fila o columna de numeros correspondera al numero de la dimension de 
    dicho barco solo para poder diferenciarlos, a efectos prácticos es indiferente.

    Restricciones:
    - Los barcos no pueden exceder los limites dimensionales del tablero, por lo que dependiendo de si la colocación es vertical u
    horizontal restaremos la dimensión a la fila o a la columna para cumplir con esta restricción.
    - Los barcos solo pueden ser colocados en espacios vacíos, por lo tanto creamos una variable lista que será una lista de boleanos obtenida de 
    comprobar si el espacio en el que queremos añadir el barco es igual a 0, comprobará cada uno de los espacios devolviendo True en caso de que
    sea 0 y devolvera False en caso de que encuentre algo distinto de 0. Si en la lista se encuentra al menos un False, volveremos a llamar a la
    función por recursividad hasta que esta restricción se cumpla, en caso contrario añadirá el barco, al tablero.

    La funcion devuelve el tablero obtenido como parametro pero con el nuevo barco añadido (el barco añadido tambien depende de la dimensión
    pasada como parametro)
    '''
    colocacion = np.random.choice(["horizontal", "vertical"])

    if colocacion == "horizontal": # Dependiendo se si es horizontal o vertical modificaremos la fila o la columna.
        columna = np.random.randint(10 - dimension_barco) 
        fila = np.random.randint(10) 
        lista = tablero[fila, columna:dimension_barco + columna] == 0  # lista es algo como: [ True False True True ... ]
        if False in lista: 
            return colocacion_de_barcos(dimension_barco, tablero) 

        else: 
            tablero[fila, columna:dimension_barco + columna] = dimension_barco # le damos el valor de la dimension para poder distinguir entre barcos y que todos sera de diferente tamaño
            return tablero

    elif colocacion == "vertical":
        fila = np.random.randint(10 - dimension_barco)
        columna = np.random.randint(10)  
        lista = tablero[fila:dimension_barco + fila, columna] == 0
        if False in lista:
            return colocacion_de_barcos(dimension_barco, tablero)
                 
        else:
            tablero[fila:dimension_barco + fila, columna] = dimension_barco
            return tablero
        
def creacion_de_tablero(barcos:list = [2,3,4,5,7]) -> np:
    '''
    Función que crea el tablero completo, la función crea un numpy array 10x10 de 0 y mediante un bucle vamos añadiendo barco por barco al
    tablero, las dimensiones de los barcos se pasan con una lista como argumento, que en este caso tiene un valor default de [2, 3, 4, 5, 7].

    Retorna el tablero ya comlpeto    
    '''

    tablero = np.full((10, 10), 0) 
    for i in barcos:
        tablero = colocacion_de_barcos(i, tablero) # Bucle que coloca todos los barcos
    return tablero

# Funciones de disparar

def disparar(tablero:np, tablero_de_aciertos:np) -> list:
    '''
    Función que actualizara el tablero si el usuario acierta. La función pedira al usuario que introduzca las coordenadas de donde quiere disparar,
    comprobará si en esa coordenada hay un 0,, si lo hay, significa que el usuario falló el intento, en caso contrario, es decir, cualquier numero distinto
    de 0, el usuario acertará y la función actualizara esa coordenada a 0.

    La función devolvera una lista, el primer elemento es el tablero que se va actualizando conforme el usuario acierta, y el segundo elemento
    es un registro de todos los disparos que hace el usuario, ambos se pasan como parametro a la función.

    En caso de error, mediante un try y except, repetiremos la función hasta que los inputs sean válidos
    '''

    try:
        coordenada_x = int(input("Introduzca la coordenada x de su disparo: "))
        coordenada_y = int(input("Introduzca la coordenada y de su disparo: "))
        if tablero[coordenada_y, coordenada_x] == 0:
            print("Falló")
            return [tablero, tablero_de_aciertos] # Dejamos un registro del tablero con las soluciones y el tablero con las respuestas del usuarios
        else:
            print("Acertó")
            tablero[coordenada_y, coordenada_x] = 0
            tablero_de_aciertos[coordenada_y, coordenada_x] = "X"
            return [tablero, tablero_de_aciertos] 
    except:
        return disparar(tablero, tablero_de_aciertos)




# Funcion del juego
# Funcion del juego

def hundir_la_flota():
    '''
    Función main del juego. La función crea por primera vez el tablero a adivinar y el tablero de registros, los cuales se irán actualizando en 
    cada vuelta de un bucle while, el bucle finalizará cuando el usuario hunda todos los barcos, ganando así el juego.

    En cada vuelta del bucle la función llamará a disparar() la cual devolverá una lista con dos numpy arrays, el primero es el tablero del juego 
    actualizado con el disparo del usuario y el segundo un tablero de registros actualizado que será impreso en cada vuelta del bucle para que 
    el usuario visualice en forma de X todas las veces que haya acertado en un disparo
    '''

    print("Bienvenido al juego de hundir la flota (las coordenadas a introducir empiezan por 0)")
    tablero = creacion_de_tablero() 
    tablero_registros = np.full((10, 10), "~")
    print(tablero)

    while True:    
        tableros = disparar(tablero, tablero_registros)
        tablero = tableros[0]
        tablero_registros = tableros[1] 
        print(tablero_registros)

        finalizado = tablero == 0 # Idem que en la funcion de colocar barcos, devuelve un numpy array de booleanos donde comprueba si todos los elementos de la matriz son 0
        if False not in finalizado: # Si existe algun false, significará que faltará algún punto por disparar.
            print("Ganaste, hundiste todos los barcos")
            return 
        
        
        
        

hundir_la_flota()