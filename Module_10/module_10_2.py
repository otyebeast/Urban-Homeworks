import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        enemies = 100
        self.enemies = enemies
        days = 0
        self.days = days

    def day(self, name, power, enemies, days):
        while self.enemies > 0:
            time.sleep(1)
            self.days += 1
            self.enemies -= self.power
            print(f'{self.name} сражается {self.days} день(дня), осталось {self.enemies} воинов')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.day(self.name, self.power, self.enemies, self.days)
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Все битвы закончились')
