import os, getpass
from Juego import Juego
class Consola:
    
    def print_linea(self) -> None:
        print("--------------------------------------------")
    
    def limpiar_consola(self) -> None:
        os.system("cls")

    def print_menu_bienvenida(self) -> None:
        self.limpiar_consola()
        self.print_linea()
        print("| Bienvenido al ahorcado de Paula y Daniel |")
        self.print_linea()
        input()
        self.limpiar_consola()

    def print_menu_jugadores(self) -> int:
        print(" Jugadores:")
        print("  1. Un jugador")
        print("  2. Dos jugadores")
        print("  > ", end="")
        jugadores = int(input())
        self.limpiar_consola()
        return jugadores

    def print_menu_dificultad(self) -> int:
        print(" Dificultad:")
        print("  1. Fácil")
        print("  2. Medio")
        print("  3. Dificil")
        print("  > ", end="")
        dificultad = int(input())
        self.limpiar_consola()
        return dificultad
    
    def print_menu_pistas(self) -> int:
        print(" Pistas:")
        print("  1. Con pistas")
        print("  2. Sin pistas")
        print("  > ", end="")
        pistas = int(input())
        self.limpiar_consola()
        return pistas

    def print_menu_inicial(self) -> tuple[int, int, int]:
        self.print_menu_bienvenida()
        jugadores = self.print_menu_jugadores()
        dificultad = self.print_menu_dificultad()
        pistas = self.print_menu_pistas()
        return jugadores, dificultad, pistas
        
    def print_palabra(self, juego: Juego) -> None:
        self.limpiar_consola()
        print(" ", end="")
        for caracter in juego.palabra["palabra"].upper():
            if caracter in juego.letras_introducidas:
                print (f"{caracter}", end=" ")
            elif caracter == " ":
                print(" ", end=" ")
            else:
                print("_", end=" ")
        print()
        for i in juego.letras_introducidas:
            if i not in juego.palabra["palabra"].upper():
                print(i, end=" ")
                
    def preguntar_letra(self, juego: Juego) -> None:
        print("\n\n > ", end="")
        letra = str(input()).upper()
        if letra == juego.palabra["palabra"].upper():
            for caracter in letra:
                juego.letras_introducidas.append(caracter)
        elif letra not in juego.letras_introducidas:
            juego.letras_introducidas.append(letra)

    def dibujar_ahorcado(self, errores: list[str]) -> None:
        estados = [
            "\n  +---+\n      |\n      |\n      |\n      |\n      |\n=========",
            "\n  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
            "\n  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
            "\n  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========", 
            "\n  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
            "\n  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
            "\n  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
            "\n  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="]
        print(estados[len(errores)])

    def print_ganador(self, jugador):
        print("\nHAS GANADO")
        print(f"\n{jugador.nombre} ahora tienes {jugador.puntuacion} puntos")
    
    def print_perdedor(self, jugador, juego):
        print("\nHAS PERDIDO")
        print(juego.palabra["palabra"].upper(), sep= "")
        print(f"\n{jugador.nombre} ahora tienes {jugador.puntuacion} puntos")

    def preguntar_nombre(self):
        return input("Nombre Jugador > ")
    
    def preguntar_palabra(self):
        self.limpiar_consola()
        return getpass.getpass(" Dime una palabra (se ve oculta) > ")
    
    def preguntar_pistas(self):
        return [getpass.getpass(" Dime una pista (se ve oculta) > ") for i in range(3)]