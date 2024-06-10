"""

Juego: Aventura en el Bosque
En este juego, tendrás cuatro clases principales:

Jugador
Enemigo
Objeto
Juego
Código:
python
"""

import random

class Jugador:

    def _init_(self, nombre):
        self.nombre = nombre
        self.salud = 100
        self.ataque = 10
        self.inventario = []

    def atacar(self, enemigo):
        dano = random.randint(5, self.ataque)
        enemigo.salud -= dano
        print(f"{self.nombre} ataca a {enemigo.nombre} y le causa {dano} de daño.")

    def recoger_objeto(self, objeto):
        self.inventario.append(objeto)
        print(f"{self.nombre} recoge un {objeto.nombre}.")

    def usar_objeto(self, objeto_nombre):
        for objeto in self.inventario:
            if objeto.nombre == objeto_nombre:
                objeto.usar(self)
                self.inventario.remove(objeto)
                break

class Enemigo:
    def _init_(self, nombre, salud, ataque):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque

    def atacar(self, jugador):
        dano = random.randint(5, self.ataque)
        jugador.salud -= dano
        print(f"{self.nombre} ataca a {jugador.nombre} y le causa {dano} de daño.")

class Objeto:
    def _init_(self, nombre, tipo, valor):
        self.nombre = nombre
        self.tipo = tipo
        self.valor = valor

    def usar(self, jugador):
        if self.tipo == "salud":
            jugador.salud += self.valor
            print(f"{jugador.nombre} usa {self.nombre} y recupera {self.valor} de salud.")
        elif self.tipo == "ataque":
            jugador.ataque += self.valor
            print(f"{jugador.nombre} usa {self.nombre} y gana {self.valor} de ataque.")

class Juego:
    def _init_(self, jugador):
        self.jugador = jugador
        self.enemigos = [
            Enemigo("Lobo", 30, 8),
            Enemigo("Ogro", 50, 12)
        ]
        self.objetos = [
            Objeto("Poción de Salud", "salud", 20),
            Objeto("Espada Mágica", "ataque", 5)
        ]
        self.ejecutando = True

    def encontrar_objeto(self):
        objeto = random.choice(self.objetos)
        print(f"Encuentras un {objeto.nombre}.")
        self.jugador.recoger_objeto(objeto)

    def encontrar_enemigo(self):
        enemigo = random.choice(self.enemigos)
        print(f"Un {enemigo.nombre} aparece.")
        while enemigo.salud > 0 and self.jugador.salud > 0:
            accion = input("¿Qué deseas hacer? (atacar/usar objeto/huir): ").lower()
            if accion == "atacar":
                self.jugador.atacar(enemigo)
                if enemigo.salud > 0:
                    enemigo.atacar(self.jugador)
            elif accion == "usar objeto":
                objeto_nombre = input("¿Qué objeto deseas usar?: ")
                self.jugador.usar_objeto(objeto_nombre)
            elif accion == "huir":
                print("Huyes del enemigo.")
                break
            else:
                print("Acción no válida.")
        if self.jugador.salud <= 0:
            print("Has sido derrotado.")
            self.ejecutando = False
        elif enemigo.salud <= 0:
            print(f"Has derrotado al {enemigo.nombre}.")

    def jugar(self):
        print(f"Bienvenido, {self.jugador.nombre}, a la Aventura en el Bosque.")
        while self.ejecutando:
            accion = input("¿Qué deseas hacer? (explorar/salir): ").lower()
            if accion == "explorar":
                evento = random.choice(["enemigo", "objeto"])
                if evento == "enemigo":
                    self.encontrar_enemigo()
                elif evento == "objeto":
                    self.encontrar_objeto()
            elif accion == "salir":
                print("Gracias por jugar. ¡Hasta la próxima!")
                self.ejecutando = False
            else:
                print("Acción no válida.")

# Inicializar el juego
nombre_jugador = input("Ingresa tu nombre: ")
jugador = Jugador(nombre_jugador)
juego = Juego(jugador)
juego.jugar()
""" 
Descripción de las Clases
Jugador:

Atributos: nombre, salud, ataque, inventario
Métodos: atacar, recoger_objeto, usar_objeto
Enemigo:

Atributos: nombre, salud, ataque
Métodos: atacar
Objeto:

Atributos: nombre, tipo, valor
Métodos: usar
Juego:

Atributos: jugador, enemigos, objetos, ejecutando
Métodos: encontrar_objeto, encontrar_enemigo, jugar
Funcionamiento del Juego
El jugador puede explorar el bosque y encontrarse con enemigos o encontrar objetos.
El jugador puede atacar a los enemigos o usar objetos para mejorar sus atributos.
El juego termina cuando el jugador decide salir o si su salud llega a cero. """