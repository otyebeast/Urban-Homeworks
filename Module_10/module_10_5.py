from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start = datetime.now()

for i in filenames:
    read_info(i)

end = datetime.now()
print(f'{end - start} (линейный)')

if __name__ == '__main__':
    start1 = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end1 = datetime.now()
    print(f'{end1 - start1} (многопроцессный)')
