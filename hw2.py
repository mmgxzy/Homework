class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
        
    def inroduce(self):
        print(f'имя- {self.fullname} возраст- {self.age} женат- {self.is_married}')
        
kim_chen_yn = Person('Ким-чин-ин', 56, 'да') 
kim_chen_yn.inroduce()

class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.selery = 0
        
    def balans(self):
        for i in range(self.experience):
            self.selery += 3000
        print(f'имя- {self.fullname} возраст- {self.age} женат- {self.is_married} , зарплата - {self.selery}')

teaghers_selery = Teacher('Jarkynai', 45, 'да', 3)
teaghers_selery.balans()