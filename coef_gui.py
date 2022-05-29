import tkinter as tk
from coefficients import Coefficients,function_inputs,desired_output


class CoefGUI:
    def __init__(self):
        self.coef = Coefficients()
        self.picture_size = 420
        self.root = tk.Tk()
        self.root.geometry('1280x500')
        self.root.title('Equation')


        self.coefficients_text = tk.Text(self.root, height=2, width=20)
        self.coefficients_label = tk.Label(self.root, text="Write all coefficients")
        self.coefficients_label.config(font=("Courier", 14))
        self.coefficients_label.pack()
        self.coefficients_text.pack()

        self.ex_res_text = tk.Text(self.root, height=2, width=10)
        self.ex_res_label = tk.Label(self.root, text="Write expected result")
        self.ex_res_label.config(font=("Courier", 14))
        self.ex_res_label.pack()
        self.ex_res_text.pack()

        self.calc_button = tk.Button(self.root, text="Calculate result", command=self.calc_result)
        self.calc_button.pack()

        self.info_label = tk.Label(self.root, text="Result will be shown here:")
        self.info_label.config(font=("Courier", 14))
        self.info_label.pack()
        self.res_label = tk.Label(self.root, text=" ")
        self.res_label.config(font=("Courier", 14))
        self.res_label.pack()
        self.res2_label = tk.Label(self.root, text=" ")
        self.res2_label.config(font=("Courier", 14))
        self.res2_label.pack()

        self.root.mainloop()


    def calc_result(self):
        genes = list(map(int, self.coefficients_text.get("1.0","end").split()))
        self.coef.num_genes = len(genes)
        self.coef.function_inputs = genes
        self.coef.desired_output = int(self.ex_res_text.get("1.0","end"))

        solution = self.coef.result_clicked()
        self.res_label.config(text = solution)
        self.info_label.config(text="")

        res = 0
        for i in range(len(genes)):
            res += genes[i]*solution[i]
        self.res2_label.config(text= res)



#gui = CoefGUI()