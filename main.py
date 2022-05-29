import tkinter as tk

from coef_gui import CoefGUI
from max_gui import MaxGUI

class MainGUI:
    def __init__(self):
        self.coef_gui = CoefGUI()
        self.max_gui = MaxGUI()

        self.root = tk.Tk()
        self.root.geometry('1280x500')
        self.root.title('Find maximum')

        self.coef_button = tk.Button(self.root, text="Calculate coefficients", command=self.calc_coef)
        self.coef_button.pack()

        self.max_button = tk.Button(self.root, text="Calculate maximum of the function", command=self.calc_max)
        self.max_button.pack()

        self.root.mainloop()


    def calc_coef(self):
        gui = CoefGUI()


    def calc_max(self):
        gui = MaxGUI()




gui = MainGUI()