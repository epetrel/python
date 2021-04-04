"""
#FOR
for variable in elemento iterable
    BLOQUE DE INSTRUCCIONES
"""
contador = 0
resultado = 0
for contador in range(0, 5):
    print("Voy por el " + str(contador))
    resultado += contador
print (resultado)