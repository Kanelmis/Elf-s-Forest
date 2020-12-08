#!/usr/bin/python
_author_ = "Zihan"
_copyright_ = "Copyright 2018, Computer Science"

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import time


# declare variables
# Font Style
FONT_ONE = ("times bold italic", 48)
FONT_TWO = ("times italic", 16)
FONT_THREE = ("times bold", 16)
FONT_FOUR = ("times", 16)
FONT_FIVE = ("times bold italic", 36)
FONT_SIX = ("times bold", 14)

# Stock level of books
# Book 1
SuperDude = 8
# Book 2
LizardMan = 12
# Book 3
WaterWoman = 3

# counter for work log
counterT = 1
counterL = 1


# pop up message
def popupmsg(msg):
    tk.messagebox.showinfo("Notifications", msg)


# main root
class Elfapp():
    # initalize the class
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack(side="top")

        # create menu
        self.menubar = Menu(master)
        self.fileMenu = Menu(self.menubar, tearoff=0)
        # add label for the menu bar
        self.fileMenu.add_command(label="Testing", command=lambda: popupmsg("Not supported yet"))
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=quit)
        self.menubar.add_cascade(label="File", menu=self.fileMenu)
        self.master.config(menu=self.menubar)

        # Title for the home page
        self.label = Label(self.frame, text="""Elf's Forest""", font=FONT_ONE, fg="#33cccc")
        self.label.pack(pady=110)

        # button to enter to the main program
        self.buttonStart = Button(self.frame, text="Start",
                                  command=self.showMainPage)
        self.buttonStart.pack()

    # show next window
    def showMainPage(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = Mainpage(self.newWindow)


class Mainpage():
    def __init__(self, master):
        # declare variables
        # Time
        self.localtime = time.asctime(time.localtime(time.time()))

        self.master = master

        #set the size of interface
        self.master.geometry("550x410+400+200")

        #make window not resizable
        self.master.resizable(width=False, height=False)

        # Top frame
        self.frameTop = Frame(self.master, width=550, height=100)

        # Title
        labelTitle = Label(self.frameTop, text="Elf's Forest", font=FONT_ONE, fg='#33cccc', width=23,
                           anchor="center")
        labelTitle.grid(row=0, columnspan=4, sticky="ew")

        # Timers for local time
        labelLocalTime = Label(self.frameTop, text=self.localtime, font=FONT_TWO, fg='#66cccc',
                               anchor="center")
        labelLocalTime.grid(row=1, columnspan=4, sticky="ew")

        # separator for title
        SeparatorT = ttk.Separator(self.frameTop, orient="horizontal")
        SeparatorT.grid(row=2, columnspan=4, sticky="ew")

        # Pack Frame Top
        self.frameTop.grid(row=0, columnspan=2, sticky="ew")

        # Left Frame
        self.frameLeft = Frame(self.master, width=275, height=100)

        # Nav for books
        labelNavBookName = Label(self.frameLeft, text="Book", fg="#111111", relief="sunken", font=FONT_THREE, width=20,
                                 anchor="center")
        labelNavBookName.grid(row=0, column=0, sticky="ew")
        # Display the name of the book
        labelBook1 = Label(self.frameLeft, text="Super Dude", fg="#111111", relief="groove", font=FONT_FOUR, width=20,
                           anchor="center")
        labelBook1.grid(row=1, column=0, sticky="ew")

        labelBook2 = Label(self.frameLeft, text="Lizard Man", fg="#111111", relief="groove", font=FONT_FOUR, width=20,
                           anchor="center")
        labelBook2.grid(row=2, column=0, sticky="ew")

        labelBook3 = Label(self.frameLeft, text="Water Woman", fg="#111111", relief="groove", font=FONT_FOUR, width=20,
                           anchor="center")
        labelBook3.grid(row=3, column=0, sticky="ew")

        # Row 2 Display the current stock level
        labelNavBookName = Label(self.frameLeft, text="Current Stock Level", fg="#111111", relief="sunken",
                                 font=FONT_THREE, width=18)
        labelNavBookName.grid(row=0, column=1, sticky="w")
        # The number of current stock
        labelBook1 = Label(self.frameLeft, text=SuperDude, font=FONT_FOUR, relief="groove", anchor="center", width=18)

        labelBook1.grid(row=1, column=1, sticky="ew")

        labelBook2 = Label(self.frameLeft, text=LizardMan, font=FONT_FOUR, relief="groove", anchor="center", width=18)

        labelBook2.grid(row=2, column=1, sticky="ew")

        labelBook3 = Label(self.frameLeft, text=WaterWoman, font=FONT_FOUR, relief="groove", anchor="center", width=18)

        labelBook3.grid(row=3, column=1, sticky="ew")

        # nav for Stock
        labelNavBookName = Label(self.frameLeft, text="Stock Book", fg="#111111", relief="sunken",
                                 font=FONT_THREE, width=14)
        labelNavBookName.grid(row=0, column=3, sticky="ew")

        # The number of current stock

        # set up the name of book
        buttonBookStock1 = tk.Button(self.frameLeft, text="Stock", font=FONT_FOUR, anchor="center",
                                     command=lambda: self.stockbook1("stock <<Super Dude>>"))
        buttonBookStock1.grid(row=1, column=3, sticky="ew")

        buttonBookStock2 = tk.Button(self.frameLeft, text="Stock", font=FONT_FOUR, anchor="center",
                                     command=lambda: self.stockbook2("stock <<Lizard Man>>"))
        buttonBookStock2.grid(row=2, column=3, sticky="ew")

        buttonBookStock3 = tk.Button(self.frameLeft, text="Stock", font=FONT_FOUR, anchor="center",
                                     command=lambda: self.stockbook3("stock <<Water Woman>>"))
        buttonBookStock3.grid(row=3, column=3, sticky="ew")

        # nav for Sell
        labelNavBookName = Label(self.frameLeft, text="Sell Book", fg="#111111", relief="sunken", font=FONT_THREE,
                                 width=14)
        labelNavBookName.grid(row=0, column=2, sticky="ew")

        # The number of current stock

        # set up the name of book
        buttonBookSell1 = tk.Button(self.frameLeft, text="Sell", font=FONT_FOUR, anchor="center",
                                    command=lambda: self.sellbook1("Sell one <<Super Dude>>"))
        buttonBookSell1.grid(row=1, column=2, sticky="ew")

        buttonBookSell2 = tk.Button(self.frameLeft, text="Sell", font=FONT_FOUR, anchor="center",
                                    command=lambda: self.sellbook2("Sell one <<Lizard Man>>"))
        buttonBookSell2.grid(row=2, column=2, sticky="ew")

        buttonBookSell3 = tk.Button(self.frameLeft, text="Sell", font=FONT_FOUR, anchor="center",
                                    command=lambda: self.sellbook3("Sell one <<Water Woman>>"))
        buttonBookSell3.grid(row=3, column=2, sticky="ew")

        # separator
        separator = ttk.Separator(self.frameLeft, orient="horizontal")
        separator.grid(row=4, columnspan=4, sticky="ew")

        # Grid Frame
        self.frameLeft.grid(row=1, columnspan=2, sticky="ew")

        # Separator Frame
        self.frameSepa = Frame(self.master, width=550, height=50, bg="#ccffff")
        self.labelF = Label(self.frameSepa, text="Log", font=FONT_FIVE, fg="#914114", bg="#ccffff")
        self.labelF.pack()

        # comment for log
        self.labelN = Label(self.frameSepa, text="log recent 5 times process", fg="#914114", bg="#ccffff")
        self.labelN.pack()
        self.frameSepa.grid(row=2, columnspan=2, sticky="ew")

        # set the sell log
        self.frameBoLeft = Frame(self.master, relief="sunken", bd=3)
        labelstockL = tk.Label(self.frameBoLeft, width=32, text="Sell Log", font=FONT_THREE, anchor="center")
        labelstockL.grid(row=0, column=0)

        #add separator with the nav and content
        separator = ttk.Separator(self.frameBoLeft, orient="horizontal")
        separator.grid(row=1, columnspan=1, sticky="ew")

        #set initial blank space
        # new counte
        rowCounter = 2
        columnCounter = 0
        label_String = ["labelblank1", "labelblank2", "labelblank3", "labelblank4", "labelblank5"]
        for s in label_String:
            s = tk.Label(self.frameBoLeft, text="", anchor="center")
            s.grid(row=rowCounter, column=columnCounter, sticky="ew")
            rowCounter += 1

        self.frameBoLeft.grid(row=3, column=0, sticky="ew")

        #stock log frame
        self.frameBoRight = Frame(self.master, relief="sunken", bd=3)
        labelsellL = tk.Label(self.frameBoRight, width=34, text="Stock Log", font=FONT_THREE, anchor="center")
        labelsellL.grid(row=0, column=0)

        #add the separator with the nav and content
        separator = ttk.Separator(self.frameBoRight, orient="horizontal")
        separator.grid(row=1, columnspan=1, sticky="ew")

        #set initial blank spaces
        # new counters
        rowCounter = 2
        columnCounter = 0
        label_String = ["labelblank5", "labelblank6", "labelblank7", "labelblank8", "labelblank9"]
        for s in label_String:
            s = tk.Label(self.frameBoRight, text="", anchor="center")
            s.grid(row=rowCounter, column=columnCounter, sticky="ew")
            rowCounter += 1

        self.frameBoRight.grid(row=3, column=1, sticky="ew")

    #stock SuperDude and log
    def stockbook1(self, msg):
        #get global variable
        global SuperDude
        global counterT
        #show notification message
        popupmsg(msg)

        try:
            #get data from input
            answer = simpledialog.askinteger("Notification", "How many books you want to stock")

            #text content
            text1 = "You've stock"
            text3 = "Super Dude"

            #if answer less or equal to 0 then ask user for confirmation
            if answer <= 0:
                #show error message
                popupmsg("Ypu really don't want to stock a book?")
            else:
                #display procession
                tk.messagebox.showinfo("Notification", "{} {} {}".format(text1, answer, text3))

                #change the value of SuperDude
                SuperDude += answer

                #counter +=1
                counterT += 1

                # new counters
                rowCounter = 2
                columnCounter = 0
                label_String = ["labelblank5", "labelblank6", "labelblank7", "labelblank8", "labelblank9"]

                #when counter greater than 6 then reset the log
                if counterT > 6:
                    for s in label_String:
                        s = tk.Label(self.frameBoRight, text="", anchor="center")
                        s.grid(row=rowCounter, column=columnCounter, sticky="ew")
                        rowCounter += 1
                    #reset the counter
                    counterT = 2

                #change expression of the numbers of book
                labelBook1 = tk.Label(self.frameLeft, text=SuperDude, relief="groove", font=FONT_FOUR, anchor="center")
                labelBook1.grid(row=1, column=1, sticky="ew")

                #log
                label = tk.Label(self.frameBoRight, text="{} {} {}".format("stocked", answer, text3),
                                 font=FONT_SIX, anchor="center")
                label.grid(row=counterT, column=0)

        #Display error message
        except TypeError:
            #show error
            popupmsg("Ypu really don't want to stock a book?")

    #stock LizardMan and log
    def stockbook2(self, msg):
        #get global variables
        global LizardMan
        global counterT
        #show notifications
        popupmsg(msg)

        try:
            #get data from input
            answer = simpledialog.askinteger("Notification", "How many books you want to stock")

            #text content
            text1 = "You've stock"
            text3 = "Lizard Man"

            #if answer less or equal to 0 then ask for confirmation
            if answer <= 0:
                popupmsg("You really don't want to stock a book?")

            else:
                #show information
                tk.messagebox.showinfo("Notification", "{} {} {}".format(text1, answer, text3))

                #change value of book and counters
                LizardMan += answer
                counterT += 1

                #when counter greater than 6 then reset then log
                if counterT > 6:
                    # new counters
                    rowCounter = 2
                    columnCounter = 0
                    label_String = ["labelblank5", "labelblank6", "labelblank7", "labelblank8", "labelblank9"]
                    for s in label_String:
                        s = tk.Label(self.frameBoRight, text="", anchor="center")
                        s.grid(row=rowCounter, column=columnCounter, sticky="ew")
                        rowCounter += 1
                    counterT = 2

                #change the output of the number of books
                labelBook2 = tk.Label(self.frameLeft, text=LizardMan, relief="groove", font=FONT_FOUR, anchor="center")
                labelBook2.grid(row=2, column=1, sticky="ew")

                #log
                label = tk.Label(self.frameBoRight, text="{} {} {}".format("stocked", answer, text3), font=FONT_SIX,
                                 anchor="center")
                label.grid(row=counterT, column=0)

        #show error message
        except TypeError:
            popupmsg("Ypu really don't want to stock a book?")

    #stock WaterWoman
    def stockbook3(self, msg):
        #get global variables
        global WaterWoman
        global counterT
        #show notification
        popupmsg(msg)

        try:
            #get the data from the input
            answer = simpledialog.askinteger("Notification", "How many books you want to stock")

            #set the text content
            text1 = "You've stock"
            text3 = "Water Woman"

            #when answer less or equal to 0 then ask the confirmation
            if answer <= 0:
                #show message
                popupmsg("Ypu really don't want to stock a book?")

            #stock
            else:
                #show detail of stock
                tk.messagebox.showinfo("Notification", "{} {} {}".format(text1, answer, text3))

                #change the value of the variables
                WaterWoman += answer
                counterT += 1

                #when counter greater than 6 then reset the log
                if counterT > 6:
                    # new counters
                    rowCounter = 2
                    columnCounter = 0
                    label_String = ["labelblank6", "labelblank7", "labelblank8", "labelblank9", "labelblank10"]
                    for s in label_String:
                        s = tk.Label(self.frameBoRight, text="", anchor="center")
                        s.grid(row=rowCounter, column=columnCounter, sticky="ew")
                        rowCounter += 1

                    counterT = 2

                #change the expression of the WaterWoman
                labelBook3 = tk.Label(self.frameLeft, text=WaterWoman, relief="groove", font=FONT_FOUR, anchor="center")
                labelBook3.grid(row=3, column=1, sticky="ew")

                #log
                label = tk.Label(self.frameBoRight, text="{} {} {}".format("stocked", answer, text3), font=FONT_SIX,
                                 anchor="center")
                label.grid(row=counterT, column=0)

        #show error message
        except TypeError:
            popupmsg("Ypu really don't want to stock a book?")

    #sell book super dude
    def sellbook1(self, msg):
        popupmsg(msg)
        answer = tk.messagebox.askquestion("Notification", "Do you want to sell  1  book ")
        text3 = "Super Dude"

        #ask for confirmation
        if answer == 'yes':
            #get the global variable
            global SuperDude
            global counterL

            #check the stock
            #if have books left
            if SuperDude > 0:
                #change variables
                SuperDude -= 1
                #show message
                popupmsg("You've sold 1 Super Dude")
                #update the data of SuperDude
                labelBook1 = tk.Label(self.frameLeft, text=SuperDude, relief="groove", font=FONT_FOUR, anchor="center")
                labelBook1.grid(row=1, column=1, sticky="ew")

                counterL += 1

                #if counters greater than 6 then reset the log
                if counterL > 6:
                    # new counters
                    rowCounter = 2
                    columnCounter = 0
                    label_String = ["labelblank1", "labelblank2", "labelblank3", "labelblank4", "labelblank5"]
                    for s in label_String:
                        s = tk.Label(self.frameBoLeft, text="", anchor="center")
                        s.grid(row=rowCounter, column=columnCounter, sticky="ew")
                        rowCounter += 1
                    #reset the counter
                    counterL = 2

                #log
                label = tk.Label(self.frameBoLeft, text="{} {}".format("sold one", text3), font=FONT_SIX,
                                 anchor="n")
                label.grid(row=counterL, column=0)

            #show error message
            else:
                popupmsg("there is no book left")

    #sell Lizard Man
    def sellbook2(self, msg):
        #show message
        popupmsg(msg)
        #get the input
        answer = tk.messagebox.askquestion("Notification", "Do you want to sell  1  book ")

        #set text content
        text3 = "Lizard Man"

        #ask them for confirmation
        if answer == 'yes':
            #get global variables
            global LizardMan
            global counterL

            #check whether any book left
            if LizardMan > 0:
                LizardMan -= 1
                popupmsg("You've sold one Lizard Man")

                #chaneg expression of the LizardMan
                labelBook2 = tk.Label(self.frameLeft, text=LizardMan, relief="groove", font=FONT_FOUR, anchor="center")
                labelBook2.grid(row=2, column=1, sticky="ew")

                counterL += 1

                # counter greater than 6 then reset the log
                if counterL > 6:
                    # new counters
                    rowCounter = 2
                    columnCounter = 0
                    label_String = ["labelblank1", "labelblank2", "labelblank3", "labelblank4", "labelblank5"]
                    for s in label_String:
                        s = tk.Label(self.frameBoLeft, text="", anchor="center")
                        s.grid(row=rowCounter, column=columnCounter, sticky="ew")
                        rowCounter += 1

                    counterL = 2

                #log
                label = tk.Label(self.frameBoLeft, text="{} {}".format("sold one", text3), font=FONT_SIX,
                                 anchor="n")
                label.grid(row=counterL, column=0)

            #else show error message
            else:
                popupmsg("there is no book left")

    #sell Water Woman
    def sellbook3(self, msg):
        #show notification
        popupmsg(msg)

        #ask for confirmation
        answer = tk.messagebox.askquestion("Notification", "Do you want to sell  1  book ")
        text3 = "Water Woman"

        #check the confirmation
        if answer == 'yes':

            #get the global variables
            global WaterWoman
            global counterL

            #check stock levels
            if WaterWoman > 0:
                #change the value of variables
                WaterWoman -= 1
                popupmsg("You've sold one Water Woman")

                #change the output of Water Woman
                labelBook3 = tk.Label(self.frameLeft, text=WaterWoman, relief="groove", font=FONT_FOUR, anchor="center")
                labelBook3.grid(row=3, column=1, sticky="ew")

                counterL += 1

                #when counter greater than 6 then reset the log
                if counterL > 6:
                    # new counters
                    rowCounter = 2
                    columnCounter = 0
                    label_String = ["labelblank1", "labelblank2", "labelblank3", "labelblank4", "labelblank5"]
                    for s in label_String:
                        s = tk.Label(self.frameBoLeft, text="", anchor="center")
                        s.grid(row=rowCounter, column=columnCounter, sticky="ew")
                        rowCounter += 1

                    counterL = 2

                #log
                label = tk.Label(self.frameBoLeft, text="{} {}".format("sold one", text3), font=FONT_SIX,
                                 anchor="n")
                label.grid(row=counterL, column=0)

            #else show error message 
            else:
                popupmsg("there is no book left")


#main loop
def main():
    #inital root
    root = Tk()
    root.title("Elf's Forest")
    Elfapp(root)
    #set size of interface
    root.geometry("720x460+300+200")

    #make size not resizable
    root.resizable(width=False, height=False)
    #run mainloop
    root.mainloop()


#run main loop
if __name__ == '__main__':
    main()
