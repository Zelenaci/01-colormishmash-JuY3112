from os.path import basename, splitext
from tkinter import Scale, StringVar, HORIZONTAL, Canvas, LEFT, S, Frame, Entry, END
import tkinter as tk

class Application(tk.Tk):
    name = basename(splitext(basename(__file__))[0])
    name = "Míchání barev"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)

        self.bind("<Escape>", self.quit)

        self.frameR = Frame(self)
        self.frameR.pack()
        self.frameG = Frame(self)
        self.frameG.pack()
        self.frameB = Frame(self)
        self.frameB.pack()

        self.labelR = tk.Label(self.frameR, text="R")
        self.labelR.pack(side=LEFT, anchor=S)
        self.scaleR = Scale(self.frameR, from_=0, to=255, orient=HORIZONTAL, length= 256, command=self.change)
        self.scaleR.pack(side=LEFT, anchor=S)
        self.varR = StringVar()


        self.labelG = tk.Label(self.frameG, text="G")
        self.labelG.pack(side=LEFT)
        self.scaleG = Scale(self.frameG, from_=0, to=255, orient = HORIZONTAL, length= 256, command=self.change)
        self.scaleG.pack(side=LEFT)
        self.varG = StringVar()


        self.labelB = tk.Label(self.frameB, text="B")
        self.labelB.pack(side=LEFT)
        self.scaleB = Scale(self.frameB, from_=0, to=255, orient = HORIZONTAL, length= 256, command=self.change)
        self.scaleB.pack(side=LEFT)
        self.varB = StringVar()


        self.canvasMain = Canvas(self, width=256, height=128, background= "#000000")
        self.canvasMain.pack()
        self.entryMain = Entry(self, text="#000000")
        self.entryMain.pack(side=LEFT)

        self.buttonExit = tk.Button(self, text="Exit", command=self.quit)
        self.buttonExit.pack()



    def change(self, event):
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        colorcode = f"#{r:02x}{g:02x}{b:02x}"
        self.canvasMain.config(background=colorcode)
        self.entryMain.delete(0, END)
        self.entryMain.insert(0, colorcode)



    def quit(self, event=None):
        super().quit()

app = Application()
app.mainloop()