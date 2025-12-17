from collections import deque

class MyStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class MyQueue:
    def __init__(self):
        self.items = deque()

    def add(self, item):
        self.items.append(item)

    def remove(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items.popleft()

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


if __name__ == "__main__":
    print("Тестирование стека:")
    stack = MyStack()
    
    print("Пустой ли стек?", stack.is_empty())
    
    stack.push(5)
    stack.push(15)
    stack.push(25)
    
    print("Верхний элемент:", stack.top())
    print("Извлекаем:", stack.pop())
    print("Извлекаем:", stack.pop())
    print("Размер стека:", stack.size())
    print("Пустой ли стек?", stack.is_empty())
    
    print()
    
    print("Тестирование очереди:")
    queue = MyQueue()
    
    print("Пустая ли очередь?", queue.is_empty())
    
    queue.add("первый")
    queue.add("второй")
    queue.add("третий")
    
    print("Первый в очереди:", queue.front())
    print("Забираем:", queue.remove())
    print("Забираем:", queue.remove())
    print("Осталось элементов:", len(queue))
    print("Пустая ли очередь?", queue.is_empty())