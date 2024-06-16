import random
import os
import jugadores
import funciones
from clases import Pueblo, Enemigo, Policia, Medico

# REGLAS
print("\nBienvenidos al Juego de Mafia por Roles")
input("\nPresione enter para continuar...")

os.system("cls")

print("\nREGLAS")
print("\n1. Debe haber minimo 4 jugadores (Pueblo, Enemigo, Policia y Medico) y maximo 10")
print("2. Solo puede haber 1 Enemigo, Policia y Medico.")
print("3. El Enemigo gana si elimina a todos.")
print("4. El Enemigo no puede eliminar al policia.")
print("5. El medico puede salvar a cualquie jugador, menos al enemigo")
print("6. Si el Medico muere puede salvarse a si mismo")
print("7. El polica puede acusar a cualquier jugador")
# print("8. Cada Rol puede activar un comodin 1 sola vez ingresando '0'")

input("\nPresione enter para comenzar a jugar...")

os.system("cls")

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

# Asigna 1 Enemigo, Policia, Medico y los demas Pueblo
jugadores.roles_automaticos(num_jugadores)

os.system("cls")

# Inicia el juego
print("\nComienza el juego:")

posible = True
while True:

    if any((isinstance(jugador, (Pueblo, Medico))) and (jugador.estado == True) for jugador in jugadores.TODOS_LOS_JUGADORES): # si hay al menos 1 Medico / Pueblo y esta vivo el juego sigue
        
        if any((isinstance(ENE, Enemigo)) and (ENE.estado == True) for ENE in jugadores.TODOS_LOS_JUGADORES): # si el enemigo ESTÁ vivo el juego sigue
            pass
        else:
            print("\nEl Enemigo ha muerto. El Pueblo gana.") # Enemigo muerto, no hay mas TURNOS
            break
    
    else:
        print("\nTodo el pueblo ha muerto. Gana el Enemigo.") # Pueblo / Medico muerto, no hay mas TURNOS
        break

    # TURNOS
    
    # ENEMIGO
    print("\nTURNO DEL ENEMIGO")
    print("\nA qué jugador quiere eliminar:")
    funciones.estado_enemigo()

    while True:
        pedido = input("--> ")
        jugador_elegido = funciones.validar_existe(pedido)

        if (jugador_elegido is not None) and (not isinstance(jugador_elegido, Enemigo)): # si el jugador existe y no es el enemigo lo elimina
            if jugador_elegido.estado is True: 
                for E in jugadores.TODOS_LOS_JUGADORES:
                    if isinstance(E, Enemigo):
                        os.system("cls")
                        E.eliminar(jugador_elegido)
                        break
                break
            else:
                os.system("cls")
                print("Jugador muerto")
                break
        else:
            print("Jugador no válido")


    #validar si enemigo esta vivo o muerto
    if any(isinstance(jugador,Enemigo) and jugador.estado == True for jugador in jugadores.TODOS_LOS_JUGADORES):

    # MEDICO
        if posible == True: 
            print("\nTURNO DEL MEDICO")
            print("\nA qué jugador quiere salvar:")
            funciones.estado_medico()

            while True:
                pedido = input("--> ")
                jugador_elegido = funciones.validar_existe(pedido)
                
                if jugador_elegido is not None:
                    for M in jugadores.TODOS_LOS_JUGADORES:
                        if isinstance(M, Medico): # 2 lineas para encontrar y seleccioanar al medico

                            # si el elegido es el Medico y esta muerto se salva el mismo
                            if isinstance(jugador_elegido, Medico) and jugador_elegido.estado == False:
                                os.system("cls")
                                M.salvar(jugador_elegido)
                                break

                            # si el elegido no es el medico y el medico esta muerto
                            elif not isinstance(jugador_elegido, Medico) and any((isinstance(jugador, Medico)) and (jugador.estado == False) for jugador in jugadores.TODOS_LOS_JUGADORES):
                                os.system("cls")
                                print("El Medico no puede salvar a nadie porque esta muerto")
                                posible = False
                                break
                            
                            # si el elegido no es el medico y el medico esta vivo el elegido se salva
                            elif not isinstance(jugador_elegido, Medico) and any((isinstance(jugador, Medico)) and (jugador.estado == True) for jugador in jugadores.TODOS_LOS_JUGADORES): 
                                os.system("cls")
                                M.salvar(jugador_elegido)
                                break

                            # si el elegido es el medico y esta vivo se "salva"
                            else:
                                os.system("cls")
                                M.salvar(jugador_elegido)
                                break
                    break
                else:
                    print("Jugador no válido")
        else:
            print("El Medico esta muerto")
        
        # POLICIA
        print("\nTURNO DEL POLICIA")
        print("Quiere acusar a alguien ?\nS / N")

        while True:

            pedido = str(input("--> "))

            if pedido.upper() == "S":
                print("\nA quien quiere acusar:")
                funciones.estado_policia()
                
                pedido = str(input("--> "))
                jugador_elegido = funciones.validar_existe(pedido)

                if jugador_elegido is not None:
                    for P in jugadores.TODOS_LOS_JUGADORES:
                        if isinstance(P, Policia):
                            os.system("cls")
                            P.acusar(jugador_elegido)
                            break
                    break
                else:
                    print("Jugador no válido o vivo")
                break

            elif (pedido.upper() != "S") and (pedido.upper() != "N"):
                print("Opcion equivocada")
            else:
                os.system("cls")
                print("El Policia no acuso a nadie.")
                break
    else:
        pass
    




funciones.estado_completo()
print("\nTERMINÓ EL JUEGO")
