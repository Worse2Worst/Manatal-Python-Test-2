import random

# from 1 to 50
all_numbers = list(range(1, 51))
winners = random.sample(all_numbers, 10)
winners.sort()
print(f'From numbers 1 - 50, the winning numbers are: {winners}')
