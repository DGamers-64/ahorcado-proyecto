class Juego:

    jugadores: int

    def inicializar(self):
        print("---------------------------")
        print(" Bienvenido al ahorcado!!!")
        print("---------------------------")
        print(" Modos:")
        print("     1. Un jugador")
        print("     2. Dos jugadores")
        print("         > ", end="")
        self.jugadores = int(input())