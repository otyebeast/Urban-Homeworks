# class Human:
#     def __init__(self, name, group):
#         self.name = name
#         super().__init__(group)
#         super().about()
#
#     def info(self):
#         print(f'Hello, my name is {self.name}')
#
#
# class StudentGroup:
#     def __init__(self, group):
#         self.group = group
#
#     def about(self):
#         print(f'{self.name} studing in group {self.group}')
#
#
# class Student(Human, StudentGroup):
#     def __init__(self, name, place, group):
#         super().__init__(name, group)
#         self.place = place
#         super().info()
#
#
# # human = Human('Dimas')
# # print(human.name)
# student = Student('Dimas', 'Urban', 'Python-1')
class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()