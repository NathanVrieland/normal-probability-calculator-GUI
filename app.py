""" app.py
author: Nathan Vrieland
GUI for normal probability calculator I wrote in go
"""
import tkinter as tk
from subprocess import run
from os.path import exists
from platform import system

class App:

    def __init__(self, window):
        if system() == 'Windows':
            self.runcode = '.\\'
            self.executable = 'calculate.exe'
        else:
            self.runcode = './'
            self.executable = 'calculate'

        # declare instance variables
        self.window = window
        self.mean = tk.StringVar(value='0')
        self.stDev = tk.StringVar(value='1')
        self.x0 = tk.StringVar()
        self.x1 = tk.StringVar()
        self.answer = tk.StringVar()
        self.answerOut = False

        # declare widgets
        calcButton = tk.Button(text="calculate", command=self.__calculate)
        self.answerLabel = tk.Label(textvariable=self.answer)

        meanLabel = tk.Label(text='mean')
        stDevLabel = tk.Label(text='standard deviation')
        x0Label = tk.Label(text='x0')
        x1Label = tk.Label(text='x1')

        meanEntry = tk.Entry(textvariable=self.mean)
        stDevEntry = tk.Entry(textvariable=self.stDev)
        x0Entry = tk.Entry(textvariable=self.x0)
        x1Entry = tk.Entry(textvariable=self.x1)

        # pack widgets
        meanLabel.grid(column=0, row=0)
        stDevLabel.grid(column=0, row=1)
        x0Label.grid(column=0, row=2)
        x1Label.grid(column=0, row=3)

        meanEntry.grid(column=1, row=0)
        stDevEntry.grid(column=1, row=1)
        x0Entry.grid(column=1, row=2)
        x1Entry.grid(column=1, row=3)

        calcButton.grid(column=0, row=5, columnspan=2)

        # other stuff
        self.__checkCompile()
        self.window.mainloop()

    def __checkCompile(self):  # this only works when I run from terminal :/
        if not exists(self.executable):
            try:
                run(['go', 'build', 'calculate.go', 'reimann.go'])
            except FileNotFoundError as e:
                print('\033[91m' + str(e) + '\033[0m')
                print("\033[93mgo may not be installed in runtime environment\n"
                      "try compiling manually: ($go build calculate.go reimann.go)\033[0m")
                exit(1)

    def __calculate(self):
        self.__checkCompile()
        calcProcess = run([f'{self.runcode}{self.executable}'],
                          input=f"{self.mean.get()} {self.stDev.get()} {self.x0.get()} {self.x1.get()}",
                          text=True,
                          capture_output=True)
        self.answer.set(calcProcess.stdout)
        if not self.answerOut:
            self.answerLabel.grid(column=0, row=6, columnspan=2)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("probability calculator")
    myapp = App(root)
