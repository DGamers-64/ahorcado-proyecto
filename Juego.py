import os
class Juego:

    jugadores: int
    dificultad: int
    pistas: int

    def menuInicio(self):
        print("---------------------------")
        print(" Bienvenido al ahorcado")
        print("---------------------------")
        print(" Modos:")
        print("  1. Un jugador")
        print("     2. Dos jugadores")
        print("         > ", end="")
        self.jugadores = int(input())
        os.system("cls")
    
    def menuDificultad(self):
        print(f" Jugadores: {self.jugadores}")
        print(" Modos:")
        print("  1. Fácil")
        print("  2. Difícil")
        print("         > ", end="")
        self.dificultad = int(input())

    def menuPistas(self):
        print(f"Jugadores: {self.jugadores}")
        print(f"Dificultad: {self.dificultad}")
        print(" Modos:")
        print("  1. Con pistas")
        print("  2. Sin pistas")
        print("         > ", end="")
        self.pistas = int(input())