# class Fruit():
#     def __init__(self, name, color, weight):
#         self.name = name 
#         self.color = color
#         self.weight = weight
#     def info(self):
#         print(f"Fruit {self.name} , {self.color}, {self.weight}")
        
# apple = Fruit('- apple', 'red', '10')
# apple.info()        

# avocado = Fruit('- avocado', 'green', '10000000000000')
# avocado.info()        

class Herous():
    def __init__(self,name,role):
        self.name = name
        self.role = role
        self.is_start = True
        self.health = 30
    def info(self):
        print(f'Имя героя- {self.name}\nРоль- {self.role} \nЗдоровье- {self.health}')
    def fight(self):
        if self.health > 20:
            self.is_start == True
            print('Бой начался')
        else :
            print('Володя умер')
            
    def hp(self):
        health_now = self.health - 20
        print(f'У {self.name} , {health_now} здоровья')

    def stop(self):
        if self.health >0:
            print("Бой закончился")
        else:
            print("Драки небыло")

volodya = Herous('Володя', 'Боец')
volodya.info()

volodya.fight()

volodya.hp()

volodya.stop()
