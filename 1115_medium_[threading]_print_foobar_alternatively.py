import threading

class FooBar:
    def __init__(self, n):
        self._n = n
        self._lock1 = threading.Lock()
        self._lock2 = threading.Lock()

        self._lock2.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self._n):
            self._lock1.acquire()
            printFoo()
            self._lock2.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self._n):
            self._lock2.acquire()
            printBar()
            self._lock1.release()

if __name__ == '__main__':
    foo_bar = FooBar(10)

    t1 = threading.Thread(target=foo_bar.foo, args=(lambda: print('foo'),))
    t2 = threading.Thread(target=foo_bar.bar, args=(lambda: print('bar'),))

    t1.start()
    t2.start()
