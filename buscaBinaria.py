#Necessita estar ordenado o array.

def buscaBinaria(array, valor,inicio=0, fim= None):
    if fim is None:
        fim = len(lista)-1
    if inicio <= fim:
        m = (inicio + fim)//2
        if array[m] == valor:
            return m
        if valor < array[m]:
            return buscaBinaria(array, valor, inicio, m-1)
        else:
            return buscaBinaria(array,valor,m+1,fim)
    return None

lista = [1,2,3,4,5,6]
#print(buscaBinaria(lista, 5, 0, len(lista)-1))
