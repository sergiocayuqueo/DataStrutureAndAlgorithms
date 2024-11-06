class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return
        else:
            current = self.head

            while current.next:
                current = current.next
            current.next = new_node

    def nodo_de_medio(self, start, end):
        slow = start
        fast = start

        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next

        return slow

    def busqueda_binaria(self, start, end, value_objetivo):
        if start == end:
            return False

        medio = self.nodo_de_medio(start, end)

        if medio.value == value_objetivo:
            return True
        elif medio.value < value_objetivo:
            return self.busqueda_binaria(medio.next, end, value_objetivo)
        elif medio.value > value_objetivo:
            return self.busqueda_binaria(start, medio, value_objetivo)


if __name__ == '__main__':

    lista_enlazada = LinkedList()

    n = int(input("Ingrese la cantidad de nodos que tendrà la lista: "))

    for i in range(n):
        value = int(input(f"ingrese el valor del nodo {i + 1} : "))
        lista_enlazada.append(value)

    valor_objetivo = int(
        input("ingrese el valor que desea buscar en la lista: "))

    resultado = lista_enlazada.busqueda_binaria(
        lista_enlazada.head, None, valor_objetivo)

    print(resultado)
