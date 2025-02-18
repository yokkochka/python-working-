import tkinter as tk
import general
import entrance
from tkinter import messagebox
import supporting_function
import user_window

class Registartion:
    def __init__(self):
        self.root = tk.Toplevel()
        self.flag_eye_password = 1
        self.flag_eye_confirm = 1
        self.settings_window()
        self.root.protocol("WN_DELETE_WINDOW", self.after_exit)
        self.create_widgets()

    def settings_window(self):
        self.root.title("Регистрация")
        self.root.geometry(f"{general.SMALL_WIN_WIDTH}x{general.SMALL_WIN_HEIGHT}+{general.SMALL_WIN_POS_X}+{general.SMALL_WIN_POS_Y}")

        self.root.resizable(False, False)
        self.root["bg"] = general.BACKGROUND

    def create_widgets(self):
        self.entry_login = tk.Entry(self.root, font=general.NORMAL_FONT)
        self.entry_login.place(relx=0.52, rely=0.39, anchor="center")

        self.entry_password = tk.Entry(self.root, font=general.NORMAL_FONT, show="*")
        self.entry_password.place(relx=0.52, rely=0.45, anchor="center")

        eye = tk.PhotoImage(file="images/open_eye.png")
        eye = eye.subsample(5, 5)
        self.btn_eye_password = tk.Button(self.root,image = eye, width = 22, height= 22, compound="top", borderwidth=0, command = self.change_eye_password)
        self.btn_eye_password.image = eye
        self.btn_eye_password.place(relx=0.637, rely=0.428)

        self.entry_password_confirm = tk.Entry(self.root, font=general.NORMAL_FONT, show="*")
        self.entry_password_confirm.place(relx=0.52, rely=0.51, anchor="center")

        self.btn_eye_confirm = tk.Button(self.root,image = eye, width = 22, height= 22, compound="top", borderwidth=0, command = self.change_eye_confirm)
        self.btn_eye_confirm.image = eye
        self.btn_eye_confirm.place(relx=0.637, rely=0.49)

        self.btn_back = tk.Button(self.root, text="Назад", command = self.back, font=general.NORMAL_FONT,\
                                       highlightbackground=general.LIGHTBLUE, fg=general.DARKBLUE, width=5, anchor="center")
        self.btn_back.place(relx = 0.315, rely=0.63)

        self.btn_registration = tk.Button(self.root, text="Зарегистрироваться", command = self.validate, font=general.NORMAL_FONT,\
                                       highlightbackground=general.LIGHTBLUE, fg=general.DARKBLUE, width=15, anchor="center")
        self.btn_registration.place(relx = 0.435, rely=0.63)

    def change_eye_password(self):
        self.flag_eye_password *= -1
        if self.flag_eye_password == -1:
            eye = tk.PhotoImage(file="images/close_eye.png")
            eye = eye.subsample(5, 5)
            self.entry_password.config(show="")
            self.btn_eye_password.config(image=eye)
        else:
            eye = tk.PhotoImage(file="images/open_eye.png")
            eye = eye.subsample(5, 5)
            self.entry_password.config(show="*")
            self.btn_eye_password.config(image=eye)
        self.btn_eye_password.image = eye

    def change_eye_confirm(self):
        self.flag_eye_confirm *= -1
        if self.flag_eye_confirm == -1:
            eye = tk.PhotoImage(file="images/close_eye.png")
            eye = eye.subsample(5, 5)
            self.entry_password_confirm.config(show="")
            self.btn_eye_confirm.config(image=eye)
        else:
            eye = tk.PhotoImage(file="images/open_eye.png")
            eye = eye.subsample(5, 5)
            self.entry_password_confirm.config(show="*")
            self.btn_eye_confirm.config(image=eye)
        self.btn_eye_confirm.image = eye

    def validate(self):

        if not self.check_empty():
            return False
        
        if not self.check_all_symbols():
            return False
        
        if not self.check_lenght():
            return False
        
        if self.entry_password.get() != self.entry_password_confirm.get():
            self.entry_password.config(highlightbackground="red")
            self.entry_password_confirm.config(highlightbackground="red")
            messagebox.showwarning("Ошибка", "Пароли не совпадают!")
            return False
        else:
            self.entry_password.config(highlightbackground=general.LIGHTBLUE)
            self.entry_password_confirm.config(highlightbackground=general.LIGHTBLUE)

        if not supporting_function.check_login(self.entry_login.get()):
            self.entry_login.config(highlightbackground="red")
            messagebox.showwarning("Ошибка", "Логин уже занят!")
            return False
        else:
            self.entry_login.config(highlightbackground=general.LIGHTBLUE)

        supporting_function.write_new_user(self.entry_login.get(), supporting_function.hash_string(self.entry_password.get()))
        supporting_function.rewrite_config(True, self.entry_login.get())
        messagebox.showinfo("Успешно", "Вы успешно зарегистрированы!")
        self.root.destroy()
        user_window.UserWindow()

        return True
        
    def check_empty(self):
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
        
        if self.entry_password_confirm.get() == "":
            self.entry_password_confirm.config(highlightbackground="red")
            messagebox.showwarning("Ошибка", "Заполните поле подтверждения пароля!")
            return False
        else:
            self.entry_password_confirm.config(highlightbackground=general.LIGHTBLUE)

        return True

    def check_all_symbols(self):
        if not supporting_function.check_symbols(self.entry_login.get()):
            self.entry_login.config(highlightbackground="red")
            messagebox.showwarning("Ошибка", "Логин не должен содержать символы ':{}'")
            return False
        else:
            self.entry_login.config(highlightbackground=general.LIGHTBLUE)

        if not supporting_function.check_symbols(self.entry_password.get()):
            self.entry_password.config(highlightbackground="red")
            messagebox.showwarning("Ошибка", "Пароль не должен содержать символы ':{}'")
            return False
        else:
            self.entry_password.config(highlightbackground=general.LIGHTBLUE)
        
        if not supporting_function.check_symbols(self.entry_password_confirm.get()):
            self.entry_password_confirm.config(highlightbackground="red")
            messagebox.showwarning("Ошибка", "Подтверждение пароля не должно содержать символы ':{}'")
            return False
        else:
            self.entry_password_confirm.config(highlightbackground=general.LIGHTBLUE)
        
        return True

    def check_lenght(self):
        if len(self.entry_login.get()) < 4:
            self.entry_login.config(highlightbackground="red")
            messagebox.showwarning("Ошибка", "Логин должен содержать не менее 4 символов!")
            return False
        else:
            self.entry_login.config(highlightbackground=general.LIGHTBLUE)

        if len(self.entry_password.get()) < 4:
            self.entry_password.config(highlightbackground="red")
            messagebox.showwarning("Ошибка", "Пароль должен содержать не менее 4 символов!")
            return False
        else:
            self.entry_password.config(highlightbackground=general.LIGHTBLUE)

        if len(self.entry_password_confirm.get()) < 4:
            self.entry_password_confirm.config(highlightbackground="red")
            messagebox.showwarning("Ошибка", "Подтверждение пароля должен содержать не менее 4 символов!")
            return False
        else:
            self.entry_password_confirm.config(highlightbackground=general.LIGHTBLUE)

        return True

    def back(self):
        entrance.Entrance()
        self.root.destroy()

    def after_exit(self):
        general.MAIN_CLASS.destroy()


