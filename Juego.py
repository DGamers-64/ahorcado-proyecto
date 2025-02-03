import json, random

class Juego: 

    jugadores: int
    dificultad: int
    pistas: int
    palabra:dict
    letras_introducidas:list
    
    def __init__(self):
        self.letras_introducidas = []
    
    def crear_palabra(self) -> None:
        palabra_obtenida = False
        while not palabra_obtenida:
            with open('palabras.json', 'r', encoding='utf-8') as f:
                palabras = json.load(f)
            indice_palabra = random.randint(0,len(palabras)-1)
            self.palabra = palabras[indice_palabra]
            if (self.palabra["dificultad"] == "Fácil" and self.dificultad == 1) or (self.palabra["dificultad"] == "Media" and self.dificultad == 2) or (self.palabra["dificultad"] == "Difícil" and self.dificultad == 3):
                palabra_obtenida = True
    
    def comprobar_errores(self):
        errores = []
        for i in self.letras_introducidas:
            if i not in self.palabra["palabra"].upper():
                errores.append(i)
        return errores
    
    def comprobar_ganador(self):
        letras_unicas= []
        for letra in self.palabra["palabra"].upper():
            if letra not in letras_unicas and letra != " ":
                letras_unicas.append(letra)
        for letra in letras_unicas:
            if letra not in self.letras_introducidas:
                return False
        return True