class bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:#如果饿
            print("Aaaaaah...")
            self.hungry = False#吃了一次，不饿
        else:
            print("No,thanks")

b = bird()

b.eat()

b.eat()
