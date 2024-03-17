
""" This Program draws a rotating spiral."""
import tkinter as tk
import math
from random import random
# Dear user, you can just adapt those for capitalized variables and so adapt the program.
# colors
SPIRAL_FILLCOLOR = "black"
SPIRAL_OUTLINE = "gray14"
# words
WORDS = ["Beleidigung", "stress", "Hunger", "Leid","Gewalt"]
WORDCOLORS = ["grey1", "grey33", "grey55", "grey66", "white", "grey99"]
# spiral geometry
SPIRAL_LENGTH = 1000
SPIRAL_SEGMENTATION_FACTOR = 4 # factor > 1 means spiral consists out of fewer elements
SPIRAL_RING_DISTANCE = 10

# the rest is not for users
class SpiralDrawer:
    def __init__(self, master):
        self.master = master    
        self.canvas = tk.Canvas(master , background="black",width=600, height=600)
        self.spiral_size = (80,250)
        self.spiral_grow_speed = 8
        self.angle = 0
        self.center_x = 300
        self.center_y = 300
        self.radius = SPIRAL_RING_DISTANCE
        self.increment = -0.1
        self.word_radius = [150, 320, 150, 250, 300, 350, 150] 
        self.words = WORDS
        self.colors = WORDCOLORS
        
        self.canvas.pack()
        self.rotate_spiral(size=self.spiral_size[0])
        self.rotate_words()

    def rotate_spiral(self, size = 4, increasing = True):
        """Draw spiral recursively calling itself and thus pulsing / rotating."""
        self.angle += self.increment
        self.canvas.delete("all")
        # draw spiral of ovals
        for i in range(SPIRAL_LENGTH):
            angle = math.radians(i) * SPIRAL_SEGMENTATION_FACTOR
            x = self.center_x + self.radius * angle * math.cos(angle + self.angle)
            y = self.center_y + self.radius * angle * math.sin(angle + self.angle)
            self.canvas.create_oval(x -size, y-size, x+size, y+size, fill=SPIRAL_FILLCOLOR, outline=SPIRAL_OUTLINE)
        # handle pulsing spiral size
        min, max = self.spiral_size
        inc = self.spiral_grow_speed
        size = size + inc if increasing else size - inc
        if increasing and size > max:
            increasing = False
        if not increasing and size < min:
            increasing = True
        self.master.after(40, self.rotate_spiral, size, increasing)

    def rotate_words(self):
        self.angle += self.increment
        self.canvas.delete("text")
        for layer, color in zip(self.word_radius, self.colors):
            for i, word in enumerate(self.words):
                angle = math.radians(i * 72 + self.angle * 10)
                x = self.center_x + layer * math.cos(angle)
                y = self.center_y + layer * math.sin(angle)
                if layer > self.radius:
                    layer -= 1
                else:
                    layer = 600
                fontsize = 10+ i + math.trunc(random()*10)
                self.canvas.create_text(x, y, text=word, font=("Comic Sans MS", fontsize), fill=color, tags="text")
        self.master.after(100, self.rotate_words)
    def mainloop(self):
        print("hey")
def main():
    root = tk.Tk()
    root.title("Rotating Spiral with Multiple Layers of Words")
    
    SpiralDrawer(root)

    
    
    
    root.mainloop()

if __name__ == "__main__":
    main()
