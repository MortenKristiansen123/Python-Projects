# Functions are reusables blocks of code. When we call a function it runs the block of code.
# Functions are all lowercase, if we wanted to separate words we can use an underscore.
def hello_world():
    print("Hello, world!")


hello_world()


def sum(num1, num2):
    print(num1 + num2)


# The paramiters never change, but the arguments can change with every function call.
sum(2, 3)  # 2 + 3 = 5
sum(8, 12)  # 8 + 12 = 20
sum(32, 48)  # 32 + 48 = 80


def sum1(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return "Error, please enter an integer when using this function."
    return num1 + num2


# If I change one of the values to something that isn't an int, it will return the error message.
# If I just had return with no else statement, it would return None in the terminal.
total = sum1(2, 3)
print(total)


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Morten", "Daniel", "Søren")


# kwargs stands for key word arguments.
def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(name="Morten", age=30, city="Copenhagen")
mult_named_items(first_name="Morten", last_name="Kristiansen")
