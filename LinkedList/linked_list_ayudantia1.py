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
    
        current = self.head
        while current.next != None:
            current = current.next
        
        current.next = new_node


    def append_recursive(self, nodo, value ):
        if nodo == None:
            return Node(value)
        
        nodo.next = self.append_recursive(nodo.next, value)
        return nodo

    def print_list(self):
        if self.head is None:
            print("La lista está vacía")
            return

        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


    def print_list_recurive(self, nodo):
        if nodo == None:
            print("None:")
            return
        print(nodo.value, end=" -> ")
        self.print_list_recurive(nodo.next)
        
        
    def buscar_recursivamente(self, nodo, value):
        if nodo == None:
            return False
        if nodo.value == value: #4 == 7
            return True
        
        return self.buscar_recursivamente(nodo.next, value)


    def delete_value(self, value):
        if self.head == None:
            print("La lista no contiene ningùn nodo")
            return
        
        if self.head.value == value:
            self.head = self.head.next

        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next


    def insertar_valor(self, valor, index):
        new_node = Node(valor)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        contador = 0
        current = self.head
        while current.next != None and contador < index:
            current = current.next
            contador += 1

        if current.next == None:
            print("No es posible ingresa un nuevo nodo con un nuevo valor, puesto que la lista es màs pequeña")
            return


        new_node.next = current.next
        current.next = new_node
        print("nodo con su valor agregado correctamente a la lista")
        return

    def largo(self):
        if self.head == None:
            print("La lista esta vacia, no hay nodos")
            return
        
        contador = 0
        current = self.head
        while current.next != None:
            current = current.next
            contador += 1
        print(f"El largo de la lista es: {contador}")
        return


    def largo_recursivo(self, nodo):
        if nodo == None:
            return 0
        
        return 1 + self.largo_recursivo(nodo.next) # 1 + (1 + (1 + (1 +(1 + (1 + (0))))))


    def encontrar_mayor(self):
        if self.head == None:
            return None

        mayor = self.head.value

        current = self.head.next

        while current != None:
            if current.value > mayor:
                mayor = current.value

            current = current.next

        return mayor
   
    def encontrar_mayor_recurisvo(self, nodo):
        if nodo == None:
            return float('-inf')

        mayor = self.encontrar_mayor_recurisvo(nodo.next)

        return max(nodo.value, mayor)





if __name__ == "__main__":

    lista_enlazada = LinkedList()

    print("append estructuradamente: (normalmente)")
    lista_enlazada.append(1)
    lista_enlazada.append(2)
    lista_enlazada.append(3)


    print("append recursivamente")
    lista_enlazada.append_recursive(lista_enlazada.head, 99)

    print("append normal: ")
    lista_enlazada.append(4)
    lista_enlazada.append(5)
    lista_enlazada.append(6)


    lista_enlazada.print_list()

    print("imprimir recursivamente: ")
    lista_enlazada.print_list_recurive(lista_enlazada.head)
    print("------------------")


    
    print("buscar un valor en mi lista enlazada recursivamente: ")
    print(lista_enlazada.buscar_recursivamente(lista_enlazada.head, 5))



    print("-----------------------------------------------------------")
    print("buscar un valor en mi lista enlazada recursivamente: ")
    print(lista_enlazada.buscar_recursivamente(lista_enlazada.head, 9))



    print("encontrar mayor estructuradamente: ")
    print(lista_enlazada.encontrar_mayor())


    print("encontrar el valor mayor en mi lista enlazda recursivamente: ")
    print(lista_enlazada.encontrar_mayor_recurisvo(lista_enlazada.head))


    print("append recursive: ")
    lista_enlazada.append_recursive(lista_enlazada.head, 19)



    print("print the list recursively:")
    lista_enlazada.print_list_recurive(lista_enlazada.head)