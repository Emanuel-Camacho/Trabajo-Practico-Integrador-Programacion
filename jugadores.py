from clases import Jugador, Pueblo, Enemigo, Policia, Medico
import random


TODOS_LOS_JUGADORES = []

# el jugador que se agrega es de class Jugador
def agregar_jugador(nombre):
    TODOS_LOS_JUGADORES.append(Jugador(nombre))

# en la lista TODOS_LOS_JUGADORES se asignan los roles automaticamente y de forma aleatoria
def roles_automaticos(num_jugadores):
    # Seleccionar aleatoriamente Policía, Enemigo y Médico
    jugadores_seleccionados = random.sample(TODOS_LOS_JUGADORES, 3)
    jugadores_seleccionados[0] = Policia(jugadores_seleccionados[0]._nombre)
    jugadores_seleccionados[1] = Enemigo(jugadores_seleccionados[1]._nombre)
    jugadores_seleccionados[2] = Medico(jugadores_seleccionados[2]._nombre)

    # Actualizar TODOS_LOS_JUGADORES con los jugadores seleccionados
    for i in range(3):
        for j in range(num_jugadores):
            if TODOS_LOS_JUGADORES[j]._nombre == jugadores_seleccionados[i]._nombre:
                TODOS_LOS_JUGADORES[j] = jugadores_seleccionados[i]
                break

    # Asignar Pueblo a los jugadores que no son Policía, Enemigo ni Médico
    for i in range(len(TODOS_LOS_JUGADORES)):
        if not isinstance(TODOS_LOS_JUGADORES[i], (Policia, Enemigo, Medico)): 
            TODOS_LOS_JUGADORES[i] = Pueblo(TODOS_LOS_JUGADORES[i]._nombre)
