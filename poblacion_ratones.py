import csv

class PoblacionRatones:
    def __init__(self, nombre_poblacion, responsable, dias):
        self.nombre_poblacion = nombre_poblacion
        self.responsable = responsable
        self.dias = dias
        self.ratones = []

    def agregar_ratón(self, ratón):
        self.ratones.append(ratón)

    def listar_codigos_referencia(self):
        return [ratón.codigo_referencia for ratón in self.ratones]

    def eliminar_ratón(self, codigo_referencia):
        for ratón in self.ratones:
            if ratón.codigo_referencia == codigo_referencia:
                self.ratones.remove(ratón)
                return True
        return False

    def modificar_ratón(self, codigo_referencia, nuevos_datos):
        for ratón in self.ratones:
            if ratón.codigo_referencia == codigo_referencia:
                ratón.__dict__.update(nuevos_datos)
                return True
        return False

    def obtener_ratón_por_codigo(self, codigo_referencia):
        for ratón in self.ratones:
            if ratón.codigo_referencia == codigo_referencia:
                return ratón
        return None

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Codigo Referencia', 'Fecha de Nacimiento', 'Peso', 'Sexo', 'Temperatura', 'Notas', 'Mutacion X', 'Mutacion Y'])
            for ratón in self.ratones:
                writer.writerow([ratón.codigo_referencia, ratón.fecha_nacimiento, ratón.peso, ratón.sexo, ratón.temperatura, ratón.notas, ratón.mutacion_X, ratón.mutacion_Y])

    @staticmethod
    def cargar_desde_archivo(nombre_archivo):
        poblacion = PoblacionRatones("", "", 0)
        with open(nombre_archivo, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                poblacion.agregar_ratón(Ratón(*row))
        return poblacion