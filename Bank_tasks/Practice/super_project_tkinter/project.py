import tkinter as tk

import entrance
import general
import user_window
import supporting_function

class Main():
    def __init__(self):
        
        self.root = tk.Tk()
        supporting_function.create_files()
        general.MAIN_CLASS = self.root
        self.settings_window()
        self.loading_gif = tk.PhotoImage(file="gifs/load.gif")
        self.create_labels()
        self.update_gif(0)

        self.root.after(1000, self.end_loading)
        self.root.mainloop()

    def settings_window(self):
        self.root.title("Добро пожаловать")
        self.root.geometry(f"{general.SMALL_WIN_WIDTH}x{general.SMALL_WIN_HEIGHT}+{general.SMALL_WIN_POS_X}+{general.SMALL_WIN_POS_Y}")

        self.root.resizable(False, False)
        self.root["bg"] = general.BACKGROUND

    def create_labels(self):
        self.lbl_loading = tk.Label(self.root, image=self.loading_gif, bg=general.BACKGROUND)
        self.lbl_loading.place(relx=0.5, rely=0.5, anchor="center")

        lbl_hello = tk.Label(self.root, text="Добро пожаловать в приложение Заметки!", font=general.ACCENT_FONT, \
                             bg=general.BACKGROUND, fg = general.DARKBLUE)
        lbl_hello.place(rely=0.4, relx=0.06)

        lbl_tkinter = tk.Label(self.root, text="Built with Tkinter", font=general.SMALL_FONT, bg=general.BACKGROUND, fg = general.DARKBLUE)
        lbl_tkinter.place(rely=0.95, relx=0.45)

    def update_gif(self, frame):
        gif = tk.PhotoImage(file="gifs/load.gif", format=f"gif - {frame}")
        gif = gif.subsample(10,10)
        self.lbl_loading.config(image=gif)
        self.lbl_loading.image = gif 
        frame = (frame + 1) % 18
        self.root.after(100, self.update_gif, frame) 

    def end_loading(self):
        self.root.withdraw()
        if supporting_function.get_autorised():
            user_window.UserWindow()
        else:
            entrance.Entrance()


if __name__ == "__main__":
    main = Main()
    
 
