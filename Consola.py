import os
class Consola:
    
    def print_linea(self, ):
        print("-------------------------------------")
    
    def limpiar_consola(self, ):
        os.system("cls")
        
    def print_menu_inicial(self, ) -> tuple[int, int, int]:
        self.limpiar_consola()
        self.print_linea()
        print(" Bienvenido al ahorcado")
        self.print_linea()
        print(" Modos:")
        print("  1. Un jugador")
        print("  2. Dos jugadores")
        print("  > ", end="")
        jugadores = int(input())
        self.limpiar_consola()
        print(f" Jugadores: {jugadores}")
        print(" Modos:")
        print("  1. Fácil")
        print("  2. Difícil")
        print("  > ", end="")
        dificultad = int(input())
        self.limpiar_consola()
        print(f"Jugadores: {jugadores}")
        print(f"Dificultad: {dificultad}")
        print(" Modos:")
        print("  1. Con pistas")
        print("  2. Sin pistas")
        print("  > ", end="")
        pistas = int(input())
        self.limpiar_consola()
        return jugadores, dificultad, pistas
        
    def print_palabra(self, juego):
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
                
    def preguntar_letra(self, juego):
        print("\n\n > ", end="")
        letra = str(input()).upper()
        if letra == juego.palabra["palabra"].upper():
            for caracter in letra:
                juego.letras_introducidas.append(caracter)
        elif letra not in juego.letras_introducidas:
            juego.letras_introducidas.append(letra)

    def dibujar_ahorcado(self, errores):
        estados = [
            "\n  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
            "\n  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
            "\n  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========", 
            "\n  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
            "\n  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
            "\n  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
            "\n  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="]
        if len(errores) > 0:
            print(estados[len(errores)-1])