import tkinter as tk
import general
import registration
from tkinter import messagebox
import supporting_function
import user_window

class Entrance:
    def __init__(self):
        self.root = tk.Toplevel()
        self.settings_window()
        self.create_widgets()

        self.flag_eye = 1
        self.root.protocol("WM_DELETE_WINDOW", self.after_exit)

    def settings_window(self):
        self.root.title("Вход")
        self.root.geometry(f"{general.SMALL_WIN_WIDTH}x{general.SMALL_WIN_HEIGHT}+{general.SMALL_WIN_POS_X}+{general.SMALL_WIN_POS_Y}")

        self.root.resizable(False, False)
        self.root["bg"] = general.BACKGROUND

    def create_widgets(self):

        self.entry_login = tk.Entry(self.root, font=general.NORMAL_FONT)
        self.entry_login.place(relx=0.52, rely=0.39, anchor="center")

        self.entry_password = tk.Entry(self.root, font=general.NORMAL_FONT, show="*")
        self.entry_password.place(relx=0.52, rely=0.45, anchor="center")

        self.btn_entrance = tk.Button(self.root, text="Войти", command = self.validate, font=general.NORMAL_FONT,\
                                       highlightbackground=general.LIGHTBLUE, fg=general.DARKBLUE, width=10, anchor="center")
        self.btn_entrance.place(relx = 0.28, rely=0.5)

        self.btn_registration = tk.Button(self.root, text="Зарегистрироваться", command = self.registration, font=general.NORMAL_FONT,\
                                       highlightbackground=general.LIGHTBLUE, fg=general.DARKBLUE, width=15, anchor="center")
        self.btn_registration.place(relx = 0.48, rely=0.5)

        eye = tk.PhotoImage(file="images/open_eye.png")
        eye = eye.subsample(5, 5)
        self.btn_eye = tk.Button(self.root,image = eye, width = 22, height= 22, compound="top", borderwidth=0, command = self.change_eye)
        self.btn_eye.image = eye
        self.btn_eye.place(relx=0.637, rely=0.428)

    
    def change_eye(self):
        self.flag_eye *= -1
        if self.flag_eye == -1:
            eye = tk.PhotoImage(file="images/close_eye.png")
            eye = eye.subsample(5, 5)
            self.entry_password.config(show="")
            self.btn_eye.config(image=eye)
        else:
            eye = tk.PhotoImage(file="images/open_eye.png")
            eye = eye.subsample(5, 5)
            self.entry_password.config(show="*")
            self.btn_eye.config(image=eye)
        self.btn_eye.image = eye

    def validate(self):
        if self.entry_login.get() == "":
            self.entry_login.config(highlightbackground="red")
            messagebox.showwarning("Ошибка", "Заполните поле логина!")
            return False
        else:
            self.entry_login.config(highlightbackground=general.LIGHTBLUE)
        
        if self.entry_password.get() == "":
            self.entry_password.config(highlightbackground="red")
            messagebox.showwarning("Ошибка", "Заполните поле пароля!")
            return False
        else:
            self.entry_password.config(highlightbackground=general.LIGHTBLUE)

        if supporting_function.try_entrance(self.entry_login.get(), self.entry_password.get()):
            supporting_function.change_autorised(True)
            supporting_function.change_login_conf(self.entry_login.get())
            messagebox.showwarning("Успешно", "Вы успешно авторизированы!")
        else:
            messagebox.showwarning("Ошибка", "Неверный логин или пароль!")
            return False
        supporting_function.rewrite_config("True", self.entry_login.get())
        self.root.destroy()
        user_window.UserWindow()
        
        return True
    
    def registration(self):
        self.root.destroy()
        registration.Registartion()

    def after_exit(self):
        general.MAIN_CLASS.destroy()