"""Реализуйте в классе функцию для вставки нового элемента в дерево по
следующим правилам:
• Левое поддерево узла содержит только узлы со значениями меньше,
чем значение в узле.
• Правое поддерево узла содержит только узлы со значениями меньше,
чем значение в узле.
• Каждое из левого и правого поддеревьев также должно быть
бинарным деревом поиска.
• Не должно быть повторяющихся узлов.
Метод вставки сравнивает значение узла с родительским узлом и решает
куда доваить элемент (в левое или правое поддерево). Перепишите, метод
PrintTree для печати полной версии дерева."""
from queue import Queue


class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data > self.data:
            if self.right is None:
                self.right = Tree(data)
            else:
                self.right.insert(data)
        elif data < self.data:
            if self.left is None:
                self.left = Tree(data)
            else:
                self.left.insert(data)
        else:
            raise Exception("This data has already exist")

    def print_tree(self):
        children = Queue()
        children.put(self)
        while not children.empty():
            cur_tree = children.get()
            if cur_tree.left is not None:
                children.put(cur_tree.left)
            if cur_tree.right is not None:
                children.put(cur_tree.right)
            print(cur_tree.data)
