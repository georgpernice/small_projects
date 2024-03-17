Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from turtle import*
for i in range(100):
    for j in range(100):
        pu()
        
        goto(i,j)
        pd()
        if i%2 == 0:
            color("green")
        else:
            color ("red")
        dot()

        
Traceback (most recent call last):
  File "<pyshell#5>", line 11, in <module>
    dot()
  File "<string>", line 8, in dot
  File "C:\Users\georg\AppData\Local\Programs\Python\Python310\lib\turtle.py", line 3392, in dot
    self.pensize(size)
  File "C:\Users\georg\AppData\Local\Programs\Python\Python310\lib\turtle.py", line 2092, in pensize
    self.pen(pensize=width)
  File "C:\Users\georg\AppData\Local\Programs\Python\Python310\lib\turtle.py", line 2459, in pen
    self._update()
  File "C:\Users\georg\AppData\Local\Programs\Python\Python310\lib\turtle.py", line 2662, in _update
    screen._update()                  # TurtleScreenBase
  File "C:\Users\georg\AppData\Local\Programs\Python\Python310\lib\turtle.py", line 561, in _update
    self.cv.update()
  File "C:\Users\georg\AppData\Local\Programs\Python\Python310\lib\tkinter\__init__.py", line 1343, in update
    self.tk.call('update')
KeyboardInterrupt
tracer(False);for i in range(100):
    for j in range(100):
        pu()
        
        goto(i,j)
        pd()
        if i%2 == 0:
            color("green")
        else:
            color ("red")
        dot()
        
SyntaxError: invalid syntax
tracer(False);for i in range(100):
    for j in range(100):
        pu()

        goto(i,j)
        pd()
        if i%2 == 0:
            color("green")
        else:
            color ("red")
        dot()
KeyboardInterrupt
def f():
    tracer(False)
    for i in range(100):
        for j in range(100):
            pu()
            
            goto(i,j)
            pd()
            if i%2 == 0:
                color("green")
            else:
                color ("red")
            dot()
    tracer(True)

    
f()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    f()
  File "<pyshell#11>", line 2, in f
    tracer(False)
  File "<string>", line 5, in tracer
turtle.Terminator
f()
def f():
    
    tracer(False)
    for i in range(100):
KeyboardInterrupt
>>> def f():
...     tracer(False)
...     for i in range(100):
...         for j in range(100):
...             pu()
...             
...             goto(i,j)
...             pd()
...             if i%2 == 0 or j%2 ==0:
...                 color("green")
...             else:
...                 color ("red")
...             dot()
...     tracer(True)
... 
...     
>>> f()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    f()
  File "<pyshell#15>", line 2, in f
    tracer(False)
  File "<string>", line 5, in tracer
turtle.Terminator
>>> f()
>>> def f():
...     tracer(False)
...     for i in range(100):
...         for j in range(100):
...             pu()
...             
...             goto(i,j)
...             pd()
...             if i%2 == 0 or j%2 ==0:
...                 color("lightgreen")
...             else:
...                 color ("red")
...             dot()
...     tracer(True)
