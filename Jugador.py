class Jugador:
    puntuacion: int
    nombre: str
    records:dict

    def __init__(self, nombre, records):
        self.nombre = nombre
        self.records = records
        self.puntuacion = 0
    
    def __str__(self):
        return f"Usuario: {self.nombre} \n Puntuacion: {self.puntuacion} \n Records: {self.records}"
    
    
    
    
