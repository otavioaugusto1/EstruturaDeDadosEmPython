lista1 = []
lista = [1,2,3,4,5]
lista[0]          # acesso aleatório(pois basta informar o índice)


# Busca
def busca(lista, elem):
    #return o índice do elemento caso esteja na lista ou None caso contrário
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None

lista_estranha = [1,"Oi", 25, "Trezeguet", "Zidane", 9]
elemento = 25
resultado = busca(lista_estranha,elemento)

if resultado is not None:
    print(' O elemento {} esta na indice  {}'.format(elemento, resultado))
else:
    print("O elemento {} não se encontra na lista".format(elemento))    


#complexidade : O(n), ou seja, linear  


# Inserção e Remoção
#para inserir, vai depender da posição
#se for no final, basta ir para a última posição+1 e adicionar
#caso seja na primeira posição ou meio, deverá empurrar todo o restante
# Complexidade no pior caso: O(n), pois terá que empurrar a lista inteira de tamanho N
# Da mesma forma para remoção
