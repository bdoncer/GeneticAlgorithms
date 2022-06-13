import tkinter as tk
from maxim import MaxCtr


class MaxGUI:
    def __init__(self):
        self.max_ctr = MaxCtr()
        self.picture_size = 420
        self.root = tk.Tk()
        self.root.geometry('1280x500')
        self.root.title('Find maximum')


        self.left_b_text = tk.Text(self.root, height=2, width=10)
        self.left_b_label = tk.Label(self.root, text="Write left boundary")
        self.left_b_label.config(font=("Courier", 14))
        self.left_b_label.pack()
        self.left_b_text.pack()

        self.right_b_text = tk.Text(self.root, height=2, width=10)
        self.right_b_label = tk.Label(self.root, text="Write right boundary")
        self.right_b_label.config(font=("Courier", 14))
        self.right_b_label.pack()
        self.right_b_text.pack()

        self.calc_button = tk.Button(self.root, text="Calculate result", command=self.calc_result)
        self.calc_button.pack()


        self.res_label = tk.Label(self.root, text="x = ")
        self.res_label.config(font=("Courier", 14))
        self.res_label.pack()
        self.res2_label = tk.Label(self.root, text="y = ")
        self.res2_label.config(font=("Courier", 14))
        self.res2_label.pack()

        self.show_plot_button = tk.Button(self.root, text="Show plot", command=self.show_plot)
        self.show_plot_button.pack()



        self.root.mainloop()


    def calc_result(self):

        self.max_ctr.left_boundary.append(int(self.left_b_text.get("1.0","end")))
        self.max_ctr.right_boundary.append(int(self.right_b_text.get("1.0", "end")))
        #self.max_ctr.function = self.left_b_text.get("1.0","end"))

        x,y = self.max_ctr.result_clicked()
        self.res_label.config(text = "x = "+ str(x[0]))
        self.res2_label.config(text= "y = "+ str(y[0]))


    def show_plot(self):
        self.max_ctr.plot_function()



#gui = MaxGUI()