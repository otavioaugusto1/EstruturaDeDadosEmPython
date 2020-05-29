from node import Node
# inserir na fila
# remover na fila
# observar o topo da fila
class Fila:

    def __init__(self):
       self._size = 0
       self.first = None
       self.last = None

    def __len__(self):
        return self._size   
    def push(self, elemento):
       node = Node(elemento)
        if self.last is None:
           self.last = node
        else:
            self.last.next = node
            self.last = node
        if self.first is None:
            self.first = node
        self._size = self._size + 1           
    def pop(self):
        if self.first is not None:
            elemento = self.first.data
            self.first - self.first.next
            self._size = self._size - 1
            return elemento
    def peek(self):
        