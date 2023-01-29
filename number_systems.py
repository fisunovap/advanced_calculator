import tkinter
from calculators import *
from base_calculator import Calculator

class NumberSystem(Calculator):
    def __init__(self):

        self.root = tkinter.Tk()
        self.root.title("СС")
        self.root.minsize(450, 100)
        self.root.resizable(width=False, height=False)
        super(NumberSystem, self).__init__(self.root)

        self.number_calc()

    def number_calc(self):
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

        frame = tkinter.Frame(self.root)
        frame.grid()

        a = tkinter.Entry(frame, width=20)
        a.grid(row=1, column=1, padx=(10, 0))
        a.bind("<FocusIn>", self.clear)
        tkinter.Label(frame, text="Число").grid(row=1, column=2)

        b = tkinter.Entry(frame, width=3)
        b.bind("<FocusIn>", self.clear)
        b.grid(row=1, column=3)
        tkinter.Label(frame, text="Исходная СС").grid(row=1, column=4)

        c = tkinter.Entry(frame, width=3)
        c.bind("<FocusIn>", self.clear)
        c.grid(row=1, column=5)
        tkinter.Label(frame, text="Конечная СС").grid(row=1, column=6)

        tkinter.Button(frame, text="Решить", command=handler).grid(row=1, column=7, padx=(10, 0))

        output = tkinter.Text(frame, bg="black", font="Arial 12", fg="white", width=50, height=10)
        output.grid(row=2, columnspan=8)

        self.root.mainloop()
