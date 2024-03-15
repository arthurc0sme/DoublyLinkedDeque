#Tentativa  de implementação de Deque de forma duplamente encadeada
#Trabalho avaliativo da cadeira Estrutura de Dados Lineares 2023/2, Prof. Gilberto Irajá Müller


#Inicialização das classes essenciais.
class UnderflowError(Exception):
    pass

class DNode:
    def __init__(self, element=None, prev=None, next=None):
        self.element = element
        self.prev = prev
        self.next = next
    
    def __str__(self) -> str:
        return str(self.element)
    
class DoublyLinkedDeque:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._count: int = 0

    def __len__(self) -> int:
        return self._count

    def __str__(self) -> str:
        return "[" + " ".join([str(node) for node in self]) + "]"

    def __iter__(self) -> object:
        current: DNode = self._head
        while current:
            yield current.element
            current = current.next

    def is_empty(self) -> bool:
        return self._count == 0
    
    def size(self) -> int:
        return len(self)


    def insert_first(self, element:object):
        new_node = DNode(element, None, self._head)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._count += 1

    def insert_last(self, element:object):
        new_node = DNode(element, self._tail, None)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._count += 1

    def remove_first(self):
        if self.is_empty():
            raise UnderflowError()
        element = self._head.element
        if (self._head == self._tail):
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        self._count -= 1
        return element

    def remove_last(self):
        if self.is_empty():
            raise UnderflowError()
        element = self._tail.element
        if (self._head == self._tail):
            self._head = self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        self._count -= 1
        return element
    
    def peek_first(self) -> object:
        if self.is_empty():
            raise UnderflowError()
        return self._head.element
    
    def peek_last(self) -> object:
        if self.is_empty():
            raise UnderflowError()
        return self._tail.element

#Testando a implementação
if __name__ == "__main__":
    d = DoublyLinkedDeque()
    #Checando se o Deque está vazio
    print("Deque está vazio?", d.is_empty()) 
    #Inserindo Valores no Deque
    d.insert_first(4)
    d.insert_first(3)
    d.insert_last(5)
    d.insert_last(6)
    #Mostrando na tela valores do deque e checando se o mesmo continua vazio
    print("Elementos do Deque:", (str(d)))
    print("Deque está vazio?", d.is_empty())
    #Inserindo novos valores e mostrando na tela o conteúdo do deque.
    d.insert_first(2)
    d.insert_first(1)
    d.insert_last(7)
    d.insert_last(8)
    d.insert_last(9)
    print("Elementos do Deque:", (str(d)))
    #Mostrando o primeiro e último elemento do Deque
    print("Primeiro elemento: ", d.peek_first())
    print("Ultimo elemento: ", d.peek_last())
    #Removendo o primeiro e último elemento do Deque e mostrando na tela
    print("Primeiro elemento removido: ", d.remove_first())
    print("Último elemento removido: ",d.remove_last())
    #Mostrando na tela informações finais do Deque após as operações
    print("Elementos do Deque:", (str(d)))
    print("Numero de elementos no Deque:", d.size())
    print("Primeiro elemento: ", d.peek_first())
    print("Ultimo elemento: ", d.peek_last())