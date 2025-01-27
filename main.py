from Jugador import Jugador
from Juego import Juego
from Consola import Consola

juego = Juego()
Consola.print_menu(juego)
paula = Jugador("Paula",10000)
print(paula)

juego.crear_palabra()


while True:
    Consola.print_palabra(juego)
    Consola.preguntar_letra(juego)