


class FlyBehavior(object):
    def __init__(self) -> None:
        pass

    def fly():
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        # fly with wings
        print("Flap Flap!")
        pass

class FlyNoWoay(FlyBehavior):
    def fly(self):
        # don't fly
        pass


class QuackBehavior(object):
    def __init__(self) -> None:
        pass

    def quack(self):
        pass


class Quack(QuackBehavior):
    def __init__(self):
        pass

    def quack(self):
        # do a quack
        print("Quack!")
        pass

class Duck(object):

    def __init__(self, fly_behavior: FlyBehavior, quack_behavior):
        
        self.FlyBehavior = fly_behavior
        self.QuackBehavior = quack_behavior

    def performQuack(self):
        self.QuackBehavior.quack()

    def performFly(self):
        self.FlyBehavior.fly()

    def swim(self):
        print("All ducks can swim")

class Mallard(Duck):

    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

    def display(self):
        print("Im a mallard duck")

class DuckSimulator():
    duck = Mallard()
    duck.performFly()
    duck.performQuack()
    duck.swim()
    duck.display()