'''
Desarrolle un algoritmo para el cálculo del salario de un trabajador. 
El importe liquidado (sueldo) depende de una tarifa o precio por hora establecida y de un condicionante sobre las horas trabajadas: 
si la cantidad de horas trabajadas es mayor a 40 horas, la tarifa se incrementa en un 50% para las horas extras. 
Calcular el sueldo recibido por el trabajador en base las horas trabajadas y la tarifa. 
Utilice las instrucciones LEER HORASTRABAJADAS y LEER TARIFA al inicio del programa para cargar los valores en las variables 
HORASTRABAJADAS y TARIFA.
'''
# Lectura
HORASTRABAJADAS = float(input("LEER HORASTRABAJADAS: "))
TARIFA = float(input("LEER TARIFA: "))

# Calculo horas normales y horas extra
if HORASTRABAJADAS > 40:
    horas_normales = 40
    horas_extra = HORASTRABAJADAS - 40
else:
    horas_normales = HORASTRABAJADAS
    horas_extra = 0

# Calculo salario
sueldo = (horas_normales * TARIFA) + (horas_extra * TARIFA * 1.5)

print(f"El salario del trabajador es: {sueldo}")
