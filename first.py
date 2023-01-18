from pythonping import ping
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Viping")
root.geometry("300x250")

# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

# создаем пару фреймвов
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)

# добавляем фреймы в качестве вкладок
notebook.add(frame1, text="Pinger")
notebook.add(frame2, text="CheckDevice")


def start_ping():
    ping_adress = entry.get()
    print (ping_adress)
    s = ping(ping_adress, verbose=True)
    label ["text"] = s


entry = ttk.Entry()
entry.pack(frame1, anchor=NW, padx=6, pady=6)

btn = ttk.Button(text="Click", command=start_ping)
btn.pack(frame1, anchor=NW, padx=6, pady=6)

label = ttk.Label()
label.pack(frame1, anchor=NW, padx=6, pady=6)


root.mainloop()
