class Node:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True

        node = self.root
        while True:
            if start >= node.end:
                if node.right is None:
                    node.right = Node(start, end)
                    return True
                node = node.right
            elif end <= node.start:
                if node.left is None:
                    node.left = Node(start, end)
                    return True
                node = node.left
            else:
                return False

if __name__ == '__main__':
    my_calendar = MyCalendar()

    assert my_calendar.book(10, 20) is True
    assert my_calendar.book(15, 25) is False
    assert my_calendar.book(20, 30) is True
