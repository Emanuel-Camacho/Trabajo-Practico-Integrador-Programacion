class Jugador:
    # comodin = 1
    def __init__(self, nombre):
        self.nombre = str(nombre)
        self.estado = True  # Vivo

class Pueblo(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

class Enemigo(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def eliminar(self, jugador):
        if isinstance(jugador, Policia):
            print(f"{self.__class__.__name__} ha perdido por querer eliminar a un {jugador.__class__.__name__}.")
            self.estado = False
        else:
            print(f"{jugador.__class__.__name__} ha sido eliminado por el Enemigo.")
            jugador.estado = False

class Policia(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def acusar(self, jugador):
        if isinstance(jugador, Enemigo):
            print(f"{self.__class__.__name__} ha acusado correctamente a {jugador.nombre} ({jugador.__class__.__name__}).")
            jugador.estado = False
        else:
            print(f"{self.__class__.__name__} ha acusado incorrectamente a {jugador.__class__.__name__}.")

class Medico(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def salvar(self, jugador):
        if not jugador.estado:
            jugador.estado = True
            print(f"{self.__class__.__name__} ha salvado a alguien.")
        else:
            print(f"{self.__class__.__name__} no necesita salvar a ese jugador porque ya está vivo.")
