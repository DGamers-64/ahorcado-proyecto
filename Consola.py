import os
class Consola:
    
    def print_linea():
        print("------------------------------------------------")
    
    def limpiar_consola():
        os.system("cls")
        
    def print_menu(juego):
        Consola.limpiar_consola()
        print("---------------------------")
        print(" Bienvenido al ahorcado")
        print("---------------------------")
        print(" Modos:")
        print("  1. Un jugador")
        print("     2. Dos jugadores")
        print("         > ", end="")
        juego.jugadores = int(input())
        Consola.limpiar_consola()
        print(f" Jugadores: {juego.jugadores}")
        print(" Modos:")
        print("  1. Fácil")
        print("  2. Difícil")
        print("         > ", end="")
        juego.dificultad = int(input())
        Consola.limpiar_consola()
        print(f"Jugadores: {juego.jugadores}")
        print(f"Dificultad: {juego.dificultad}")
        print(" Modos:")
        print("  1. Con pistas")
        print("  2. Sin pistas")
        print("         > ", end="")
        juego.pistas = int(input())
        
    def print_palabra(juego):
        for caracter in juego.palabra["palabra"].upper():
            if caracter in juego.letras_acertadas:
                print (f"{caracter} ", end="")
            elif caracter == " ":
                print("  ", end="")
            else:
                print("_ ", end="")
                
    def preguntar_letra(juego):
        letra = str(input("Dime una letra: ")).upper()
        juego.letras_acertadas.append(letra)
        print(juego.letras_acertadas)
    
    
            