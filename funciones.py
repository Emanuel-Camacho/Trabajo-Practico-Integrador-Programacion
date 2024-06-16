from clases import Jugador, Pueblo, Enemigo, Policia, Medico
from jugadores import TODOS_LOS_JUGADORES  

def validar_elegido(pedido):
    for jugador in TODOS_LOS_JUGADORES:
        if ((jugador.nombre == pedido) and (jugador.estado == True)):
            return jugador
    return None

def validar_vivo(pedido):
    for jugador in TODOS_LOS_JUGADORES:
        if (jugador.nombre == pedido):
            return jugador
    return None

def estado_completo():
    print("\nEstado de los jugadores:")
    # Mostrar estado inicial de todos los jugadores
    for jugador in TODOS_LOS_JUGADORES:
        print(f"Jugador: {jugador.nombre}, Estado: {'Vivo' if jugador.estado else 'Muerto'}, Rol: {jugador.__class__.__name__}")

def estado_jugadores():
    print("\nEstado de los jugadores:")
    # Mostrar estado inicial de todos los jugadores
    for jugador in TODOS_LOS_JUGADORES:
        print(f"Jugador: {jugador.nombre}")

