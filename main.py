from Jugador import Jugador
from Juego import Juego
from Consola import Consola as Interfaz

interfaz = Interfaz()

juego = Juego()
juego.jugadores, juego.dificultad, juego.pistas = interfaz.print_menu_inicial()

# PREGUNTAR NOMBRE A JUGADOR Y SI YA EXISTE EN LA BASE DE DATOS USAR SU USUARIO, SI NO CREAR UNO NUEVO
# jugador1 = juego.nuevoJugador
# if jugador1 == existe
#   jugador1 = Jugador(ya existente)
# else
#   jugador1 = Jugador(nuevo)

# ¿HACER BUCLES DISTINTOS DEPENDIENDO DE LAS OPCIONES?

juego.crear_palabra()

errores = []

while len(errores) < 7 or not juego.comprobar_ganador():
    interfaz.print_palabra(juego)
    interfaz.preguntar_letra(juego)
    errores = juego.comprobar_errores()