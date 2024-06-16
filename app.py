import random
import os
import jugadores
import funciones
from clases import Pueblo, Enemigo, Policia, Medico

while True:
    try:
        num_jugadores = int(input("¿Cuántos jugadores hay? "))
        if num_jugadores < 4 or num_jugadores > 10:
            print("Los jugadores deben ser mínimo 4 y máximo 10")
        else:
            break
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Agregar jugadores a la lista TODOS_LOS_JUGADORES
for i in range(num_jugadores):
    nombre = input(f"¿Cuál es el nombre del jugador {i+1}? ")
    jugadores.agregar_jugador(nombre)

# Seleccionar aleatoriamente Policía, Enemigo y Médico
jugadores_seleccionados = random.sample(jugadores.TODOS_LOS_JUGADORES, 3)
jugadores_seleccionados[0] = Policia(jugadores_seleccionados[0].nombre)
jugadores_seleccionados[1] = Enemigo(jugadores_seleccionados[1].nombre)
jugadores_seleccionados[2] = Medico(jugadores_seleccionados[2].nombre)

# Actualizar TODOS_LOS_JUGADORES con los jugadores seleccionados
for i in range(3):
    for j in range(num_jugadores):
        if jugadores.TODOS_LOS_JUGADORES[j].nombre == jugadores_seleccionados[i].nombre:
            jugadores.TODOS_LOS_JUGADORES[j] = jugadores_seleccionados[i]
            break

# Asignar Pueblo a los jugadores que no son Policía, Enemigo ni Médico
for i in range(len(jugadores.TODOS_LOS_JUGADORES)):
    if not isinstance(jugadores.TODOS_LOS_JUGADORES[i], (Policia, Enemigo, Medico)): 
        jugadores.TODOS_LOS_JUGADORES[i] = Pueblo(jugadores.TODOS_LOS_JUGADORES[i].nombre)

# Iniciar el juego
print("\nComienza el juego:")


while True:

    print("-----------------------------")

    if any((isinstance(jugador, (Pueblo, Medico))) and (jugador.estado == True) for jugador in jugadores.TODOS_LOS_JUGADORES): # si hay al menos 1 Medico / Pueblo y esta vivo
        
        if any((isinstance(ENE, Enemigo)) and (ENE.estado == True) for ENE in jugadores.TODOS_LOS_JUGADORES): # si el enemigo ESTÁ vivo
            print("\nEl enemigo aun esta vivo.")
        else:
            print("\nEl Enemigo ha muerto. El Pueblo gana.") # Enemigo muerto, no hay mas TURNOS
            break
        
        print("Quedan jugadores vivos.")
    
    else:
        print("\nTodo el pueblo ha muerto. Gana el Enemigo.") # todo Pueblo / Medico muerto, no hay mas TURNOS
        break


    # TURNOS
    
    # ENEMIGO
    print("\nTURNO DEL ENEMIGO")
    print("\nA qué jugador quiere eliminar:")
    funciones.estado_completo()

    while True:
        pedido = input("--> ")
        jugador_elegido = funciones.validar_elegido(pedido)

        if (jugador_elegido is not None) and (not isinstance(jugador_elegido, Enemigo)): # si el jugador existe y no es el enemigo lo elimina
            for E in jugadores.TODOS_LOS_JUGADORES:
                if isinstance(E, Enemigo):
                    os.system("cls")
                    E.eliminar(jugador_elegido)
                    break
            break
        else:
            print("Jugador no válido o muerto")


    # MEDICO
    print("\nTURNO DEL MEDICO")
    print("\nA qué jugador quiere salvar:")
    funciones.estado_completo()

    while True:
        pedido = input("--> ")
        jugador_elegido = funciones.validar_vivo(pedido)

        if jugador_elegido is not None:
            for M in jugadores.TODOS_LOS_JUGADORES:
                if isinstance(M, Medico):
                    os.system("cls")
                    M.salvar(jugador_elegido)
                    break
            break
        else:
            print("Jugador no válido o vivo")


    
    # POLICIA
    print("\nTURNO DEL POLICIA")


funciones.estado_completo()
print("\nTERMINÓ EL JUEGO")
