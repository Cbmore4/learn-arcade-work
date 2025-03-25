class Cat():
    def __init__(self, age, weight, name):
        self.age=age
        self.name=name
        self.weight=weight

    def meow(self):
        print(self.name,"goes meow", self.name, 16)


class Monster():
    def __init__(self, health, name):
        self.health=health
        self.name=name


    def decrease_health(self, health):
        health-=4
        if health<1:
            print(self.name, "have been killed")
        else:
            print(self.name, "has",health,"health remaining")
new_cat=Cat(3, 16, "cat"
                   )
new_cat.meow()

new_monster=Monster(10, "John")
new_monster.decrease_health(10)


class Star:
    def __init__(self,name):
        self.name=name
    def star(self):
        print(self.name,  "A star is born!")
new_star=Star("Big Man")
new_star.star()
new_star=Star("A star is born!")
