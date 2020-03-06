from tkinter import *
import copy

# Варіант 24 ∪ ∩ ¯

set_U = set(range(255))


def union_set(set1, set2):
    return set1.union(set2)


def difference_set(set1, set2):
    return set1.difference(set2)


def not_set(myset):
    return difference_set(set_U, myset)


def create_win(title):
    win = Tk()
    win.title(title)
    win.geometry("900x700")
    win.resizable(False, False)
    win.config(bg="#2B2B2B")
    return win


def second_window():
    res = "Preliminary result"
    step = ["B ∩ !C", set_ABC[1], not_set(set_ABC[2]), difference_set(set_ABC[1], not_set(set_ABC[2])),
            "!A ∩ C", not_set(set_ABC[0]), set_ABC[2], difference_set(not_set(set_ABC[0]), set_ABC[2]),
            "A ∩ B", set_ABC[0], set_ABC[2], difference_set(set_ABC[0], set_ABC[2]),
            "!A ∪ B", not_set(set_ABC[0]), set_ABC[1], union_set(not_set(set_ABC[0]), set_ABC[1])]

    step.extend([res + " ∪ !C", step[15], set_ABC[2], union_set(step[15], set_ABC[2])])
    step.extend([res + " ∪ (B ∩ !C)", step[19], step[3], union_set(step[19], step[3])])
    step.extend([res + "∪ (!A ∩ C)", step[23], step[7], union_set(step[23], step[7])])
    step.extend([res + "∪ (A ∩ B)", step[27], step[11], union_set(step[27], step[11])])
    step.extend(["Астанавітесь", "D", "D", step[-1]])

    Window23(set_ABC, "Second Window", step, "D = !A ∪ B ∪ !C ∪ (B ∩ !C) ∪ (!A ∩ C) ∪ (A ∩ B)")


def third_window():
    res = "Preliminary result"
    step = ["!A ∪ B", not_set(set_ABC[0]), set_ABC[1], union_set(not_set(set_ABC[0]), set_ABC[1])]
    step.extend([res + " ∪ !C", step[3], set_ABC[2], union_set(step[3], set_ABC[2])])
    step.extend(["Астанавітесь", "D", "D", step[-1]])

    Window23(set_ABC, "Third Window", step, "D = !A ∪ B ∪ !C")


def fourth_window():
    Window4(*set_ABC)


def fifth_window():
    Window5(*set_ABC)


class Window23:

    def __init__(self, set_ABC, title, step, text_D):
        self.title = title
        self.win = create_win(self.title)
        self.text_set = Text(self.win, width=110, height=30, font="Arial 9 bold")
        self.text_set.place(relx=0.5, rely=0.54, anchor=CENTER)
        self.step_res = step[-1]
        self.step_len = len(step)
        self.step = iter(step)
        self.recorded = False
        leb_set = Label(self.win, text="Множина A: {}\nМножина B: {}\nМножина C: {}".format(*set_ABC),
                        font="Arial 11 bold", justify=LEFT, bg="#3C3F41", fg="white", bd=10)

        label_example = Label(self.win, text=text_D, font="Arial 14 bold",
                              justify=LEFT, bg="#3C3F41", fg="white", bd=10)

        butt_next_step = Button(self.win, text="Наступний крок", command=lambda: next(self.next_step()))
        butt_write = Button(self.win, text="Записати у файл", command=self.write_to_file)

        leb_set.place(relx=0.5, rely=0.1, anchor=CENTER)
        label_example.place(relx=0.5, rely=0.2, anchor=CENTER)
        butt_next_step.place(relx=0.8, rely=0.9, anchor=CENTER)
        butt_write.place(relx=0.2, rely=0.9, anchor=CENTER)
        self.win.mainloop()

    def write_to_file(self):
        if not self.recorded:
            with open(self.title + ".txt", "w+") as f:
                f.write(str(self.step_res))
            ledel_write = Label(self.win, text="Записано", font="Arial 14 bold",
                                justify=LEFT, bg="#3C3F41", fg="green", bd=10)
            ledel_write.place(relx=0.5, rely=0.9, anchor=CENTER)
            self.recorded = True

    def next_step(self):
        for i in range(0, self.step_len, 4):
            self.text_set.delete(1.0, END)
            self.text_set.insert(1.0, 'Операція: {}\n\n Mножина 1: {}\n\n Множина 2: {}\n\n Результат : {}'.format(
                *(next(self.step) for j in range(4))))
            yield


