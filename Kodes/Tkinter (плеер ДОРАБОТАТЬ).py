# from tkinter import *
# from pygame import mixer
# from tkinter import filedialog
# 
# root = Tk()
# mixer.init()
# 
# master_frame = Frame(root)
# master_frame.pack()
# 
# root.mainloop()





# from tkinter import *
# from pygame import mixer
# from tkinter import filedialog
# 
# root = Tk()
# mixer.init()
# 
# master_frame = Frame(root)
# master_frame.pack()
# 
# info_frame = Frame(master_frame)
# info_frame.grid(row=0, column=0)
# 
# controls_frame = Frame(master_frame)
# controls_frame.grid(row=1, column=0)
# 
# file_frame = Frame(master_frame)
# file_frame.grid(row=0, column=5)
# 
# song_state = Label(info_frame, width=60, text="Остановлено", font="Arial 8 bold")
# song_state.grid(row=0, column=0)
# 
# song_box = Listbox(info_frame, width=60, selectbackground="blue")
# song_box.grid(row=1, column=0)
# 
# def prev_song():
#     pass
# def next_song():
#     pass
# def play():
#     pass
# def pause():
#     pass
# def stop():
#     pass
# def openfile():
#     pass
# def openfolder():
#     pass
# 
# back_button = Button(controls_frame, text="<-", width=10)
# back_button.grid(row=0, column=0)
# forward_button = Button(controls_frame, text='->', width=10)
# forward_button.grid(row=0, column=1)
# play_button = Button(controls_frame, text='|>', width=10)
# play_button.grid(row=0, column=2)
# pause_button = Button(controls_frame, text='||', width=10)
# pause_button.grid(row=0, column=3)
# stop_button = Button(controls_frame, text='[]', width=10)
# stop_button.grid(row=0, column=4)
# 
# openfile_button = Button(file_frame, text='Открыть файл')
# openfile_button.grid(row=0, column=0)
# openfolder_button = Button(file_frame, text='Открыть папку')
# openfolder_button.grid(row=1, column=0)
# 
# 
# root.mainloop()










# from tkinter import *
# from pygame import mixer
# from tkinter import filedialog
# 
# root = Tk()
# mixer.init()
# 
# master_frame = Frame(root)
# master_frame.pack()
# 
# info_frame = Frame(master_frame)
# info_frame.grid(row=0, column=0)
# 
# controls_frame = Frame(master_frame)
# controls_frame.grid(row=1, column=0)
# 
# file_frame = Frame(master_frame)
# file_frame.grid(row=0, column=5)
# 
# song_state = Label(info_frame, width=60, text="Остановлено", font="Arial 8 bold")
# song_state.grid(row=0, column=0)
# 
# song_box = Listbox(info_frame, width=60, selectbackground="blue")
# song_box.grid(row=1, column=0)
# 
# def prev_song():
#     passurselection
# 
# def next_song():
#     pass
# 
# def play():
#     song = song_box.get(ACTIVE)
#     mixer.music.load(song)
#     mixer.music.play()
#     song_state['text'] = "Воспроизведение"
#     
# def pause():
#     pass
#         
# 
# def stop():
#     mixer.music.stop()
#     song_box.selection_clear(ACTIVE)
#     song_state['text'] = "Остановлено"
# 
# def openfile():
#     song = filedialog.askopenfilename(initialdir='tracks/', title="Выберите песню!", filetypes=(("mp3 Files", "*.mp3"),))
#     song_box.insert(END, song)
#     
# def openfolder():
#     songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
#     for song in songs:
#         song_box.insert(END, song)
# 
# back_button = Button(controls_frame, text="<-", width=10, command=prev_song)
# back_button.grid(row=0, column=0)
# 
# forward_button = Button(controls_frame, text='->', width=10, command=next_song)
# forward_button.grid(row=0, column=1)
# 
# play_button = Button(controls_frame, text='|>', width=10, command=play)
# play_button.grid(row=0, column=2)
# 
# pause_button = Button(controls_frame, text='||', width=10, command=pause)
# pause_button.grid(row=0, column=3)
# 
# stop_button = Button(controls_frame, text='[]', width=10, command=stop)
# stop_button.grid(row=0, column=4)
# 
# 
# openfile_button = Button(file_frame, text='Открыть файл', command=openfile)
# openfile_button.grid(row=0, column=0)
# 
# openfolder_button = Button(file_frame, text='Открыть папку', command=openfolder)
# openfolder_button.grid(row=1, column=0)
# 
# 
# root.mainloop()



