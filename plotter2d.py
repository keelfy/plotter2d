import numpy as np
import fourFn as fn
from fourFn import BNF
import matplotlib.pyplot as plt

# Queue to draw with of function's XY coordinates + Color
class Queue:
    def __init__(self):
        self.x_values = []
        self.y_values = []
        self.colors = []

    def is_empty(self):
        return self.x_values == [] and self.y_values == [] and self.colors == []

    def add(self, x_values, y_values, color):
        self.x_values.append(x_values)
        self.y_values.append(y_values)
        self.colors.append(color)

    def length(self):
        return len(self.x_values)

    def clear(self):
        self.x_values.clear()
        self.y_values.clear()
        self.colors.clear()

# Function data representation
class Function:
    def __init__(self, text, start, end, accuracy, color):
        self.text = text
        self.start = start
        self.end = end
        self.accuracy = accuracy
        self.color = color

# Calculates X values for function
# With the specific borders and accuracy
def calculate_x_values(start=0, end=10, accuracy=0):
    if accuracy <= 0:
        accuracy = (end - start) * 10

    x_values = np.linspace(start, end, accuracy)
    return x_values

# Calculates Y values for function based on X values
def calculate_y_values(x_values, expression):
    expression = expression.replace('X', 'x')
    y_values = []

    for x in x_values:
        fn.exprStack = []
        try:
            BNF().parseString(expression.replace('x', str(x)), parseAll=True)
            x_value = fn.evaluate_stack(fn.exprStack)
        except fn.ParseException as pe:
            print(expression, "failed parse:", str(pe))
            return 0
        except Exception as e:
            print(expression, "failed eval:", str(e), fn.exprStack)
            return 0

        y_values.append(x_value)

    return y_values

# Creates canvas with axes
def create_figure_canvas(start=0, end=10):
    plt.cla()
    figure_canvas = plt.figure()
    axes = figure_canvas.add_subplot(111)
    axes.set_xlim(start, end)
    axes.set_ylim(start, end)
    axes.grid(True)
    axes.set_xlabel('Аргумент')
    axes.set_ylabel('Функция')
    return figure_canvas, axes

# Draws all functions from queue
def draw(function_queue, axes):
    for i in range(0, len(function_queue.y_values)):
        try:
            axes.plot(function_queue.x_values[i], function_queue.y_values[i], color=str(function_queue.colors[i]))
        except Exception as e:
            print('There is incorrect functions in list ', e)

# Adds function to draw queue
def add_function(expression, function_queue, x_values, color):
    try:
        y_values = calculate_y_values(x_values, expression)
    except Exception as e:
        print('Incorrect input')
    else:
        function_queue.add(x_values, y_values, color)

# Edits function in queue by index
def edit_function(index, expression, function_queue, x_values, color):
    try:
        y_values = calculate_y_values(x_values, expression)
    except Exception as e:
        print('Incorrect input')
    else:
        function_queue.x_values[index] = x_values
        function_queue.y_values[index] = y_values
        function_queue.colors[index] = color

# Clears drawing queue
def clear_all(function_queue, axes):
    length = len(axes.lines)
    for i in range(length):
        axes.lines[0].remove()
    function_queue.clear()

# Validates text as math expression
def validate_text(text):
    try:
        BNF().parseString(text.replace('x', str(0)), parseAll=True)
        fn.evaluate_stack(fn.exprStack)
        print('validated')
    except fn.ParseException as pe:
        print(text, "failed parse:", str(pe))
        return False
    except Exception as e:
        print(text, "failed eval:", str(e), fn.exprStack)
        return False
    return True

# Creates screenshot (just cuz' why not?)
def screenshot(figure_canvas):
    figure_canvas.savefig('example.png')