class Window4:

    def in_file(self):
        with open("Fourth Window.txt", "w+") as f:
            f.write(str(self.Z))

    def __init__(self, A, B, *x):
        self.X = not_set(B)
        self.Y = not_set(A)
        self.Z = union_set(self.X, self.Y)
        self.win = create_win("Fourth Window")
        leb = Label(self.win, text="X = !B Y = !A Z = X ∪ Y",
                    font="Arial 11 bold", justify=LEFT, bg="#3C3F41", fg="white", bd=10)
        leb.place(relx=0.5, rely=0.1, anchor=CENTER)
        but = Button(self.win, text="Записати у файл", command=self.in_file)
        but.place(relx=0.5, rely=0.9, anchor=CENTER)
        text_set = Text(self.win, width=85, height=30, font="Arial 12 bold")
        text_set.insert(1.0, "X = {} \n\n Y = {} \n\n Z = {}".format(self.X, self.Y, self.Z))
        text_set.place(relx=0.5, rely=0.54, anchor=CENTER)
        self.win.mainloop()


def read_in(title):
    try:
        with open(title + ".txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Помилка читання"


class Window5:

    def __init__(self, A, B, *x):
        self.X = not_set(B)
        self.Y = not_set(A)
        self.win = create_win("Fifth Window")
        butt_read = Button(self.win, text="Почати зчитування", command=read)
        butt_read.place(relx=0.5, rely=0.05, anchor=CENTER)
        butt_union = Button(self.win, text="Знайти Z", command=self.pythonZ)
        butt_union.place(relx=0.5, rely=0.1, anchor=CENTER)
        leb = Label(self.win,
                    text="Не оптимізов.: {0}Оптимізований: {0}Множина Z: {0}Множина \n  X ∪ Y: ".format("\n" * 6),
                    font="Arial 13 bold", justify=LEFT, bg="#3C3F41", fg="white", bd=12)
        leb.place(relx=0.17, rely=0.43, anchor=CENTER)
        self.win.mainloop()

    def printSet(self):
        set_min_full_Z = iter(read_in("Second Window"), read_in("Third Window"), read_in("Fourth Window"))
        text = [Text(self.win, width=60, height=5, font="Arial 12 bold") for i in range(3)]
        tuple(map(lambda x: x.insert(1.0, next(set_min_full_Z)), text))
        tuple(map(lambda x, y: x.place(relx=0.65, rely=0.23 + y / 8, anchor=CENTER), text, range(len(text))))

    def pythonZ(self):
        text = Text(self.win, width=60, height=5, font="Arial 12 bold")
        text.insert(1.0, self.X.union(self.Y))
        text.place(relx=0.65, rely=0.63, anchor=CENTER)

    def tester(self):
        return Label(self.win, text="Не оптимізований = Оптимізований {0}\n Множина Z = Множина X ∪ Y {1} ".format(
            lambda x, y: x == y, ),
                     font="Arial 13 bold", justify=LEFT, bg="#3C3F41", fg="white", bd=12).place(relx=0.5, rely=0.8,
                                                                                                anchor=CENTER)


# ОБЕРЕЖНО

set_ABC = [{' 71', ' 194', ' 155', ' 158', ' 203', ' 88', ' 36', ' 29', '96'},
           {' 218', '161', ' 83', ' 228', ' 167', ' 145', ' 6', ' 79'},
           {' 247', ' 94', ' 14', ' 47', ' 208', ' 150', '170'}]

second_window()
third_window()
fourth_window()
fifth_window()
