from node import Node
# inserir na pilha
# remover na pilha
# observar o topo da pilha
class Pilha:

    def __init__(self):
        self.topo =None
        self._size = 0
    def __len__(self):
        return self._size    
    def push(self, elemento):
        #insere um elemento na pilha
        node = Node(elemento)
        node.next = self.topo
        self.top = node
        self._size = self._size + 1
    def pop(self):
        # remove o último elemento da pilha, não especifica qual, pois é o último
        if self._size > 0:
            node = self.topo
            self.topo = self.topo.next
            self._size = self._size + 1
            return node.data
    def peek(self):
        #retorna o último elemento da pilha
        if self._size > 0:
            return self.topo.data
