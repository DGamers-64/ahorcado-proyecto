import os
class Consola:
    
    def print_linea():
        print("-------------------------------------")
    
    def limpiar_consola():
        os.system("cls")
        
    def print_menu_inicial() -> tuple[int, int, int]:
        Consola.limpiar_consola()
        Consola.print_linea()
        print(" Bienvenido al ahorcado")
        Consola.print_linea()
        print(" Modos:")
        print("  1. Un jugador")
        print("  2. Dos jugadores")
        print("  > ", end="")
        jugadores = int(input())
        Consola.limpiar_consola()
        print(f" Jugadores: {jugadores}")
        print(" Modos:")
        print("  1. Fácil")
        print("  2. Difícil")
        print("  > ", end="")
        dificultad = int(input())
        Consola.limpiar_consola()
        print(f"Jugadores: {jugadores}")
        print(f"Dificultad: {dificultad}")
        print(" Modos:")
        print("  1. Con pistas")
        print("  2. Sin pistas")
        print("  > ", end="")
        pistas = int(input())
        Consola.limpiar_consola()
        return jugadores, dificultad, pistas
        
    def print_palabra(juego: object):
        Consola.limpiar_consola()
        print(" ", end="")
        for caracter in juego.palabra["palabra"].upper():
            if caracter in juego.letras_introducidas:
                print (f"{caracter}", end=" ")
            elif caracter == " ":
                print(" ", end=" ")
            else:
                print("_", end=" ")
                
    def preguntar_letra(lista: list[str]) -> list[str]:
        print("\n\n > ", end="")
        letra = str(input()).upper()
        lista.append(letra)
        return lista
