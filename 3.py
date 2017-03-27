class bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:#如果饿
            print("Aaaaaah...")
            self.hungry = False#吃了一次，不饿
        else:
            print("No,thanks")

class songbird(bird):#鸟叫；超类为bird
    def __init__(self):
        super(songbird,self).__init__()
        self.sound = "squawk"

    def sing(self):
        print(self.sound)

sb = songbird()
sb.sing()
sb.eat()
sb.eat()
