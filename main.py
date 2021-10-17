# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    num1 = numpy.array([[1, 1], [2, 2]])
    num2 = numpy.array([[3, 3], [2, 2]])
    num = num1 - num2
    print(num)
    num = num1 + num2
    print(num)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
