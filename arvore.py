class Node:
    def __init__(self, dado):
        self.dado=dado
        self.esq = None
        self.dir = None
    def __str__(self):
        return str(self.dado)

class ArvoreBinaria:
    def __init__(self,dado=None):
        if dado:  
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
if __name__ == "__main__":
    arvore = ArvoreBinaria()
    n1 = Node('i')
    n2 = Node('n')
    n3 = Node('s')
    n4 = Node('c')
    n5 = Node('r')
    n6 = Node('e')
    n7 = Node('v')
    n8 = Node('a')
    n9 = Node('5')
    n0 = Node('3')
    n0.esq = n6
    n0.dir = n9
    n6.esq = n1
    n6.dir = n5
    n5.esq = n2
    n5.dir = n4
    n4.dir = n3
    n9.esq = n8
    n8.dir = n7
    arvore.raiz = n0 
    arvore.posOrdem()
    #arvore.simetric_traversal()
    print()        
    print(arvore.alturaDaArvore())