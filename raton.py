class Ratón:
    def __init__(self, codigo_referencia, fecha_nacimiento, peso, sexo, temperatura, notas, mutacion_X='Normal', mutacion_Y='Normal'):
        self.codigo_referencia = codigo_referencia
        self.fecha_nacimiento = fecha_nacimiento
        self.peso = peso
        self.sexo = sexo
        self.temperatura = temperatura
        self.notas = notas
        self.mutacion_X = mutacion_X
        self.mutacion_Y = mutacion_Y

    def __str__(self):
        return f"Código de Referencia: {self.codigo_referencia}\nFecha de Nacimiento: {self.fecha_nacimiento}\nPeso: {self.peso} gramos\nSexo: {self.sexo}\nTemperatura: {self.temperatura}°C\nNotas: {self.notas}\nMutación Cromosoma X: {self.mutacion_X}\nMutación Cromosoma Y: {self.mutacion_Y}"