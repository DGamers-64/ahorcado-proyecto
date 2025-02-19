from Jugador import Jugador
from Juego import Juego
from Vista import Vista as Interfaz
from Modelo import Modelo

interfaz = Interfaz()
modelo = Modelo()

try:
    respuesta = 1
    while respuesta == 1:
        juego = Juego()
        resultado = 2
        while resultado != 1:
            resultado = interfaz.print_menu_bienvenida()
            if resultado == 2:
                jugadores = Modelo.get_jugadores()
                interfaz.print_ranking(jugadores)
            elif resultado == 3:
                interfaz.print_reglas()
        juego.jugadores = interfaz.print_menu_jugadores()

        # Aquí establecemos el juego dependiendo de la cantidad de jugadores

        if juego.jugadores != 2:
            juego.dificultad = interfaz.print_menu_dificultad()
            juego.pistas = interfaz.print_menu_pistas()
            nombre = interfaz.preguntar_nombre("adivinador")
            jugador1 = Jugador(nombre)
            juego.crear_palabra()
        elif juego.jugadores == 2:
            juego.dificultad = 1
            juego.pistas = 1
            nombre = interfaz.preguntar_nombre("adivinador")
            jugador1 = Jugador(nombre)
            nombre = interfaz.preguntar_nombre("preguntador")
            jugador2 = Jugador(nombre)
            palabra = interfaz.preguntar_palabra()
            pistas = interfaz.preguntar_pistas()
            juego.insertar_palabra(palabra, pistas)

        # Bucle principal

        errores = []
        ganador = False
        while len(errores) < 7 and not ganador:
            interfaz.print_palabra(juego.palabra, juego.letras_introducidas)
            interfaz.print_pistas(errores, juego.palabra_info["pistas"])
            interfaz.print_ahorcado(errores)
            juego.letras_introducidas = interfaz.preguntar_letra(juego.palabra, juego.letras_introducidas)
            errores = juego.comprobar_errores()
            ganador = juego.comprobar_ganador()

        # Resultados partida

        interfaz.print_palabra(juego.palabra, juego.letras_introducidas)
        interfaz.print_ahorcado(errores)
        if ganador:
            jugador1.sumar_puntos(juego.jugadores, juego.dificultad, juego.pistas)
            interfaz.print_ganador()
            print(jugador1)
            if juego.jugadores == 2:
                jugador2.restar_puntos(juego.jugadores, juego.dificultad, juego.pistas)
                print(jugador2)
        else:
            jugador1.restar_puntos(juego.jugadores, juego.dificultad, juego.pistas)
            interfaz.print_perdedor(juego.palabra)
            print(jugador1)
            if juego.jugadores == 2:
                jugador2.sumar_puntos(juego.jugadores, juego.dificultad, juego.pistas)
                print(jugador2)
        respuesta = interfaz.preguntar_seguir_jugando()
except KeyboardInterrupt:
    interfaz.print_keyboard_interrupt()