import json
from Modelo import Modelo 

class Jugador:
    nombre: str
    puntuacion: int

    def __init__(self, nombre: str) -> None:
        jugadores = Modelo.get_jugadores()
        if nombre not in jugadores:
            jugadores[nombre] = 0
        self.nombre = nombre
        self.puntuacion = jugadores[nombre]

    def __str__(self) -> str:
        return f"Usuario: {self.nombre} \nPuntuacion: {self.puntuacion}"

    def sumar_puntos(self, jugadores, dificultad, pistas) -> None:
        if jugadores != 2:
            puntuacion_partida = 1
            puntuacion_partida *= dificultad
            puntuacion_partida *= pistas
        else:
            puntuacion_partida = 10
        self.puntuacion += puntuacion_partida
        Modelo.actualizar_jugador(self.nombre, self.puntuacion)

    def restar_puntos(self, jugadores, dificultad, pistas) -> None:
        if jugadores != 2:
            puntuacion_partida = 1
            puntuacion_partida *= dificultad
            puntuacion_partida *= pistas
        else:
            puntuacion_partida = 10
        self.puntuacion -= puntuacion_partida
        Modelo.actualizar_jugador(self.nombre, self.puntuacion)