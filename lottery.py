import random


def draw_lottery():
    # numbers is a list contains 1 to 50
    numbers = list(range(1, 51))
    winners = random.sample(numbers, 10)
    winners.sort()
    return winners
