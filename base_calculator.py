from tkinter import *

class Calculator(Frame):

    def inserter(self, value, output):
        """ Вставляет указанное значение в текстовый виджет """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def clear(self, event):
        """ Очищает форму ввода """
        caller = event.widget
        caller.delete("0", "end")