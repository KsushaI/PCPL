from random import randint

def gen_random(num_count, begin, end):
    gener = (f', зарплата {randint(begin, end)} руб.' for i in range(num_count))
    return gener
def main():
    gener=gen_random(5, 1, 3)
    for i in gener:
        print(i, end=' ')
