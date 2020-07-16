class Human( ):
    '''인간'''
    def create( name, weight ): # 다음 강의에서 자세히 설명
        person = Human()
        person.name = name
        person.weight = weight
        return person

    def eat( self ):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다".format(self.name, self.weight))

    def walk( self ):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다".format(self.name, self.weight))

person = Human.create("철수", 60.5)
person.eat()