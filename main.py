from tkinter import *
from calculators import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
        self.build()

    def build(self):
        self.lbl.place(x=11, y=50)

        btns = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "X^2", "ax^2+bx+c", "ax^4+bx^2+c", "СС", "."
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def inserter(self, value, output):
        """ Вставляет указанное значение в текстовый виджет """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def clear(self, event):
        """ Очищает форму ввода """
        caller = event.widget
        caller.delete("0", "end")

    def logicalc(self, operation):
        match operation:
            case "C":
                self.formula = ""
            case "DEL":
                self.formula = self.formula[0:-1]
            case "X^2":
                self.formula += "^2"
            case "=":
                self.formula = str(eval(self.formula.replace("^2", "**2")))
            case "ax^2+bx+c":
                def handler():
                    """ Получает содержимое записей и передает результат в текст """
                    try:
                        # проверка, что мы ввели правильные значения
                        a_val = float(a.get())
                        b_val = float(b.get())
                        c_val = float(c.get())
                        self.inserter(solver_x2(a_val, b_val, c_val), output)
                    except ValueError:
                        self.inserter("Убедитесь, что вы ввели 3 цифры", output)

                root = Tk()
                root.title("ax^2+bx+c")
                root.minsize(325, 230)
                root.resizable(width=False, height=False)

                frame = Frame(root)
                frame.grid()

                a = Entry(frame, width=3)
                a.grid(row=1, column=1, padx=(10, 0))
                a.bind("<FocusIn>", self.clear)
                Label(frame, text="x^2+").grid(row=1, column=2)

                b = Entry(frame, width=3)
                b.bind("<FocusIn>", self.clear)
                b.grid(row=1, column=3)
                Label(frame, text="x+").grid(row=1, column=4)

                c = Entry(frame, width=3)
                c.bind("<FocusIn>", self.clear)
                c.grid(row=1, column=5)
                Label(frame, text="= 0").grid(row=1, column=6)

                Button(frame, text="Решить", command=handler).grid(row=1, column=7, padx=(10, 0))

                output = Text(frame, bg="black", font="Arial 12", fg="white", width=35, height=10)
                output.grid(row=2, columnspan=8)

                root.mainloop()

            case "ax^4+bx^2+c":
                def handler():
                    """ Получает содержимое записей и передает результат в текст """
                    try:
                        # проверка, что мы ввели правильные значения
                        a_val = float(a.get())
                        b_val = float(b.get())
                        c_val = float(c.get())
                        self.inserter(solver_x4(a_val, b_val, c_val), output)
                    except ValueError:
                        self.inserter("Убедитесь, что вы ввели 3 цифры", output)

                root = Tk()
                root.title("ax^4+bx^2+c")
                root.minsize(325, 230)
                root.resizable(width=False, height=False)

                frame = Frame(root)
                frame.grid()

                a = Entry(frame, width=3)
                a.grid(row=1, column=1, padx=(10, 0))
                a.bind("<FocusIn>", self.clear)
                Label(frame, text="x^4+").grid(row=1, column=2)

                b = Entry(frame, width=3)
                b.bind("<FocusIn>", self.clear)
                b.grid(row=1, column=3)
                Label(frame, text="x^2+").grid(row=1, column=4)

                c = Entry(frame, width=3)
                c.bind("<FocusIn>", self.clear)
                c.grid(row=1, column=5)
                Label(frame, text="= 0").grid(row=1, column=6)

                Button(frame, text="Решить", command=handler).grid(row=1, column=7, padx=(10, 0))

                output = Text(frame, bg="black", font="Arial 12", fg="white", width=35, height=10)
                output.grid(row=2, columnspan=8)

                root.mainloop()
            case "СС":
                def handler():
                    """ Получает содержимое записей и передает результат в текст """
                    try:
                        # проверка, что мы ввели правильные значения
                        a_val = str(a.get())
                        s_val = int(b.get())
                        f_val = int(c.get())
                        result = to_new_system(a_val, s_val, f_val)
                        self.inserter(result, output)
                    except ValueError:
                        self.inserter("Убедитесь, что введены верные значения", output)


                root = Tk()
                root.title("СС")
                root.minsize(450, 100)
                root.resizable(width=False, height=False)

                frame = Frame(root)
                frame.grid()

                a = Entry(frame, width=20)
                a.grid(row=1, column=1, padx=(10, 0))
                a.bind("<FocusIn>", self.clear)
                Label(frame, text="Число").grid(row=1, column=2)

                b = Entry(frame, width=3)
                b.bind("<FocusIn>", self.clear)
                b.grid(row=1, column=3)
                Label(frame, text="Исходная СС").grid(row=1, column=4)

                c = Entry(frame, width=3)
                c.bind("<FocusIn>", self.clear)
                c.grid(row=1, column=5)
                Label(frame, text="Конечная СС").grid(row=1, column=6)

                Button(frame, text="Решить", command=handler).grid(row=1, column=7, padx=(10, 0))

                output = Text(frame, bg="black", font="Arial 12", fg="white", width=50, height=10)
                output.grid(row=2, columnspan=8)

                root.mainloop()

            case _:
                if self.formula == "0":
                    self.formula = ""
                self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x650+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
