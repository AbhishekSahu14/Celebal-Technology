class Node:
    def __init__(self, data):
        self.data =data
        self.next =None


class LinkedList:
    def __init__(self):
        self.head =None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next =new_node

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return
        current =self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        if not self.head:
            raise Exception("Cannot delete from an empty list.")

        if n <= 0:
            raise Exception("Index must be 1 or greater.")

        if n == 1:
            print(f"Deleting node at position {n} with value {self.head.data}")
            self.head = self.head.next
            return

        current = self.head
        count =1
        while current and count< n-1:
            current = current.next
            count += 1

        if not current or not current.next:
            raise Exception("Index out of range.")

        print(f"Deleting node at position {n} with value {current.next.data}")
        current.next = current.next.next

def main():
    ll = LinkedList()
    while True:
        print("\n--- LinkedList Menu ---")
        print("1. Add a node")
        print("2. Print the list")
        print("3. Delete the Nth node")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice=='1':
            data = int(input("Enter the value to add: "))
            ll.add_node(data)
            print("Node added successfully.")

        elif choice=='2':
            print("LinkedList contains: ")
            ll.print_list()

        elif choice=='3':
            try:
                n = int(input("Enter the position to delete(1-based index): "))
                ll.delete_nth_node(n)
            except Exception as e:
                print(f"Error: {e}")

        elif choice=='4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()