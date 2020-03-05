# Description
My project for University, I did it in a couple days and may be will be developed in a future  
![Screenshot](/Screenshot.png)

# Stack
- pyqt 5 (user interface)
- pyparsing (parsing math expressions into executable code)
- matplotlib (plotting)
- numpy (calculating values)

# Features
 It can plot a lot of math expressions like `cos(x)-3+arctg(x+10)` or `(log(x) + 100) / 2.3`

# Acceptable operations
"+": operator.add
"-": operator.sub
"*": operator.mul
"/": operator.truediv
"^": operator.pow

# Acceptable functions
"sin": math.sin
"cos": math.cos
"tg": math.tan
"tan": math.tan
"ctg": mpmath.cot
"arcsin": math.asin
"arccos": math.acos
"arctg": math.atan
"arctan": math.atan
"arcctg": mpmath.acot
"exp": math.exp
"abs": abs
"trunc": lambda a: int(a)
"round": round
"log": math.log
"lg": math.log10
"sgn": lambda a: -1 if a < -epsilon else 1 if a > epsilon else 0

# Acceptable constants
E - epsilon
PI - 3.1415...blahblah
