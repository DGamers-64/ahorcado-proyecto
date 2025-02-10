import json, random

class Juego: 

    jugadores: int
    dificultad: int
    pistas: int
    palabra_info: dict
    __palabra: str
    letras_introducidas:list
    
    def __init__(self) -> None:
        self.letras_introducidas = []

    @property
    def palabra(self) -> str:
        return self.__palabra
    
    @palabra.setter
    def palabra(self, palabra_obtenida):
        self.__palabra = palabra_obtenida
    
    def crear_palabra(self) -> None:
        palabra_obtenida = False
        while not palabra_obtenida:
            with open('palabras.json', 'r', encoding='utf-8') as f:
                palabras = json.load(f)
            indice_palabra = random.randint(0,len(palabras)-1)
            self.palabra_info = palabras[indice_palabra]
            self.palabra = self.palabra_info["palabra"].upper()
            if (self.palabra_info["dificultad"] == "Fácil" and self.dificultad == 1) or (self.palabra_info["dificultad"] == "Media" and self.dificultad == 2) or (self.palabra_info["dificultad"] == "Difícil" and self.dificultad == 3):
                palabra_obtenida = True

    def insertar_palabra(self, palabra: str, pistas: list[str]) -> None:
        self.palabra = palabra
        self.palabra_info = { "palabra": palabra, "pistas": pistas }
    
    def comprobar_errores(self) -> list[str]:
        errores = []
        palabra = self.palabra
        for i in self.letras_introducidas:
            if i not in palabra:
                errores.append(i)
            elif len(i) > 1 and i != palabra:
                errores.append(i)
        return errores
    
    def comprobar_ganador(self) -> bool:
        letras_unicas= []
        for letra in self.palabra:
            if letra not in letras_unicas and letra != " ":
                letras_unicas.append(letra)
        for letra in letras_unicas:
            if letra not in self.letras_introducidas:
                return False
        return True