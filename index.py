from tkinter import *
from tkinter import filedialog
from moviepy.editor import *
import uuid


def on_button():
    Open_file(entry_file_on)

def in_button():
    Open_file(entry_file_in)


def Open_file(name):
    if name == entry_file_on:
        file = filedialog.askopenfilename(initialdir='C:/', filetypes=(("mp4 Files", "*.mp4"),))
    else:
        file = filedialog.askdirectory(initialdir='C:/')

    if not file == '':
        name.delete(0, END)
        name.insert(0, file)

def random_name():
    entry_name_file.delete(0, END)
    entry_name_file.insert(0, str(uuid.uuid4()))


def result():
    print(f'{str(entry_file_in.get())}/{str(entry_name_file.get())}')
    audio = AudioFileClip(entry_file_on.get())
    audio.write_audiofile(f'{str(entry_file_in.get())}/{entry_name_file.get()}.mp3')



root = Tk()
root.title("Конвектор")
root.geometry("900x600")

glob = Label(text="Конвертирование из mp4 в mp3", font=("Arial", 14))
glob.pack()


txt_file_on = Label(text="Конвертируемый файл", font=("Arial", 14))
txt_file_on.place(x=50, y=100)

entry_file_on = Entry(font="Times 16")
entry_file_on.place(x=50, y=130, width=500, height=30)

btn_on = Button(text="Поиск", command=on_button, font="Times 12")
btn_on.place(x=560, y=130, width=70, height=30)




txt_file_in = Label(text="Путь сохранения готового файла", font=("Arial", 14))
txt_file_in.place(x=50, y=200)

entry_file_in = Entry(font="Times 16")
entry_file_in.place(x=50, y=230, width=500, height=30)

btn_in = Button(text="Поиск", command=in_button, font="Times 12")
btn_in.place(x=560, y=230, width=70, height=30)



name_file = Label(text="Имя нового файла", font=("Arial", 14))
name_file.place(x=50, y=300)

entry_name_file = Entry(font="Times 16")
entry_name_file.place(x=50, y=330, width=500, height=30)
entry_name_file.insert(0, str(uuid.uuid4()))

random_gen = Button(text="Случайно", command=random_name, font="Times 14")
random_gen.place(x=560, y=330, width=90, height=30)




start = Button(text="Конвертировать", command=result, font="Times 14")
start.place(x=50, y=400, width=300, height=50)



root.mainloop()