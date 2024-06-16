from clases import Jugador, Pueblo, Enemigo, Policia, Medico


TODOS_LOS_JUGADORES = []

def agregar_jugador(nombre):
    TODOS_LOS_JUGADORES.append(Jugador(nombre))

