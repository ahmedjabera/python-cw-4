def my_name():
    print("My name is hassan")
my_name()


def my_meal(food, drink):
   print(f"I like to eat {food} and while drinking {drink}")

my_meal('machbos','mango')

def cube(number):
    return number ** 3
print(cube(3))

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        print(False)
print(by_three(4))