import random
""" 
JUEGO EL ASESINO
REGLAS:

"""

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = True # Vivo

class Pueblo(Jugador):
    def __init__(self):
        pass

class Enemigo(Jugador):
    def __init__(self,):
        pass

    def eliminar(self):
        # si elimina al policia o medico pierde el enemigo
        # sino puede eliminar
        print("Jugador eliminado")

class Policia(Jugador):
    def __init__(self,):
        pass

    def acusar():
        pass

class Medico(Jugador):
    def __init__(self,):
        pass

    def salvar():
        pass

Jugadores = int(input("¿ Cuantos jugadores hay ? ")) # que no pueda ingresar letras
while (Jugadores < 4):
    print("No hay suficientes jugadores, deben ser 4 o mas.")
    Jugadores = int(input("¿ Cuantos jugadores hay ? "))

for i in range(1,Jugadores+1):
    nombre_jugador = input("Cual es su nombre ? ")
    Jugador(nombre_jugador, True)

# def roles_aleatoriamente():

roles = [
    Enemigo(),
    Medico(),
    Policia(),
    Pueblo(),
]


def asignar_autos_aleatoriamente(jugadores, autos):
    autos_disponibles = autos[:]
    random.shuffle(autos_disponibles)
    
    for jugador in jugadores:
        if autos_disponibles:
            auto_asignado = autos_disponibles.pop()
            jugador.elegir_auto(auto_asignado)
        else:
            print(f"No hay suficientes autos para {jugador.nombre}.")

# Ejemplo de uso con las clases y el juego definido anteriormente
autos = [
    Auto("Auto Rojo", velocidad=10, durabilidad=100),
    Auto("Auto Azul", velocidad=8, durabilidad=120),
    Auto("Auto Verde", velocidad=9, durabilidad=110),
    Auto("Auto Amarillo", velocidad=7, durabilidad=130)
]

jugadores = [
    Jugador("Jugador 1"),
    Jugador("Jugador 2"),
    Jugador("Jugador 3"),
    Jugador("Jugador 4")
]

# Asignar autos aleatoriamente a los jugadores
asignar_autos_aleatoriamente(jugadores, autos)

# Inicializar pista
pista = Pista(distancia=100)

# Comenzar el juego
juego = Juego(jugadores, pista)
juego.jugar()