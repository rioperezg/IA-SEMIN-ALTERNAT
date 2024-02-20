import os
from poblacion_ratones import PoblacionRatones
from raton import Ratón

def validar_numero_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def validar_numero_real(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingrese un número real válido.")

def validar_sexo(mensaje):
    while True:
        sexo = input(mensaje).capitalize()
        if sexo in ['Macho', 'Hembra']:
            return sexo
        else:
            print("El sexo debe ser 'Macho' o 'Hembra'.")

def main():
    while True:
        print("\nMenú Principal:")
        print("1. Abrir un archivo de texto plano con formato y extensión csv que contenga una población de ratones.")
        print("2. Crear una nueva población de ratones.")
        print("3. Añadir un nuevo ratón a una población ya existente.")
        print("4. Listar los códigos de referencia de todos los ratones de una población.")
        print("5. Eliminar un ratón de una población indicando su código de referencia.")
        print("6. Modificar los datos de un ratón, indicando previamente su código de referencia.")
        print("7. Ver información detallada de un ratón, habiendo especificado previamente su código de referencia.")
        print("8. Guardar.")
        print("9. Guardar como.")
        print("10. Salir.")

        opcion = validar_numero_entero("Seleccione una opción del menú: ")

        if opcion == 1:
            archivo = input("Ingrese el nombre del archivo CSV a abrir: ")
            if os.path.exists(archivo):
                poblacion = PoblacionRatones.cargar_desde_archivo(archivo)
                print("Archivo cargado exitosamente.")
            else:
                print("El archivo especificado no existe.")
        
        elif opcion == 2:
            nombre_poblacion = input("Ingrese el nombre de la población de ratones: ")
            responsable = input("Ingrese el nombre de la persona responsable: ")
            dias = validar_numero_entero("Ingrese el número de días que la población estará en las instalaciones: ")
            poblacion = PoblacionRatones(nombre_poblacion, responsable, dias)
            print("Población creada exitosamente.")

        elif opcion == 3:
            if 'poblacion' in locals():
                codigo_referencia = input("Ingrese el código de referencia del nuevo ratón: ")
                fecha_nacimiento = input("Ingrese la fecha de nacimiento del nuevo ratón (DD/MM/AAAA): ")
                peso = validar_numero_entero("Ingrese el peso del nuevo ratón (en gramos): ")
                sexo = validar_sexo("Ingrese el sexo del nuevo ratón (Macho/Hembra): ")
                temperatura = validar_numero_real("Ingrese la temperatura corporal del nuevo ratón (en grados centígrados): ")
                notas = input("Ingrese notas adicionales sobre el nuevo ratón: ")
                mutacion_X = input("Ingrese el estado del cromosoma X (Normal/Mutado): ")
                mutacion_Y = input("Ingrese el estado del cromosoma Y (Normal/Mutado): ")
                poblacion.agregar_ratón(Ratón(codigo_referencia, fecha_nacimiento, peso, sexo, temperatura, notas, mutacion_X, mutacion_Y))