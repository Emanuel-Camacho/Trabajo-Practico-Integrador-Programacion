class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = True

class Pueblo(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

class Enemigo(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def eliminar(self, jugador):
        if isinstance(jugador, Policia) or isinstance(jugador, Medico):
            print(f"{self.nombre} (Enemigo) ha perdido por eliminar a un {jugador.__class__.__name__}.")
        else:
            print(f"{self.nombre} (Enemigo) ha eliminado a {jugador.nombre}.")
            jugador.estado = False

class Policia(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def acusar(self, jugador):
        if isinstance(jugador, Enemigo):
            print(f"{self.nombre} (Policia) ha acusado correctamente a {jugador.nombre} (Enemigo).")
        else:
            print(f"{self.nombre} (Policia) ha acusado incorrectamente a {jugador.nombre} ({jugador.__class__.__name__}).")

class Medico(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def salvar(self, jugador):
        if not jugador.estado:
            jugador.estado = True
            print(f"{self.nombre} (Medico) ha salvado a {jugador.nombre}.")
        else:
            print(f"{self.nombre} (Medico) no necesita salvar a {jugador.nombre}, ya está vivo.")
