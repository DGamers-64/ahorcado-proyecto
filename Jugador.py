import json

class Jugador:
    nombre: str
    puntuacion: int

    def __init__(self, nombre: str) -> None:
        with open('jugador.json', 'r', encoding='utf-8') as f:
            jugadores = json.load(f)
        if nombre not in jugadores:
            jugadores[nombre] = 0
        self.nombre = nombre
        self.puntuacion = jugadores[nombre]

    def __str__(self) -> str:
        return f"Usuario: {self.nombre} \nPuntuacion: {self.puntuacion}"

    def sumar_punto(self) -> None:
        self.puntuacion += 1
        with open('jugador.json', 'r', encoding='utf-8') as f:
            jugadores = json.load(f)
        jugadores[self.nombre] = self.puntuacion
        with open('jugador.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(jugadores, indent=4))

    def restar_punto(self) -> None:
        self.puntuacion -= 1
        with open('jugador.json', 'r', encoding='utf-8') as f:
            jugadores = json.load(f)
        jugadores[self.nombre] = self.puntuacion
        with open('jugador.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(jugadores, indent=4))