# from tkinter import *
# from pygame import mixer
# from tkinter import filedialog
# 
# root = Tk()
# mixer.init()
# 
# master_frame = Frame(root)
# master_frame.pack()
# 
# info_frame = Frame(master_frame)
# info_frame.grid(row=0, column=0)
# 
# controls_frame = Frame(master_frame)
# controls_frame.grid(row=1, column=0)
# 
# file_frame = Frame(master_frame)
# file_frame.grid(row=0, column=5)
# 
# song_state = Label(info_frame, width=60, text="Остановлено", font="Arial 8 bold")
# song_state.grid(row=0, column=0)
# 
# song_box = Listbox(info_frame, width=60, selectbackground="blue")
# song_box.grid(row=1, column=0)
# 
# def prev_song():
#     pass
# 
# def next_song():
#     next_s = song_box.courselection()
#     ext_s = next_s[0] + 1
#     song = song_box.get(next_s)
#     mixer.music.load(song)
#     mixer.music.play()
#     song_box.selection_clear(0, END)
#     song_box.activate(next_s)
#     song_box.selection_set(next_s, last=None)
# 
# def play():
#     song = song_box.get(ACTIVE)
#     mixer.music.load(song)
#     mixer.music.play()
#     song_state['text'] = "Воспроизведение"
#     
# def pause():
#     if song_state['text'] == "Пауза":
#         mixer.music.unpause()
#         song_state['text'] = "Воспроизведение"
#     else:
#         mixer.music.pause()
#         song_state['text'] = "Пауза"
#         
# 
# def stop():
#     mixer.music.stop()
#     song_box.selection_clear(ACTIVE)
#     song_state['text'] = "Остановлено"
# 
# def openfile():
#     song = filedialog.askopenfilename(initialdir='tracks/', title="Выберите песню!", filetypes=(("mp3 Files", "*.mp3"),))
#     song_box.insert(END, song)
#     
# def openfolder():
#     songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
#     for song in songs:
#         song_box.insert(END, song)
# 
# back_button = Button(controls_frame, text="<-", width=10, command=prev_song)
# back_button.grid(row=0, column=0)
# 
# forward_button = Button(controls_frame, text='->', width=10, command=next_song)
# forward_button.grid(row=0, column=1)
# 
# play_button = Button(controls_frame, text='|>', width=10, command=play)
# play_button.grid(row=0, column=2)
# 
# pause_button = Button(controls_frame, text='||', width=10, command=pause)
# pause_button.grid(row=0, column=3)
# 
# stop_button = Button(controls_frame, text='[]', width=10, command=stop)
# stop_button.grid(row=0, column=4)
# 
# 
# openfile_button = Button(file_frame, text='Открыть файл', command=openfile)
# openfile_button.grid(row=0, column=0)
# 
# openfolder_button = Button(file_frame, text='Открыть папку', command=openfolder)
# openfolder_button.grid(row=1, column=0)
# 
# 
# root.mainloop()





from tkinter import *
from pygame import mixer
from tkinter import filedialog

root = Tk()
mixer.init()

master_frame = Frame(root)
master_frame.pack()

info_frame = Frame(master_frame)
info_frame.grid(row=0, column=0)

controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0)

file_frame = Frame(master_frame)
file_frame.grid(row=0, column=5)

song_state = Label(info_frame, width=60, text="Остановлено", font="Arial 8 bold")
song_state.grid(row=0, column=0)

song_box = Listbox(info_frame, width=60, selectbackground="blue")
song_box.grid(row=1, column=0)

def prev_song():
    pass

def next_song():
    next_s = song_box.courselection()
    ext_s = next_s[0] + 1
    song = song_box.get(next_s)
    mixer.music.load(song)
    mixer.music.play()
    song_box.selection_clear(0, END)
    song_box.activate(next_s)
    song_box.selection_set(next_s, last=None)

def play():
    song = song_box.get(ACTIVE)
    mixer.music.load(song)
    mixer.music.play()
    song_state['text'] = "Воспроизведение"
    
def pause():
    if song_state['text'] == "Пауза":
        mixer.music.unpause()
        song_state['text'] = "Воспроизведение"
    else:
        mixer.music.pause()
        song_state['text'] = "Пауза"
        

def stop():
    mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    song_state['text'] = "Остановлено"

def openfile():
    song = filedialog.askopenfilename(initialdir='tracks/', title="Выберите песню!", filetypes=(("mp3 Files", "*.mp3"),))
    song_box.insert(END, song)
    
def openfolder():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    for song in songs:
        song_box.insert(END, song)

back_button = Button(controls_frame, text="<-", width=10, command=prev_song)
back_button.grid(row=0, column=0)

forward_button = Button(controls_frame, text='->', width=10, command=next_song)
forward_button.grid(row=0, column=1)

play_button = Button(controls_frame, text='|>', width=10, command=play)
play_button.grid(row=0, column=2)

pause_button = Button(controls_frame, text='||', width=10, command=pause)
pause_button.grid(row=0, column=3)

stop_button = Button(controls_frame, text='[]', width=10, command=stop)
stop_button.grid(row=0, column=4)


openfile_button = Button(file_frame, text='Открыть файл', command=openfile)
openfile_button.grid(row=0, column=0)

openfolder_button = Button(file_frame, text='Открыть папку', command=openfolder)
openfolder_button.grid(row=1, column=0)


root.mainloop()
