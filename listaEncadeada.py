from node import Node
class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.tamanho = 0
    def append(self, elemento):
        if self.head:
            #inserção quando a lista já possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elemento)    
        else:
            # Primeira inserção
            self.head = Node(elemento)
        self.tamanho = self.tamanho + 1
    def __len__(self):
        return self.tamanho
    def getElemento(self, item):
        pointer = self.head
        for i in range(item):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")
    
    def setElemento(self, index, item):
        pointer = self.head
        for i in range(item):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            pointer.data = item
        else:
            raise IndexError("list index out of range")
    
    
    def busca(self, item): # Retorna o índice do elemento na lista
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == item:
                return i
            pointer = pointer.next
            i = i + 1    
        raise ValueError("{} is not in list".format(item))

