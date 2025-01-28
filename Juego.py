import json, random

class Juego: 

    jugadores: int
    dificultad: int
    pistas: int
    palabra:str
    letras_introducidas:list
    
    def __init__(self):
        self.letras_introducidas = []
    
    def crear_palabra(self) -> None:
        with open('palabras.json', 'r', encoding='utf-8') as f:
            palabras = json.load(f)
        indice_palabra = random.randint(0,len(palabras))
        self.palabra = palabras[indice_palabra -1]
    