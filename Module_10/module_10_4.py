from queue import Queue
from time import sleep
from threading import Thread
import random


# def getter(queue):
#     while True:
#         time.sleep(2)
#         item = queue.get()
#         print(threading.current_thread(), 'взял элемент', item)
#
#
# q = Queue(maxsize=10)
# thread1 = threading.Thread(target=getter, args=(q,), daemon=True)
# thread1.start()
#
# for i in range(10):
#     time.sleep(5)
#     q.put(i)
#     print(threading.current_thread(), 'положил в очередь элемент', i)

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        eat = random.randint(3, 10)
        sleep(eat)


class Cafe(Table):
    list_thr = []

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)


    def guest_arrival(self, *guests):
        list_guests = list(guests)
        list_tables = self.tables
        amount_guests = len(list_guests)
        free_tables = min(amount_guests, len(self.tables))
        for i in range(free_tables):
            list_tables[i].guest = guests[i]
            thr1 = guests[i]
            thr1.start()
            Cafe.list_thr.append(thr1)
            print(f'{list_guests[i].name} сел(-a) за стол номер {list_tables[i].number}')
        if amount_guests > free_tables:
            for i in range(free_tables, amount_guests):
                self.queue.put(guests[i])
                print(f'{list_guests[i].name} в очереди')

    def discuss_guests(self):
        while not (self.queue.empty()) or Cafe.check_table(self):
            for table in self.tables:
                if not (table.guest is None) and not (table.guest.is_alive()):
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if (not (self.queue.empty())) and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    thr1 = table.guest
                    thr1.start()
                    Cafe.list_thr.append(thr1)

    def check_table(self):
        for table in self.tables:
            if table.guest is not None:
                return True
        return False

tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

for thr in Cafe.list_thr:
    thr.join()