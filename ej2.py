'''
Escriba un algoritmo que visualice una clasificación de 50 personas según edad y sexo. Deberá mostrar los siguientes resultados:
Cantidad de personas mayores de edad (18 años o más).
Cantidad de personas menores de edad.
Cantidad de personas masculinas mayores de edad.
Cantidad de personas femeninas menores de edad.
Porcentaje que representan las personas mayores de edad respecto al total de personas.
Porcentaje que representan las mujeres respecto al total de personas.

Utilice la instrucción LEER PERSONAS al inicio del programa para cargar los datos de las 50 personas en un variable, PERSONAS,
que actúa como un vector de 50 posiciones.
Cada elemento de PERSONAS es de un tipo estructurado que dispone dos campos:
SEXO y EDAD.
'''
# Clase persona para tener la estructura
class Persona:
    def __init__(self, sexo, edad):
        self.sexo = sexo
        self.edad = edad

PERSONAS = []

# Lectura 50 veces
for i in range(50):
    while True:
        sexo = input("LEER SEXO (M/F): ").upper()
        if sexo in ["M", "F"]:
            break
        else:
            print("Error: Por favor, ingrese 'M' o 'F' para el sexo.")

    while True:
        try:
            edad = int(input("LEER EDAD: "))
            if 0 <= edad <= 120:
                break
            else:
                print("Error: La edad debe estar en el rango de 0 a 120.")
        except ValueError:
            print("Error: Por favor, ingrese un valor numérico para la edad.")

    persona = Persona(sexo, edad)
    PERSONAS.append(persona)

# Contadores
mayores_de_edad = 0
menores_de_edad = 0
masculinos_mayores = 0
femeninos_menores = 0

# Calculo de contadores
for persona in PERSONAS:
    if persona.edad >= 18:
        mayores_de_edad += 1
        if persona.sexo == "M":
            masculinos_mayores += 1
    else:
        menores_de_edad += 1
        if persona.sexo == "F":
            femeninos_menores += 1

# Calculo de porcentajes
porcentaje_mayores = (mayores_de_edad / 50) * 100
porcentaje_mujeres = (femeninos_menores / 50) * 100

print(f"Cantidad de personas mayores de edad: {mayores_de_edad}")
print(f"Cantidad de personas menores de edad: {menores_de_edad}")
print(f"Cantidad de personas masculinas mayores de edad: {masculinos_mayores}")
print(f"Cantidad de personas femeninas menores de edad: {femeninos_menores}")
print(f"Porcentaje de personas mayores de edad respecto al total: {porcentaje_mayores}%")
print(f"Porcentaje de mujeres respecto al total: {porcentaje_mujeres}%")