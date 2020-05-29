class Node:
    def __init__(self, dado):
        self.dado=dado
        self.esq = None
        self.dir = None
    def __str__(self):
        return str(self.dado)

class ArvoreBinaria:
    def __init__(self,dado=None, node = None):
        if node:
            self.root = node
        elif dado:  
            node= Node(dado)
            self.raiz = node
        else:
            self.raiz = None    
    def simetric_traversal(self, node = None):
        if node is None:
            node = self.raiz
        if node.esq:
            print('(', end= '')
            self.simetric_traversal(node.esq)
        print(node, end='')
        if node.dir:
            self.simetric_traversal(node.dir)
            print(')', end='')        
    # Fazendo o pós ordem em uma árvore binária
    def posOrdem(self,no = None):
        if no is None:
            no = self.raiz
        if no.esq:
            self.posOrdem(no.esq)
        if no.dir:
            self.posOrdem(no.dir)
        print(no.dado)
    def alturaDaArvore(self, no = None):
        if no is None:
            no = self.raiz
        alturaDaDireita = 0
        alturaDaEsquerda = 0    
        if no.esq:
            alturaDaEsquerda= self.alturaDaArvore(no.esq)
        if no.dir:
            alturaDaDireita = self.alturaDaArvore(no.dir)
        if alturaDaDireita > alturaDaEsquerda:
           return alturaDaDireita + 1
        return alturaDaEsquerda + 1


#ABB herdando tudo da classe Árvore Binária
class ArvoreBinariaDeBusca(ArvoreBinaria):
    #Inserção
    def insercao(self, valor):
        parent = None
        x = self.raiz
        while(x):
            parent = x
            if valor < x.dado:
                x = x.esq
            else:
                x = x.dir    
        if parent is None:
            self.raiz = Node(valor)
        elif valor < parent.dado:
            parent.esq = Node(valor)
        else:
            parent.dir = Node(valor)    
    def busca(self,valor,  node):
        if node is None or node.dado == valor:
            return ArvoreBinaria(node)
        if valor < node.dado:
            return self.busca(valor,node.esq)
        return self.busca(valor, node.dir)
                     