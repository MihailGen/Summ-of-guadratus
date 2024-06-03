from functools import reduce
numbers = [1, 2, 3, 4, 5, -2, -4]


def process_numbers(numbers):
    positive_numbers = list(filter(lambda x: x > 0, numbers))
    kvadratus = list(map(lambda x: x * x, positive_numbers))
    sum_of_kvadratus = reduce(lambda x, y: x + y, kvadratus)
    print(sum_of_kvadratus)
    return sum_of_kvadratus


# то же самое, если собрать в одну строку
def process_numbers_short(numbers):
    sum_of_kvadratus = reduce(lambda x, y: x + y, list(map(lambda x: x * x,
                                                           list(filter(lambda x: x > 0, numbers)))))
    print(sum_of_kvadratus)
    return sum_of_kvadratus


process_numbers(numbers)
process_numbers_short(numbers)