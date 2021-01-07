from tkinter import *
import sys

class Application(Frame):  # Application is a Frame (inheritance from Frame)
    def __init__(self, master):
        Frame.__init__(self, master) 
        self.grid(sticky=N+S+E+W) # put frame in toplevel window
        #self.createBackground()
        self.createWidgets()

    def commandHandler(self, bNo):
        print("Cmd handler called: " + str(bNo))

    def createBackground(self):
        #Gradient = PhotoImage(file = "C:\\Users\\tavss\\OneDrive\\Dokumenter\\GitHub\\Tkinter-Gui-Andegradsligning\\Gradient.png")
        background_label = Label(top, image=Gradient)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def createWidgets(self):
        top=self.winfo_toplevel()
        #top.geometry("500x500")
        top.rowconfigure(0, weight=1)     # toplevel window rows scalable
        top.columnconfigure(0, weight=1)  # toplevel window colums scalable

        # rows with minimum size and equal weights
        for row in range(0,6):
            self.rowconfigure(row, weight=1 , minsize=50)

        # columns with different scale
        for i in range(0,5):
            self.columnconfigure(i, weight=i, minsize=150)

        # create 3 labels and 3 inputs
        colors = ('#FA4EB2','#d1ff00','#DB3BE3','#d1ff00','#C142FD')    
        letter = ('A','error','B','error','C')
        for row in range(0,5):
            if (row % 2 != 1):
                l=Label(self, text=letter[row] + ' value', justify="left", bg=colors[row])
                l.grid(row=row, column=0, sticky=S+W+N+E)
                l2=Label(self,justify="left",bg=colors[row])
                l2.grid(row=row,column=1, stick=S+W+N+E)

                entryA = Entry(self)
                entryB = Entry(self)
                entryC = Entry(self)

                entryA.grid(row=0, column=1)
                entryB.grid(row=2, column=1)
                entryC.grid(row=4, column=1)
            #else:

        
        # create 3 buttons
        for i in range(2,5):
            self.columnconfigure(i, weight=i) # , minsize=200
            def cmd(no=i):  # hidden argument trick
                self.commandHandler(no)  
            Button(self, text=str(i), command=cmd).grid(row=5, column=i, sticky=N+S+E+W)

root = Tk()

app = Application(root)
app.master.title("QUADRATIC EQUATION SOLVER")
app.mainloop()