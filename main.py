from Jugador import Jugador
from Juego import Juego
from Consola import Consola as Interfaz

juego = Juego()
juego.jugadores, juego.dificultad, juego.pistas = Interfaz.print_menu_inicial()

# PREGUNTAR NOMBRE A JUGADOR Y SI YA EXISTE EN LA BASE DE DATOS USAR SU USUARIO, SI NO CREAR UNO NUEVO
# jugador1 = juego.nuevoJugador
# if jugador1 == existe
#   jugador1 = Jugador(ya existente)
# else
#   jugador1 = Jugador(nuevo)

# ¿HACER BUCLES DISTINTOS DEPENDIENDO DE LAS OPCIONES?

juego.crear_palabra()

while True:
    Interfaz.print_palabra(juego)
    juego.letras_introducidas = Interfaz.preguntar_letra(juego.letras_introducidas)