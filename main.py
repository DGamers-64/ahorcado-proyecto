from Jugador import Jugador
from Juego import Juego
from Consola import Consola as Interfaz

interfaz = Interfaz()

juego = Juego()
juego.jugadores, juego.dificultad, juego.pistas = interfaz.print_menu_inicial()

# PREGUNTAR NOMBRE A JUGADOR Y SI YA EXISTE EN LA BASE DE DATOS USAR SU USUARIO, SI NO CREAR UNO NUEVO
nombre = input("Nombre Jugador >")
jugador1 = Jugador(nombre)
# if jugador1 == existe
#   jugador1 = Jugador(ya existente)
# else
#   jugador1 = Jugador(nuevo)

# ¿HACER BUCLES DISTINTOS DEPENDIENDO DE LAS OPCIONES?

juego.crear_palabra()

errores = []
ganador = False

while len(errores) < 7 and not ganador:
    interfaz.print_palabra(juego)
    if len(errores) >= 3 and juego.pistas == 1:
        print("\n\n",juego.palabra["pistas"][0], sep="")
    if len(errores) >= 5 and juego.pistas == 1:
        print("\n\n",juego.palabra["pistas"][1], sep="")
    if len(errores) >= 6 and juego.pistas == 1:
        print("\n\n",juego.palabra["pistas"][2], sep="")    
    interfaz.dibujar_ahorcado(errores)
    interfaz.preguntar_letra(juego)
    errores = juego.comprobar_errores()
    ganador = juego.comprobar_ganador()
interfaz.print_palabra(juego)
if ganador:
    print("\n\nHAS GANADO")
else:
    print("\n\nHAS PERDIDO")
    print("\n", juego.palabra["palabra"].upper(), sep= "")
interfaz.dibujar_ahorcado(errores)