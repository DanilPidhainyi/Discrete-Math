from tkinter import *
import random, NextWindow


def my_variant(G=93, N=20, M="ІВ"):
    if M == "ІО":
        N += 2
    return str((N + G % 60) % 30 + 1)


def my_write(v: list, s: list) -> object:
    """Функція для перезаписів у поля Entry"""
    for i in range(3):
        v[i].delete(0, END)
        v[i].insert(0, s[i])
    return v


class FistWindow:

    def do_nothing(self):
        file_win = Toplevel(self.root)
        button = Button(file_win, text="Do nothing button")
        button.pack()

    def __init__(self):
        self.len_ABC = [0, 0, 0]
        self.set_ABC = [set() for i in range(3)]
        self.root = Tk()
        self.root.title("Start Window")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        self.menubar = Menu(self.root)
        self.menubar.add_command(label=" Second win ", font="Arial 14", command=lambda: NextWindow.second_window(self.set_ABC, self.scanU()))
        self.menubar.add_command(label=" Third win ", font="Arial 14", command=lambda: NextWindow.third_window(self.set_ABC, self.scanU()))
        self.menubar.add_command(label=" Fourth win ", font="Arial 14", command=self.do_nothing)
        self.menubar.add_command(label=" Fifth win ", font="Arial 14", command=self.do_nothing)
        self.root.config(bg="#2B2B2B", menu=self.menubar)
        # про мене
        Label(self.root,
              text="Підгайний Данило Романович\nстудент групи ІВ-93\nномер у списку групи: 20\n" +
                   "варіант: " + my_variant(),
              font="Arial 14 bold", justify=LEFT, bg="#3C3F41", fg="white", bd=10).place(relx=0.5, rely=0.1,
                                                                                         anchor=CENTER)
        # Задавання потужності
        label_len_ABC = [Label(self.root, text="Потужність {}: ".format(i), font="Arial 10 bold", justify=LEFT, bg="#3C3F41",
                               fg="white") for i in ("A", "B", "C")]
        self.ent_len_ABC = [Entry(self.root, width=5, bd=3) for i in range(3)]

        # Задавання множини
        label_set_ABC = [Label(self.root, text="Множина {}: ".format(i), font="Arial 10 bold", justify=LEFT, bg="#3C3F41",
                               fg="white") for i in ("A", "B", "C")]
        self.ent_set_ABC = [Entry(self.root, width=30, bd=3) for i in range(3)]

        # Задавання універсальної множини
        label_set_U = Label(self.root, text="Універсальна множина : ", font="Arial 10 bold", justify=LEFT, bg="#3C3F41",
                            fg="white", bd=7).place(relx=0.47, rely=0.55, anchor=CENTER)
        self.ent_U = (Entry(self.root, width=10, bd=3), Entry(self.root, width=10, bd=3))

        # Кнопки задавання потужності
        Button(self.root, text="Випадкові значення", command=self.rand_len_set).place(relx=0.3, rely=0.25, anchor=CENTER)
        Button(self.root, text="Підтвердити", command=self.scan_len).place(relx=0.34, rely=0.45, anchor=CENTER)

        # Кнопки задавання множини
        Button(self.root, text="Випадкові значення", command=self.rand_set).place(relx=0.65, rely=0.25, anchor=CENTER)
        Button(self.root, text="Підтвердити", command=self.scan_set).place(relx=0.61, rely=0.45, anchor=CENTER)

        # Розміщеня множин
        for i in range(len(self.ent_len_ABC)):
            j = 0.3 + 0.05 * i
            self.ent_len_ABC[i].place(relx=0.4, rely=j, anchor=CENTER)
            label_len_ABC[i].place(relx=0.28, rely=j, anchor=CENTER)
            self.ent_set_ABC[i].place(relx=0.8, rely=j, anchor=CENTER)
            label_set_ABC[i].place(relx=0.6, rely=j, anchor=CENTER)

        # Scale
        self.sca1 = Scale(self.root, orient=HORIZONTAL, length=300, from_=0, to=255, tickinterval=25, resolution=1,
                          font="Arial 10 bold")
        self.sca2 = Scale(self.root, orient=HORIZONTAL, length=300, from_=0, to=255, tickinterval=25, resolution=1,
                          font="Arial 10 bold")
        self.sca1.place(relx=0.47, rely=0.62, anchor=CENTER)
        self.sca2.place(relx=0.47, rely=0.67, anchor=CENTER)
        self.root.mainloop()

    def scanU(self):
        return set(range(*map(lambda x: int(x.get()), (self.sca1, self.sca2))))

    def control_len(self, len_set, ent_len_ABC):
        my_write(ent_len_ABC, len_set)
        return ent_len_ABC

    def control_set(self, len_set):
        for i in range(3):
            while len(self.set_ABC[i]) < len_set[i]:
                self.set_ABC[i].add(random.randint(self.sca1.get(), self.sca2.get()))
            while len(self.set_ABC[i]) > len_set[i]:
                self.set_ABC[i].pop()
        my_write(self.ent_set_ABC, self.set_ABC)
        return self.set_ABC

    def scan_set(self):
        for i in range(3):
            a = set(self.ent_set_ABC[i].get().replace("{", "").replace("}", "").split(","))
            self.set_ABC[i] = a if a != {'set()'} and a != set('') and a != set() else ""
            self.len_ABC[i] = len(self.set_ABC[i])
        self.control_len(self.len_ABC, self.ent_len_ABC)
        return self.set_ABC

    def scan_len(self):
        self.len_ABC = list(map(lambda x: int(x.get()), self.ent_len_ABC))
        self.control_set(self.len_ABC)
        return self.len_ABC

    def rand_len_set(self):
        len_set = [random.randint(1, 10 if len(self.scanU()) >= 10 else len(self.scanU())) for i in range(3)]
        my_write(self.ent_len_ABC, len_set)
        self.control_set(len_set)
        return len_set

    def rand_set(self, len_set=None, boo=True):
        if len_set is None:
            len_set = self.rand_len_set()
        for i in range(len(self.ent_set_ABC)):
            self.set_ABC[i].clear()
            while len(self.set_ABC[i]) < len_set[i]:
                self.set_ABC[i].add(random.randint(self.sca1.get(), self.sca2.get()))
        my_write(self.ent_set_ABC, self.set_ABC)
        if boo:
            self.control_len(len_set, self.ent_len_ABC)
        pass


win = FistWindow()