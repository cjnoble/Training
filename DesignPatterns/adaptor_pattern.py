



class Duck(object):

    def __init__(self) -> None:
        pass

    def quack(self):
        pass

    def fly(self):
        pass


class MallardDuck(Duck):
    def __init__(self) -> None:
        pass


class TurkeyAdaptor(Duck):
    def __init__(self, turkey) -> None:
        self.turkey = turkey
        super().__init__()

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(10):
            self.turkey.fly()


class Turkey(object):
    def __init__(self) -> None:
        pass

    def gobble(self):
        pass

    def fly(self):
        pass

class DuckSimulator(object):
    def __init__(self) -> None:
        duck = MallardDuck()
        self.test_duck(duck)

        wild_turkey = Turkey()
        turkey_adaptor = TurkeyAdaptor(wild_turkey)
        self.test_duck(turkey_adaptor)

    def test_duck(self, duck):
        duck.quack()
        duck.fly()

DuckSimulator()