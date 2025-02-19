import json

class Modelo:

    @staticmethod
    def get_jugadores() -> dict:
        with open('jugador.json', 'r', encoding='utf-8') as f:
            jugadores = json.load(f)
        return jugadores
    
    @staticmethod
    def actualizar_jugador(nombre: str, puntuacion: int) -> None:
        jugadores = Modelo.get_jugadores()
        jugadores[nombre] = puntuacion
        with open('jugador.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(jugadores, indent=4))