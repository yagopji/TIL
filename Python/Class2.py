# 클래스

# 클래스: 빵틀 (설계도)
# 오브젝트, 객체, 인스턴스: 빵

class Person:
    def __init__(self, name, age): # constructor
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"안녕하세요, 저는 {self.name} 입니다.")
        print(f"저는 {self.age}세 입니다.")

    def say_bye(self):
        print("안녕히 가세요~!")


# Tommy = Person("Tommy", 20) # 객체를 만드는 방법
# Jenny = Person("Jenny", 30)

# Tommy.say_hello()
# Jenny.say_hello()


# 상속

class Police(Person):
    def say_hello(self):
        print(f"안녕하세요, 저는 {self.name} 입니다. 그리고 제 직업은 경찰이에요.")

    def freeze(self):
        print("움직이지마!!!")

Suzi = Person("Suzi", 23)
James = Police("James", 35)

# Suzi.say_hello()
# James.say_hello()

# James.freeze()

# James.say_bye()