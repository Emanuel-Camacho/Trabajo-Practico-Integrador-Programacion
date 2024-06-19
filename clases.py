class Jugador:
    # comodin = 1
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._estado = True  # Vivo

    @property
    def mostrar_nombre(self):
        return self._nombre

    @property
    def cambio_estado(self):
        return self._estado

    @cambio_estado.setter
    def cambio_estado(self, estado_nuevo):
        self._estado = estado_nuevo

class Pueblo(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

class Enemigo(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def eliminar(self, jugador):
        if isinstance(jugador, Policia):
            print(f"{self.__class__.__name__} ha perdido por querer eliminar a un {jugador.__class__.__name__}.")
            self._estado = False
        else:
            print(f"{jugador.__class__.__name__} ha sido eliminado por el Enemigo.")
            jugador._estado = False

class Policia(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def acusar(self, jugador):
        if isinstance(jugador, Enemigo):
            print(f"{self.__class__.__name__} ha acusado correctamente a {jugador._nombre} ({jugador.__class__.__name__}).")
            jugador._estado = False
        else:
            print(f"{self.__class__.__name__} ha acusado incorrectamente a {jugador.__class__.__name__}.")

class Medico(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def salvar(self, jugador):
        if not jugador._estado:
            jugador._estado = True
            print(f"{self.__class__.__name__} ha salvado a alguien.")
        else:
            print(f"{self.__class__.__name__} no necesita salvar a ese jugador porque ya está vivo.")
    