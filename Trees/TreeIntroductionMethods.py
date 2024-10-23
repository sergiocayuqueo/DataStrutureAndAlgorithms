class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = TreeNode(value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left == None:
                        current.left = TreeNode(value)
                        break
                    else:
                        current = current.left
                else:
                    if current.right == None:
                        current.right = TreeNode(value)
                        break
                    else:
                        current = current.right

    def print_pre_order(self, node):  # raiz, izquierda, derecha
        if node != None:
            print(node.value, end=" ")
            self.print_post_order(node.left)
            self.print_post_order(node.right)

    def print_in_order(self, node):  # izquierda, raiz, derecha
        if node != None:
            self.print_in_order(node.left)
            print(node.value, end=" ")
            self.print_in_order(node.right)

    def print_post_order(self, node):  # izquierda, derecha, raiz
        if node != None:
            self.print_post_order(node.left)
            self.print_post_order(node.right)
            print(node.value, end=" ")

    def count_nodes(self, node):
        if node == None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def buscar(self, value):
        current = self.root
        while current != None:
            if current.value == value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, value):
        parent = None
        current = self.root

        while current and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if current is None:
            return  # El valor no existe en el árbol

        # Caso 1: El nodo a eliminar no tiene hijos
        if current.left is None and current.right is None:
            if current != self.root:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None

        # Caso 2: El nodo a eliminar tiene dos hijos
        elif current.left and current.right:
            successor_parent = current
            successor = current.right

            while successor.left:
                successor_parent = successor
                successor = successor.left

            current.value = successor.value

            if successor_parent != current:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        # Caso 3: El nodo a eliminar tiene un solo hijo
        else:
            child = current.left if current.left else current.right

            if current != self.root:
                if current == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child


if __name__ == "__main__":

    tree = BinaryTree()

    n = int(input("Ingrese la cantidad de nodos: "))

    for i in range(n):
        value_node = int(input(f"Ingrese el valor del Nodo {i+1}: "))
        tree.insert(value_node)

#         n_1
#        /  \
#      n     n
#     / \   /  \
#    n   n n   n

    print("Print in Order: ")
    print("----------------------------------")
    tree.print_in_order(tree.root)
    print("----------------------------------")

    print("Print pre Order: ")
    print("----------------------------------")
    tree.print_pre_order(tree.root)
    print("----------------------------------")

    print("Print post Order: ")
    print("---------------------------------")
    tree.print_post_order(tree.root)
    print("---------------------------------")

    print("Cantidad de nodos que hay en àrbol binario: ")
    print("-------------------------------------------")
    print(tree.count_nodes(tree.root))
    print("-------------------------------------------")

    print("valor existe?")
    print("----------------------------------")
    print(tree.buscar(32))
    print("----------------------------------")

    print("Delete value: ")
    print("----------------------------------")
    tree.delete(19)
    print("----------------------------------")

    print("Print in Order: ")
    print("-----------------------------")
    tree.print_in_order(tree.root)
    print("-----------------------------")
