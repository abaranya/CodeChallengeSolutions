# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Solution import Solution


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    solutionObject = Solution()
    solutionObject.print_lines()
    solutionObject.open_input(r"C:\Users\Albaro\PycharmProjects\Solution\venv\input.txt")
    solutionObject.read_data()
    solutionObject.print_lines()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/