from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
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



    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula += "^2"
        elif operation == "=":
            self.formula = str(eval(self.formula.replace("^2", "**2")))
        elif operation == "ax^2+bx+c":
            from math import sqrt
            def solver(a, b, c):
                """ Решает квадратное уравнение и возвращает результат в форматированной строке """
                D = b * b - 4 * a * c
                if D >= 0:
                    x1 = (-b + sqrt(D)) / (2 * a)
                    x2 = (-b - sqrt(D)) / (2 * a)
                    text = "Дискриминант = %s \nX1 = %s \nX2 = %s \n" % (D, x1, x2)
                else:
                    text = "Дискриминант = %s \nНет корней в поле действительных чисел" % D
                return text



            root = Tk()
            root.title("ax^2+bx+c")
            root.minsize(325, 230)
            root.resizable(width=False, height=False)

            frame = Frame(root)
            frame.grid()

            a = Entry(frame, width=3)
            a.grid(row=1, column=1, padx=(10, 0))
            a.bind("<FocusIn>", clear)
            a_lab = Label(frame, text="x^2+").grid(row=1, column=2)

            b = Entry(frame, width=3)
            b.bind("<FocusIn>", clear)
            b.grid(row=1, column=3)
            b_lab = Label(frame, text="x+").grid(row=1, column=4)

            c = Entry(frame, width=3)
            c.bind("<FocusIn>", clear)
            c.grid(row=1, column=5)
            c_lab = Label(frame, text="= 0").grid(row=1, column=6)

            but = Button(frame, text="Решить", command=handler).grid(row=1, column=7, padx=(10, 0))

            output = Text(frame, bg="black", font="Arial 12", fg="white", width=35, height=10)
            output.grid(row=2, columnspan=8)

            root.mainloop()

        elif operation == "ax^4+bx^2+c":
            from math import sqrt
            def solver(a, b, c):
                """ Решает квадратное уравнение и возвращает результат в форматированной строке """
                D = b * b - 4 * a * c
                if D >= 0:
                    x1 = (-b + sqrt(D)) / (2 * a)
                    if x1>=0:
                        x_1 = sqrt(x1)
                        x_2 = (0-sqrt(x1))
                    else:
                        x_1 = "sqrt(t1)<0"
                        x_2 = "sqrt(t1)<0"
                    x2 = (-b - sqrt(D)) / (2 * a)
                    if x2>=0:
                        x_3 = sqrt(x2)
                        x_4 = (0 - sqrt(x2))
                    else:
                        x_3 = "sqrt(t2)<0"
                        x_4 = "sqrt(t2)<0"
                    text = "Дискриминант = %s \nX1 = %s \nX2 = %s \nX3 = %s\nX4 = %s " % (D, x_1, x_2, x_3, x_4)
                else:
                    text = "Дискриминант = %s \nНет корней в поле действительных чисел" % D
                return text

            def inserter(value):
                """ Вставляет указанное значение в текстовый виджет """
                output.delete("0.0", "end")
                output.insert("0.0", value)

            def clear(event):
                """ Очищает форму ввода """
                caller = event.widget
                caller.delete("0", "end")

            def handler():
                """ Получает содержимое записей и передает результат в текст """
                try:
                    # проверка, что мы ввели правильные значения
                    a_val = float(a.get())
                    b_val = float(b.get())
                    c_val = float(c.get())
                    inserter(solver(a_val, b_val, c_val))
                except ValueError:
                    inserter("Убедитесь, что вы ввели 3 цифры")

            root = Tk()
            root.title("ax^4+bx^2+c")
            root.minsize(325, 230)
            root.resizable(width=False, height=False)

            frame = Frame(root)
            frame.grid()

            a = Entry(frame, width=3)
            a.grid(row=1, column=1, padx=(10, 0))
            a.bind("<FocusIn>", clear)
            a_lab = Label(frame, text="x^4+").grid(row=1, column=2)

            b = Entry(frame, width=3)
            b.bind("<FocusIn>", clear)
            b.grid(row=1, column=3)
            b_lab = Label(frame, text="x^2+").grid(row=1, column=4)

            c = Entry(frame, width=3)
            c.bind("<FocusIn>", clear)
            c.grid(row=1, column=5)
            c_lab = Label(frame, text="= 0").grid(row=1, column=6)

            but = Button(frame, text="Решить", command=handler).grid(row=1, column=7, padx=(10, 0))

            output = Text(frame, bg="black", font="Arial 12", fg="white", width=35, height=10)
            output.grid(row=2, columnspan=8)

            root.mainloop()
        elif operation == "СС":
            root = Tk()
            root.title('СС')

            buttons = (('2', '3', '5', '8', '10'),
                       ('12', '16', '20', '60'),
                       ('CC input', 'СС output'))

            activeStr = ''
            stack = []
            root.minsize(200, 120)
            root.resizable(width=False, height=False)


            button = Button(root, text='CE', command=lambda text='CE': click(text))
            button.grid(row=1, column=3, sticky="nsew")
            for row in range(4):
                for col in range(4):
                    button = Button(root, text=buttons[row][col],
                                    command=lambda row=row, col=col: click(buttons[row][col]))
                    button.grid(row=row + 2, column=col, sticky="nsew")

            root.mainloop()

        else:
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