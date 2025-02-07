from Jugador import Jugador
from Juego import Juego
from Consola import Consola as Interfaz

interfaz = Interfaz()

try:
    respuesta = 1
    while respuesta == 1:
        juego = Juego()
        juego.jugadores, juego.dificultad, juego.pistas = interfaz.print_menu_inicial()
        jugador1 = Jugador(interfaz.preguntar_nombre())
        
        # MENU SOCKETS MÁS ADELANTE 
        if juego.jugadores == 2:
            jugador2 = Jugador(interfaz.preguntar_nombre())
            palabra = interfaz.preguntar_palabra()
            pistas = interfaz.preguntar_pistas()
            juego.insertar_palabra(palabra, pistas)
        else:
            juego.crear_palabra()

        errores = []
        ganador = False
        while len(errores) < 7 and not ganador:
            juego.letras_introducidas = interfaz.print_palabra(juego.palabra["palabra"].upper(), juego.letras_introducidas)
            interfaz.print_pistas(errores, juego)
            interfaz.print_ahorcado(errores)
            interfaz.preguntar_letra(juego)
            errores = juego.comprobar_errores()
            ganador = juego.comprobar_ganador()
        juego.letras_introducidas = interfaz.print_palabra(juego.palabra["palabra"].upper(), juego.letras_introducidas)
        interfaz.print_ahorcado(errores)
        if ganador:
            jugador1.sumar_punto()
            interfaz.print_ganador()
            interfaz.print_jugador(jugador1)
            if juego.jugadores == 2:
                jugador2.restar_punto()
                interfaz.print_jugador(jugador2)
        else:
            jugador1.restar_punto()
            interfaz.print_perdedor(juego)
            interfaz.print_jugador(jugador1)
            if juego.jugadores == 2:
                jugador2.sumar_punto()
                interfaz.print_jugador(jugador2)
        respuesta = interfaz.preguntar_seguir_jugando()
except KeyboardInterrupt:
    interfaz.print_keyboard_interrupt()
except Exception as e:
    interfaz.print_error(e)