class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def medio(self, start, end):
        slow = start
        fast = start

        # Find the middle element between start and end
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next
        return slow

    def binary_search(self, start, end, target):
        if start == end:
            print("Reached the end of the search range. Element not found.")
            return None

        # Find the middle node
        middle = self.medio(start, end)

        # Visualization of the current step
        start_data = start.data if start else "None"
        end_data = end.data if end else "None"
        middle_data = middle.data if middle else "None"
        print(
            f"\nSearching in range: Start={start_data}, Middle={middle_data}, End={end_data}")

        # Check if the middle node contains the target
        if middle.data == target:
            print(f"Element {target} found at node with value {middle.data}.")
            return middle
        elif middle.data < target:
            print(
                f"Target {target} is greater than {middle.data}. Searching in the right half.")
            # Recursively search in the right half
            return self.binary_search(middle.next, end, target)
        else:
            print(
                f"Target {target} is less than {middle.data}. Searching in the left half.")
            # Recursively search in the left half
            return self.binary_search(start, middle, target)


# Create the linked list and ask the user to input ordered data
if __name__ == '__main__':
    linked_list = LinkedList()
    n = int(input("Enter the number of nodes: "))
    print("Enter the data in ascending order:")
    for i in range(n):
        data = int(input(f"Node {i + 1}: "))
        linked_list.append(data)

    # Element to search for
    target = int(input("Enter the element to search for: "))

    # Perform binary search in the linked list
    result = linked_list.binary_search(linked_list.head, None, target)

    if result:
        print(f"Element {target} found in the linked list.")
    else:
        print(f"Element {target} not found in the linked list.")
