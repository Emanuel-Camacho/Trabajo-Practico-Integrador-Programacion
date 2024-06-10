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

# Solicitar número de jugadores
while True:
    try:
        num_jugadores = int(input("¿Cuántos jugadores hay? "))
        if num_jugadores >= 4:
            break
        else:
            print("No hay suficientes jugadores, deben ser 4 o más.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Crear lista de nombres de jugadores
nombres_jugadores = []
for i in range(num_jugadores):
    nombre = input(f"Cual es el nombre del jugador {i+1}? ")
    nombres_jugadores.append(nombre)

# Asignar roles aleatoriamente
roles = [Enemigo, Medico, Policia] + [Pueblo] * (num_jugadores - 3)
random.shuffle(roles)

# Crear instancias de jugadores con roles asignados
jugadores = []
for i in range(num_jugadores):
    rol = roles[i]
    jugador = rol(nombres_jugadores[i])
    jugadores.append(jugador)

# Mostrar los roles asignados (puedes comentar esta parte para mantener los roles en secreto)
for jugador in jugadores:
    print(f"{jugador.nombre} es un {jugador.__class__.__name__}.")
