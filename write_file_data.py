import os

cwd = os.getcwd()

test_data = "Hello world! Part 2"

with open(os.path.join(cwd, 'test_meals.csv'), 'a') as file:
    file.write(test_data)