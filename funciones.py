import jugadores
from jugadores import TODOS_LOS_JUGADORES, mostrar_vivos, quedan_vivos
from clases import Jugador, Pueblo, Enemigo, Policia, Medico

def restantes():
    for i in range(len(jugadores.TODOS_LOS_JUGADORES)):
        if isinstance(jugadores.TODOS_LOS_JUGADORES[i], (Medico, Pueblo)):
            if jugadores.TODOS_LOS_JUGADORES[i].estado == True:
                print(f"{jugadores.TODOS_LOS_JUGADORES[i].__class__.__name__} VIVO , Nombre {jugadores.TODOS_LOS_JUGADORES[i].nombre}")

