from time import sleep


class Lazy:
    def __init__(self, cls):
        self.cls = cls
        self.object = None

    def __getattr__(self, item):
        if self.object is None:
            self.object = self.cls()
        return getattr(self.object, item)


class A:
    def __init__(self):
        sleep(10)

    def get(self):
        print("A")


class B:
    def __init__(self):
        sleep(2)

    def dr(self):
        return "B"





if __name__ == '__main__':
    a = Lazy(A)
    b = Lazy(B)
    print(b.dr())
