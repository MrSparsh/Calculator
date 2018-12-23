from tkinter import *


class Calculator:

    def btn_pressed(self, text):
        self.entry_text.set(self.entry_text.get()+text)

    def equal_pressed(self):
        try:
            result = str(eval(self.entry_text.get()))
            self.entry_text.set(result)
        except Exception as e:
            self.entry_text.set("Error, Press Clear")

    def clear_pressed(self):
        self.entry_text.set("")

    def delete_pressed(self):
        self.entry_text.set(self.entry_text.get()[0:len(self.entry_text.get())-1])

    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x500')
        self.frame = Frame(self.root)
        Grid.rowconfigure(self.root, 0, weight=1)
        Grid.columnconfigure(self.root, 0, weight=1)
        self.frame.grid(row=0, column=0, sticky=N + S + E + W)
        self.root.title('Calculator')
        self.dict = {}
        self.entry_text = StringVar()
        self.arr = [
                ['CE', 'C', '(', ')'],
                ['1', '2', '3', '%'],
                ['4', '5', '6', '/'],
                ['7', '8', '9', '*'],
                ['0', '.', '+', '-'],
                ['=']
            ]
        self.max_column = 4
        print(len(self.arr))
        self.fill_widgets()

        for i in range(len(self.arr)+1):
            Grid.rowconfigure(self.frame, i, weight=1)

        for j in range(self.max_column):
            Grid.columnconfigure(self.frame, j, weight=1)

        self.root.mainloop()

    def add_entry(self, row, column, columnspan):
        entry = Entry(self.frame, relief=RIDGE, textvariable=self.entry_text, bd=30, font="Arial 18")
        entry.grid(row=row, column=column, sticky=N + S + E + W, columnspan=columnspan)

    def add_btn(self, text, row, column, columnspan):
        command= lambda: self.btn_pressed(text)
        if text == "=" :
            command= lambda: self.equal_pressed()
        elif text == "C":
            command= lambda: self.clear_pressed()
        elif text == "CE":
            command= lambda: self.delete_pressed()
        self.dict[text] = Button(self.frame, text=text, font="Arial 18", command=command)
        self.dict[text].grid(row=row, column=column, sticky=N + S + E + W, columnspan=columnspan)

    def fill_widgets(self):
        self.add_entry(row=0, column=0, columnspan=self.max_column)
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                columnspan=1
                if j == len(self.arr[i])-1:
                    columnspan = self.max_column - j
                self.add_btn(text=self.arr[i][j], row=i+1, column=j, columnspan=columnspan)


if __name__ == "__main__":
    Calculator()
