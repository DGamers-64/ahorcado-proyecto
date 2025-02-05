from Jugador import Jugador
from Juego import Juego
from Consola import Consola as Interfaz

interfaz = Interfaz()

juego = Juego()
juego.jugadores, juego.dificultad, juego.pistas = interfaz.print_menu_inicial()

jugador1 = Jugador(interfaz.preguntar_nombre())

# MENU SOCKETS MÁS ADELANTE
if juego.jugadores == 2:
    jugador2 = Jugador(interfaz.preguntar_nombre())
    juego.insertar_palabra(interfaz)
else:
    juego.crear_palabra()

errores = []
ganador = False

while len(errores) < 7 and not ganador:
    interfaz.print_palabra(juego)
    if len(errores) >= 3 and juego.pistas == 1:
        print("\n",juego.palabra["pistas"][0], sep="")
    if len(errores) >= 5 and juego.pistas == 1:
        print("\n",juego.palabra["pistas"][1], sep="")
    if len(errores) >= 6 and juego.pistas == 1:
        print("\n",juego.palabra["pistas"][2], sep="")    
    interfaz.dibujar_ahorcado(errores)
    interfaz.preguntar_letra(juego)
    errores = juego.comprobar_errores()
    ganador = juego.comprobar_ganador()
interfaz.print_palabra(juego)
interfaz.dibujar_ahorcado(errores)
if ganador:
    jugador1.sumar_punto()
    interfaz.print_ganador(jugador1)
else:
    jugador1.restar_punto()
    interfaz.print_perdedor(jugador1, juego)