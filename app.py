# se debe separar el codigo en diferentes archivos para entrega final

import random

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
        if num_jugadores >= 4:
            break
        else:
            print("No hay suficientes jugadores, deben ser 4 o más.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

TODOS_LOS_JUGADORES = [] 
# lista que va a guardar a cada juagador y su nombre con la 'class jugador' para despues modificarla y dar los roles especificos 
for i in range(num_jugadores):
    nombre = input(f"¿Cuál es el nombre del jugador {i+1}? ")
    TODOS_LOS_JUGADORES.append(Jugador(nombre))

# seleccionar al azar a 3 jugadores de la lista TODOS_LOS_JUGADORES
jugadores_seleccionados = random.sample(TODOS_LOS_JUGADORES, 3)
jugadores_seleccionados[0] = Policia(jugadores_seleccionados[0].nombre)
jugadores_seleccionados[1] = Enemigo(jugadores_seleccionados[1].nombre)
jugadores_seleccionados[2] = Medico(jugadores_seleccionados[2].nombre)

# si alguno de los jugadores seleccionados conincide su nombre con alguno de la lista de TODOS_LOS_JUGADORES se actualiza su nombre por las dudas = ????? 
for i in range(3):
    for j in range(num_jugadores):
        if TODOS_LOS_JUGADORES[j].nombre == jugadores_seleccionados[i].nombre:
            TODOS_LOS_JUGADORES[j] = jugadores_seleccionados[i]
            break  # Salir del bucle una vez que se actualizó el jugador

# todos los que no fueron seleccionados son de 'class Pueblo'
for i in range(len(TODOS_LOS_JUGADORES)):
    if not isinstance(TODOS_LOS_JUGADORES[i], (Policia, Enemigo, Medico)): 
        # si TODOS_LOS_JUGADORES[i] (un jugador) no es (not) Policia, Enemigo o Medico lo hace Pueblo
        TODOS_LOS_JUGADORES[i] = Pueblo(TODOS_LOS_JUGADORES[i].nombre)

# muestra nombre y roles de cada jugador 
# sacar para entrega final
for jugador in TODOS_LOS_JUGADORES:
    print(f"Jugador: {jugador.nombre}, Estado: {'Vivo' if jugador.estado else 'Muerto'}, Rol: {jugador.__class__.__name__}")

""" # EMPIEZA EL JUEGO
while True:
    for i in range(len(TODOS_LOS_JUGADORES)):
        if isinstance(TODOS_LOS_JUGADORES[i], (Pueblo)):
            print("")
        else:
            # comprobar si enemigo esta vivo o muerto
            print("") """