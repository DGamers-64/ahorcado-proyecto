import os, json, random
class Juego: 

    jugadores: int
    dificultad: int
    pistas: int
    palabra:str
    letras_acertadas:list
    
    def __init__(self):
        self.letras_acertadas= []
    
    def crear_palabra(self):
        with open('palabras.json', 'r', encoding='utf-8') as f:
            palabras = json.load(f)
        indice_palabra = random.randint(0,len(palabras))
        self.palabra = palabras[indice_palabra -1]
        print(self.palabra)
    