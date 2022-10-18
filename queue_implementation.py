class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, e):
        # agregar un elemento e a la cola
        self.queue.append(e)

    def dequeue(self):
        # remueve y retorna el primer elemento
        if (self.is_empty()):
            raise Exception("Cola vacía...")
        return self.queue.pop(0)

    def first(self):
        # retornar el primer elemento de la cola
        if (self.is_empty()):
            raise Exception("Cola vacía...")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):  # dunder method
        # retorna tamaño
        return len(self.queue)


class Letter:
    def __init__(self, letter, color):
        self.set_up = f'{color}{letter}[/]'
