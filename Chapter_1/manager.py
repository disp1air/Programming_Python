from person import Person

class Manager(Person):
    def giveRaise(self, percent, bonus = 0.1):
        self.pay *= (1 + percent + bonus)

if __name__ == '__main__':
    tom = Manager('Tom Taylor', age = 50, pay = 50000)
    print(tom.lastName())
    tom.giveRaise(0.20)
    print(tom.pay)
    print(tom)