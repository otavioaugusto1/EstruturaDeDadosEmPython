#diferente das listas sequenciais, elas não armazenam seus dados de forma sequencial 
# na memória, ou seja, não há uma fila já separada com o tamanho necessário
#para armazenar tudo em uma fileira só.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
