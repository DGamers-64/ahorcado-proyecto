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
        if self.dificultad == 1:
            palabra_obtenida = False
            while not palabra_obtenida:
                with open('palabras.json', 'r', encoding='utf-8') as f:
                    palabras = json.load(f)
                    if self.dificultad == 1:
                        dificultad_str = "Fácil"
                    elif self.dificultad == 2:
                        dificultad_str = "Media"
                    else:
                        dificultad_str = "Difícil"
                indice_palabra = random.randint(0,len(palabras))
                self.palabra = palabras[indice_palabra -1]
                if self.dificultad["dificultad"] == 1:
                    print(self.palabra)
        with open('palabras.json', 'r', encoding='utf-8') as f:
            palabras = json.load(f)
        indice_palabra = random.randint(0,len(palabras))
        self.palabra = palabras[indice_palabra -1]
    
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