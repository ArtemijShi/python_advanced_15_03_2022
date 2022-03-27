from random import randint
import sys
# gfg


def countdown_1(num):
    lst = []
    while num > 0:
        lst.append(num - 1)
        num -= 1
    return lst


print(countdown_1(15))


def countdown_2(num):
    print('Start')
    while num > 0:
        yield num - 1
        num -= 1


# print(next(countdown_2(15)))
gen = countdown_2(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for value in countdown_2(10):
    print(value, end=" ")
print()


def random_gen(start, stop, cnt):
    from random import randint
    while cnt > 0:
        yield randint(start, stop)
        cnt -= 1


for value in random_gen(10, 99, 10):
    print(value, end=" ")
print()
print('-'*50)

some_list = [randint(10, 99) for _ in range(15)]
# print(some_list)
print(sys.getsizeof(some_list))

some_list_new = [value for value in some_list if value % 2 == 0]
# print(some_list_new)
print('-'*50)

gen = (value for value in some_list if value % 2 == 0)
print(sys.getsizeof(gen))
# print(type(gen), gen)
# for value in gen:
#     print(value, end=' ')
# print()
print('//'*40)

some_list_new1 = [value for value in range(100) if value % 2 == 0]
print(sys.getsizeof(some_list_new1))

gen1 = (value for value in range(100) if value % 2 == 0)
print(sys.getsizeof(gen1))
