class Computers:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu
    
    @property
    def memory(self):
        return self.__memory
        
    def __make_computations(self):
        print(f"процессор {self.cpu}, и память {self.memory}\nумножение {self.cpu * self.memory}\nсложение  {self.cpu + self.memory}\nделение {self.cpu / self.memory}\nвычитание{self.cpu - self.memory}")
    @property
    def make (self):
        return self.__make_computations
    
lenovo = Computers(2132, 2142)
lenovo.make()     




class Laptop(Computers):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card

    @property
    def memory_card(self):
        return self.__memory_card
    
    def info(self):
        print(f"процессор {self.cpu}, и память {self.memory}, карта памяти {self.memory_card}")




asus = Laptop(6, 1000, 500)
asus.info()
asus.make()








    
        

