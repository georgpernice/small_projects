from turtle import*

fillcolor("lightgrey")


def move(pos):
    pu()
    goto(pos)
    pd() 

class Balken:
    def __init__(self, length, diameter, position):
        self.length = length
        self.diameter = diameter
        self.position = position
        pu()
        goto(position[0] - length/2, position[1] - diameter/2)
        pd()
        setheading(0)
        begin_fill()
        for i in range(2):
            fd(length)
            lt(90)
            fd(diameter)
            lt(90)
        end_fill()
        move(position)
    
        
##        angle = 30
##        lt(angle)
##        circle(diameter/4,(90-angle)*2)
##        #rt(angle)
##        circle(-diameter/4,(90-angle)*2)
##        lt(180)
##        circle(diameter/4,(90-angle)*2)


tracer(False)
# draw stuff
balken1 = Balken(length=300,
                 diameter = 100,
                 position = (0,0)
                 )






tracer(True)
