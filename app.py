import random
import funciones
import jugadores

# Clase base Jugador
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = True  # Vivo

# Clase Pueblo
class Pueblo(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

# Clase Enemigo
class Enemigo(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def eliminar(self, jugador):
        if isinstance(jugador, Policia) or isinstance(jugador, Medico):
            print(f"{self.nombre} (Enemigo) ha perdido por eliminar a un {jugador.__class__.__name__}.")
        else:
            print(f"{self.nombre} (Enemigo) ha eliminado a {jugador.nombre}.")
            jugador.estado = False

# Clase Policia
class Policia(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def acusar(self, jugador):
        if isinstance(jugador, Enemigo):
            print(f"{self.nombre} (Policia) ha acusado correctamente a {jugador.nombre} (Enemigo).")
        else:
            print(f"{self.nombre} (Policia) ha acusado incorrectamente a {jugador.nombre} ({jugador.__class__.__name__}).")

# Clase Medico
class Medico(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def salvar(self, jugador):
        if not jugador.estado:
            jugador.estado = True
            print(f"{self.nombre} (Medico) ha salvado a {jugador.nombre}.")
        else:
            print(f"{self.nombre} (Medico) no necesita salvar a {jugador.nombre}, ya está vivo.")

# MAIN
while True:
    try:
        num_jugadores = int(input("¿Cuántos jugadores hay? "))
        if num_jugadores <= 4 or num_jugadores > 10:
            print("Los jugadores deben ser mínimo 4 y máximo 10")
        else:
            break
    except ValueError:
        print("Por favor, ingrese un número válido.")

# lista que va a guardar a cada jugador y su nombre con la 'class jugador' para después modificarla y dar los roles específicos 
for i in range(num_jugadores):
    nombre = input(f"¿Cuál es el nombre del jugador {i+1}? ")
    jugadores.TODOS_LOS_JUGADORES.append(Jugador(nombre))

# seleccionar al azar a 3 jugadores de la lista TODOS_LOS_JUGADORES
jugadores_seleccionados = random.sample(jugadores.TODOS_LOS_JUGADORES, 3)
jugadores_seleccionados[0] = Policia(jugadores_seleccionados[0].nombre)
jugadores_seleccionados[1] = Enemigo(jugadores_seleccionados[1].nombre)
jugadores_seleccionados[2] = Medico(jugadores_seleccionados[2].nombre)

# si alguno de los jugadores seleccionados coincide su nombre con alguno de la lista de TODOS_LOS_JUGADORES se actualiza su nombre por las dudas
for i in range(3):
    for j in range(num_jugadores):
        if jugadores.TODOS_LOS_JUGADORES[j].nombre == jugadores_seleccionados[i].nombre:
            jugadores.TODOS_LOS_JUGADORES[j] = jugadores_seleccionados[i]
            break  # Salir del bucle una vez que se actualizó el jugador

# todos los que no fueron seleccionados son de 'class Pueblo'
for i in range(len(jugadores.TODOS_LOS_JUGADORES)):
    if not isinstance(jugadores.TODOS_LOS_JUGADORES[i], (Policia, Enemigo, Medico)): 
        # si TODOS_LOS_JUGADORES[i] (un jugador) no es (not) Policia, Enemigo o Medico lo hace Pueblo
        jugadores.TODOS_LOS_JUGADORES[i] = Pueblo(jugadores.TODOS_LOS_JUGADORES[i].nombre)

# muestra nombre y roles de cada jugador
# quitar para entrega final
print("\n")
for jugador in jugadores.TODOS_LOS_JUGADORES:
    print(f"Jugador: {jugador.nombre}, Estado: {'Vivo' if jugador.estado else 'Muerto'}, Rol: {jugador.__class__.__name__}")

print("\n")

# EMPIEZA EL JUEGO
while True:

    for i in range(len(jugadores.TODOS_LOS_JUGADORES)):
    
        if isinstance(jugadores.TODOS_LOS_JUGADORES[i], (Pueblo, Medico)): 
            if jugadores.TODOS_LOS_JUGADORES[i].estado == True: # si pueblo/medico sigue vivo
                
                for j in range(len(jugadores.TODOS_LOS_JUGADORES)): 
                    if isinstance(jugadores.TODOS_LOS_JUGADORES[j], (Enemigo)): # si enemigo sigue vivo 
                        if jugadores.TODOS_LOS_JUGADORES[j].estado == True:

                            # JUEGO / TURNOS ENEMIGO - MEDICO - POLICIA
                            print("Turno del enemigo")
                            print("A qué jugador quiere eliminar\n")
                            print(funciones.restantes())
                            
                            elegido = input()

                            break
            else:
                print(f"Jugador: {jugadores.TODOS_LOS_JUGADORES[i].nombre}, {jugadores.TODOS_LOS_JUGADORES[i].__class__.__name__} Muerto")
    
        else: # comprueba si el enemigo está vivo
            if isinstance(jugadores.TODOS_LOS_JUGADORES[i], (Enemigo)):
                if jugadores.TODOS_LOS_JUGADORES[i].estado == True:
                    print(f"{jugadores.TODOS_LOS_JUGADORES[i].__class__.__name__} Vivo")
                    # comprobar si quedan pueblos vivos si sí ganan si no pierden
                else:
                    print(f"{jugadores.TODOS_LOS_JUGADORES[i].__class__.__name__} Muerto")
                    # comprobar si quedan pueblos vivos si sí ganan si no pierden
                    break
        if isinstance(jugadores.TODOS_LOS_JUGADORES[i], (Policia)):
            print(f"{jugadores.TODOS_LOS_JUGADORES[i].__class__.__name__} Vivo")
    break

print("\nTERMINÓ EL JUEGO")
