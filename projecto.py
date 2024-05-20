# Crea un programa por consola todos los números comprendidos
# * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
# * Debes almacenar los resultados en un vector y buscar dentro del vector que numeros cumplen la serie de fibonnaci
# * Debes imprimir todos los numeros del vector y a lado debe decir si Cumple con la serie de fibonnaci o no.
# * Las operaciones de tu algoritmo deben estar en funciones se espera la funcion de la serie de fibonnaci, la funcion del almacenamiento del vector y la funcion de la generacion de los numeros.
# * Pueden utilizar vectores o matrices pero si utilizan matrices tendra mayor valoracion su prueba.
# 10,11,13,14,17,19,20,22,23,25,26,28,29,31,32,34,35,37,38,40,41,43,44,46,47,49,50,52,53,55
def GeneradorNumeros():
    numeros=[]
    for i in range(10, 55):
        if i % 2 == 0 and i != 16 and i % 3 != 0:
            numeros.append(i)
    return numeros
def SerieFibonacci(x):
    fibonacci1 = [0, 1]
    while fibonacci1[-1] < x:
        fibonacci1.append(fibonacci1[-1] + fibonacci1[-2])
    return fibonacci1
def VerificacionFibonacci(numero):
    fibonacci1 = SerieFibonacci(numero)
    return numero in fibonacci1
def VerificarYAlmacenar(numeros):
    resultados = []
    for numero in numeros:
        CumpleFibonacci = VerificacionFibonacci(numero)
        resultados.append((numero, CumpleFibonacci))
    return resultados
def serie():
    Numeros = GeneradorNumeros()
    resultados = VerificarYAlmacenar(Numeros)
    print("Los números a continuación han sido verificados y cumplen con la serie de Fibonacci:")
    for numero, CumpleFibonacci in resultados:
        print(f"Número: {numero}, ¿Cumple con la verificación de Fibonacci?: {CumpleFibonacci}")
if __name__ == "__main__":
    serie()