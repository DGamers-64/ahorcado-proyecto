import json

class Modelo:

    @staticmethod
    def get_jugadores() -> dict:
        with open('jugador.json', 'r', encoding='utf-8') as f:
            jugadores = json.load(f)
        return jugadores
    
    @staticmethod
    def add_jugador_nuevo(jugadores: dict, jugador: list) -> None:
        jugadores[jugador[0]] = jugador[1]
        with open('jugador.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(jugadores, indent=4))