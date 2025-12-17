class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def add_last(self, value):
        new_node = ListNode(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
    
    def add_first(self, value):
        new_node = ListNode(value, self.first)
        self.first = new_node
        if self.last is None:
            self.last = new_node
        self.length += 1

    def insert_at(self, position, value):
        if position < 0 or position > self.length:
            raise IndexError(f"Некорректная позиция: {position}")

        if position == 0:
            self.add_first(value)
            return

        if position == self.length:
            self.add_last(value)
            return

        current = self.first
        for _ in range(position - 1):
            current = current.next

        new_node = ListNode(value, current.next)
        current.next = new_node
        self.length += 1

    def delete_at(self, position):
        if position < 0 or position >= self.length:
            raise IndexError(f"Некорректная позиция: {position}")

        if position == 0:
            deleted_value = self.first.value
            self.first = self.first.next
            if self.first is None:
                self.last = None
            self.length -= 1
            return deleted_value

        current = self.first
        for _ in range(position - 1):
            current = current.next

        deleted_node = current.next
        current.next = deleted_node.next

        if deleted_node is self.last:
            self.last = current

        self.length -= 1
        return deleted_node.value

    def __iter__(self):
        current = self.first
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self.length

    def __repr__(self):
        values = list(self)
        return f"LinkedList({values})"


if __name__ == "__main__":
    print("Демонстрация работы связного списка")
    
    lst = LinkedList()

    lst.add_last(10)
    lst.add_last(20)
    lst.add_last(30)
    print("После добавления в конец:", list(lst))
    
    lst.add_first(5)
    print("После добавления в начало:", list(lst))
    
    lst.insert_at(2, 99)
    print("После вставки на позицию 2:", list(lst))
    
    deleted = lst.delete_at(3)
    print(f"Удален элемент на позиции 3: {deleted}")
    print("После удаления:", list(lst))
    
    print(f"Длина списка: {len(lst)}")
    print(f"Строковое представление: {repr(lst)}")
    
    print("\nИтерация по списку:")
    for item in lst:
        print(f"  - {item}")