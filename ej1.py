'''
Escriba un algoritmo que lea un número entero y determine si es par o impar.
Si es par, que escriba todos los pares de manera descendiente desde sí mismo y hasta el cero.
Si es impar, que escriba todos los impares de manera descendiente desde si sí mismo hasta el uno.
Utilice la instrucción LEER NUMERO al inicio del programa para cargar un número en la variable NUMERO.
'''
# Lectura
NUMERO = int(input("LEER NUMERO: "))

# Verificación par o impar
if NUMERO % 2 == 0:
    print(f"{NUMERO} es par")
    
    # Pares descendientes
    for i in range(NUMERO, -1, -2):
        print(i)
else:
    print(f"{NUMERO} es impar")
    
    # Impares descendientes
    for i in range(NUMERO, 0, -2):
        print(i)
