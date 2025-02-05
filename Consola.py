import os, getpass
from Juego import Juego
from Jugador import Jugador

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
        if jugadores == 1:
            dificultad = self.print_menu_dificultad()
            pistas = self.print_menu_pistas()
        else:
            dificultad = 1
            pistas = 1
        return jugadores, dificultad, pistas
        
    def print_palabra(self, juego: Juego) -> None:
        self.limpiar_consola()
        palabra = juego.palabra["palabra"].upper()
        for caracter in palabra:
            if caracter in juego.letras_introducidas:
                print (f"{caracter}", end=" ")
            elif caracter == " ":
                print(" ", end=" ")
            else:
                print("_", end=" ")
        print()
        for i in juego.letras_introducidas:
            if i not in palabra:
                print(i, end=" ")
            elif len(i) > 1 and i != palabra:
                print(i, end=" ")
                
    def preguntar_letra(self, juego: Juego) -> None:
        print("\n\n > ", end="")
        letra = str(input()).upper()
        if letra == juego.palabra["palabra"].upper():
            for caracter in letra:
                juego.letras_introducidas.append(caracter)
        elif letra not in juego.letras_introducidas:
            juego.letras_introducidas.append(letra)

    def print_ahorcado(self, errores: list[str]) -> None:
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

    def print_ganador(self) -> None:
        print("\nHAS GANADO")
    
    def print_perdedor(self, juego: Juego) -> None:
        print("\nHAS PERDIDO")
        print(juego.palabra["palabra"].upper(), sep= "")

    def preguntar_nombre(self) -> str:
        return input("Nombre Jugador > ")
    
    def preguntar_palabra(self) -> str:
        self.limpiar_consola()
        return getpass.getpass("Dime una palabra (se ve oculta) > ")
    
    def preguntar_pistas(self) -> str:
        return [getpass.getpass("Dime una pista (se ve oculta) > ") for i in range(3)]
    
    def print_pistas(self, errores: list[str], juego: Juego) -> None:
        if len(errores) >= 3 and juego.pistas == 1:
            print("\n",juego.palabra["pistas"][0], sep="")
        if len(errores) >= 5 and juego.pistas == 1:
            print("\n",juego.palabra["pistas"][1], sep="")
        if len(errores) >= 6 and juego.pistas == 1:
            print("\n",juego.palabra["pistas"][2], sep="")

    def print_jugador(self, jugador: Jugador) -> None:
        self.print_linea()
        print(jugador)