import os, getpass
from Modelo import Modelo

class Vista:
    
    def print_linea(self) -> None:
        print("--------------------------------------------")
    
    def limpiar_consola(self) -> None:
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")

    def input_vista(self, max_opciones: int) -> int:
        completado = False
        while not completado:
            try:
                self.print_linea()
                respuesta = int(input(" > "))
                self.print_linea()
                if respuesta < 1 or respuesta > max_opciones:
                    print("Err: Valor incorrecto")
                    continue
                completado = True
            except ValueError:
                print("Err: Valor incorrecto")
        return respuesta

    def print_menu_bienvenida(self) -> int:
        self.limpiar_consola()
        self.print_linea()
        print("Bienvenido al ahorcado de Paula y Daniel")
        self.print_linea()
        print(" Acción:")
        print("  1. Jugar")
        print("  2. Ranking")
        print("  3. Reglas del juego")
        resultado = self.input_vista(3)
        self.limpiar_consola()
        return resultado

    def print_ranking(self, jugadores: dict):
        self.limpiar_consola()
        self.print_linea()
        print("RANKING JUGADORES")
        self.print_linea()
        jugadores = dict(sorted(jugadores.items(), key=lambda x: x[1], reverse=True))
        contador = 1
        for key, valor in jugadores.items():
            print(f"{contador}. {key} {valor}")
            contador += 1
            if contador > 10:
                break
        self.print_linea()
        input()
        self.limpiar_consola()

    def print_menu_jugadores(self) -> int:
        self.print_linea()
        print("Jugadores:")
        self.print_linea()
        print(" 1. Un jugador")
        print(" 2. Dos jugadores")
        jugadores = self.input_vista(2)
        self.limpiar_consola()
        return jugadores

    def print_menu_dificultad(self) -> int:
        self.print_linea()
        print("Dificultad:")
        self.print_linea()
        print(" 1. Fácil")
        print(" 2. Medio")
        print(" 3. Dificil")
        dificultad = self.input_vista(3)
        self.limpiar_consola()
        return dificultad
    
    def print_menu_pistas(self) -> int:
        self.print_linea()
        print("Pistas:")
        self.print_linea()
        print(" 1. Con pistas")
        print(" 2. Sin pistas")
        pistas = self.input_vista(2)
        self.limpiar_consola()
        return pistas
        
    def print_palabra(self, palabra: str, letras_introducidas: list) -> None:
        self.limpiar_consola()
        for caracter in palabra:
            if caracter in letras_introducidas:
                print (f"{caracter}", end=" ")
            elif caracter == " ":
                print(" ", end=" ")
            else:
                print("_", end=" ")
        print()
        for i in letras_introducidas:
            if i not in palabra:
                print(i, end=" ")
            elif len(i) > 1 and i != palabra:
                print(i, end=" ")
                
    def preguntar_letra(self, palabra: str, letras_introducidas: list) -> list:
        print("\n\n > ", end="")
        letra = str(input()).upper()
        if letra == palabra:
            for caracter in letra:
                letras_introducidas.append(caracter)
        elif letra not in letras_introducidas:         
            letras_introducidas.append(letra)
        return letras_introducidas

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
    
    def print_perdedor(self, palabra) -> None:
        print("\nHAS PERDIDO")
        print(palabra, sep= "")

    def preguntar_nombre(self, modo: str) -> str:
        match modo:
            case "adivinador":
                respuesta = input("Nombre Adivinador > ")
            case "preguntador":
                respuesta = input("Nombre Preguntador > ")
        return respuesta
    
    def preguntar_palabra(self) -> str:
        self.limpiar_consola()
        return getpass.getpass("Dime una palabra (se ve oculta) > ").upper()
    
    def preguntar_pistas(self) -> list[str]:
        return [getpass.getpass("Dime una pista (se ve oculta) > ") for i in range(3)]
    
    def print_pistas(self, errores: list[str], pistas: list) -> None:
        if len(errores) >= 3:
            print("\n",pistas[0], sep="")
        if len(errores) >= 5:
            print("\n",pistas[1], sep="")
        if len(errores) >= 6:
            print("\n",pistas[2], sep="")

    def preguntar_seguir_jugando(self) -> int:
        print("¿Quieres seguir jugando?")
        print("  1. Si")
        print("  2. No")
        return self.input_vista(2)
    
    def print_error(self, e: str) -> None:
        match type(e).__name__:
            case "ValueError":
                print("Err: ¡Valor incorrecto!")
            case _:
                print(f"Err: {e}")

    def print_keyboard_interrupt(self) -> None:
        print("\n¡Hasta la próxima!")
        
    def print_reglas(self) -> None:
        self.print_linea()
        print("Reglas:")
        self.print_linea()
        print(" Hay 2 modos principales, 1 o 2 jugadores")
        print(" En un jugador elegirás la dificultad, y si usar o no pistas.")
        print(" Dependiendo de estas opciones tendrás más o menos puntuación.")
        print(" En 2 jugadores uno elige una palabra y el otro la debe de")
        print(" adivinar. El que pierda le dará 10 puntos al otro.")
        self.print_linea()
        input()
        self.limpiar_consola()