import tkinter as tk
import general
from tkinter import messagebox, simpledialog
import supporting_function
import entrance

import os

class UserWindow:
    def __init__(self):
        self.root = tk.Toplevel()
        self.settings_window()
        self.create_widgets()

        self.flag_eye = 1
        self.root.protocol("WM_DELETE_WINDOW", self.after_exit)

        self.notes = {}  
        self.notes_handler()  

    def settings_window(self):
        self.root.title("Заметки")
        self.root.geometry(f"{general.USER_WIN_WIDTH}x{general.USER_WIN_HEIGHT}+{general.USER_WIN_POS_X}+{general.USER_WIN_POS_Y}")
        self.root["bg"] = general.BACKGROUND
        self.root.attributes("-fullscreen", False)
        self.root.resizable(False, False)
    
    def create_widgets(self):
        self.menu = tk.Menu(self.root, tearoff=0)
        settings_menu = tk.Menu(self.menu, tearoff=0)
        settings_menu.add_command(label="Выход", command=self.exit_programm)
        settings_menu.add_command(label="Личный кабинет", command=self.user_lk)
        settings_menu.add_command(label="Сменить пароль", command=self.change_password)
        self.menu.add_cascade(label="Settings", menu=settings_menu)
        self.root.config(menu=self.menu)

        self.notes_frame = tk.Frame(self.root, bg=general.BACKGROUND)
        self.notes_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.canvas = tk.Canvas(self.notes_frame, bg=general.BACKGROUND, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.notes_frame, orient="vertical", command=self.canvas.yview)

        self.scrollable_frame = tk.Frame(self.canvas, bg=general.BACKGROUND)
        # self.scrollable_frame.pack(fill=tk.BOTH, expand=True) 
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.window_id = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.create_note_button = tk.Button(self.root, text="Создать заметку", command=self.create_note, bg="lightgray")
        self.create_note_button.pack(fill=tk.X, padx=10, pady=5)

    def notes_handler(self):
        path_to_dir = f"notes/{supporting_function.get_login()}"
        
        if not os.path.exists(path_to_dir) or not os.path.isdir(path_to_dir):
            os.makedirs(path_to_dir)  
        
        self.notes = {}
        for file in os.listdir(path_to_dir):
            file_path = path_to_dir + "/" +file
            if os.path.isfile(file_path):  
                with open(file_path, "r", encoding="utf-8") as f:
                    self.notes[file] = f.read()

        self.load_notes()  

    def load_notes(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for note_title in self.notes:
            note_button = tk.Button(
                self.scrollable_frame, text=note_title, bg=general.BACKGROUND,
                padx=10, pady=5, relief="solid", anchor="w", 
                command=lambda title=note_title: self.edit_note(title)
            )
            note_button.pack(fill=tk.X, padx=5, pady=2, expand=True)

        self.root.update_idletasks()
        self.canvas.itemconfig(self.window_id, width=self.canvas.winfo_width())
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def delete_note(self, title):
        path_to_dir = f"notes/{supporting_function.get_login()}"
        file_path = os.path.join(path_to_dir, title)

        confirm = messagebox.askyesno("Удаление заметки", f"Вы уверены, что хотите удалить заметку '{title}'?")
        
        if confirm:  
            if os.path.exists(file_path):
                os.remove(file_path)
                del self.notes[title]
                self.load_notes()
            else:
                messagebox.showerror("Ошибка", "Файл не найден!")
        self.edit_window.destroy()

    def edit_note(self, title):
        text = self.notes.get(title, "")

        self.edit_window = tk.Toplevel(self.root)
        self.edit_window.title(f"Редактирование '{title}'")
        self.edit_window.geometry("600x600")

        text_box = tk.Text(self.edit_window, wrap="word", width=80, height=30)
        text_box.insert("1.0", text)
        text_box.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        save_button = tk.Button(self.edit_window, text="Сохранить", command=lambda: self.save_note(title, text_box))
        save_button.pack(pady=5, side="right", padx = 10)

        save_button = tk.Button(self.edit_window, text="Удалить", command=lambda: self.delete_note(title))
        save_button.pack(pady=5, side="left", padx  = 10)

    def save_note(self, title, text_box):
        new_text = text_box.get("1.0", tk.END).strip()

        path_to_dir = f"notes/{supporting_function.get_login()}"
        file_path = os.path.join(path_to_dir, title)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_text)

        self.notes[title] = new_text  
        self.edit_window.destroy()
        self.load_notes()  

    def create_note(self):
        new_title = simpledialog.askstring("Создание заметки", "Введите название заметки:")
        if not new_title:
            return

        path_to_dir = f"notes/{supporting_function.get_login()}"
        file_path = os.path.join(path_to_dir, new_title)

        if os.path.exists(file_path):
            messagebox.showerror("Ошибка", "Заметка с таким названием уже существует!")
            return

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("")  

        self.notes[new_title] = ""  
        self.load_notes()  


    def user_lk(self):
        messagebox.showinfo("Личный кабинет", f"Вы авторизрованы как {supporting_function.get_login()}")

    def change_password(self):
        old_password = simpledialog.askstring("Смена пароля", "Введите старый пароль:")
        if not old_password:
            messagebox.showerror("Смена пароля", "Пароль не введен")
            return False
        
        if not supporting_function.try_entrance(supporting_function.get_login(), old_password):
            messagebox.showerror("Смена пароля", "Неверный пароль")
            return False

        new_password = simpledialog.askstring("Смена пароля", "Введите новый пароль:")

        if not new_password:
            messagebox.showerror("Смена пароля", "Пароль не введен")
            return False

        if not supporting_function.check_symbols(new_password):
            messagebox.showerror("Смена пароля", "Пароль не должен содержать символы ':{}'")
            return False

        if len(new_password) < 4:
            messagebox.showerror("Смена пароля", "Пароль должен содержать не менее 4 символов")
            return False
        
        supporting_function.change_password(supporting_function.get_login(), new_password)
        messagebox.showinfo("Смена пароля", "Пароль успешно изменен")

    def exit_programm(self):
        supporting_function.rewrite_config("False", supporting_function.get_login())
        self.root.destroy()
        entrance.Entrance()

    def after_exit(self):
        general.MAIN_CLASS.destroy()
