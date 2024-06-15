from clases import Jugador, Pueblo, Enemigo, Policia, Medico

TODOS_LOS_JUGADORES = []

def mostrar_vivos():
    vivos = []
    for jugador in TODOS_LOS_JUGADORES:
        if jugador.estado:
            vivos.append(jugador.nombre)
    return vivos

def quedan_vivos():
    return any(isinstance(jugador, (Pueblo, Medico)) and jugador.estado for jugador in TODOS_LOS_JUGADORES)
