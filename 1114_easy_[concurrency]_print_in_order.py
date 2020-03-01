import threading

class Foo:
    def __init__(self):
        self._second_event = threading.Event()
        self._third_event = threading.Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self._second_event.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self._second_event.wait()
        printSecond()
        self._third_event.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self._third_event.wait()
        printThird()