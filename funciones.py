from clases import Jugador, Pueblo, Enemigo, Policia, Medico
from jugadores import TODOS_LOS_JUGADORES 
import random 

def validar_existe(pedido):
    for jugador in TODOS_LOS_JUGADORES:
        if (jugador._nombre == pedido):
            return jugador
    return None

def estado_completo():
    print("\nEstado completo de los jugadores:")
    for jugador in TODOS_LOS_JUGADORES:
        print(f"Jugador: {jugador._nombre}, Estado: {'Vivo' if jugador._estado else 'Muerto'}, Rol: {jugador.__class__.__name__}")

def estado_enemigo():
    for jugador in TODOS_LOS_JUGADORES:
        print(f"Jugador: {jugador._nombre} {"Muerto" if not jugador._estado else ""}{"Enemigo" if isinstance(jugador, Enemigo) else ""}")

def estado_medico():
    eliminados = 0
    for jugador in TODOS_LOS_JUGADORES:
        if jugador._estado == False:
            eliminados += 1
    print(f"\nMuertos: {eliminados}\n")
    for jugador in TODOS_LOS_JUGADORES:
        print(f"Jugador: {jugador._nombre} {"Medico" if isinstance(jugador, Medico) else ""}")

def estado_policia():
    print("\nEstado de los jugadores:")
    for jugador in TODOS_LOS_JUGADORES:
        print(f"Jugador: {jugador._nombre}, Estado: {'Vivo' if jugador._estado else 'Muerto'} {"Policia" if isinstance(jugador, Policia) else ""}")

def muertos():
    desorden = TODOS_LOS_JUGADORES.copy()
    random.shuffle(desorden)
    for jugador in desorden:
        if jugador._estado == False:
            print(f"{jugador.__class__.__name__} esta muerto")
        else:
            print(f"{jugador.__class__.__name__} esta vivo")


