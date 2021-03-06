import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    blank.delete("1.0", END)
    file = askopenfilename(mode="r", filetypes=[("text files", "*.txt")])
    if file is not None:
        text = file.read()
        blank.insert("1.0", text)

def save_file():
    text = blank.get("1.0", "end-1c")
    file = asksaveasfilename(title="Save", filetypes=[("text files", "*.txt")])
    with open(file, "w") as data:
        data.write(text)

window = tkinter.Tk()
window.title("Text Editor")

menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Exit", command=window.destroy)

blank = Text(window,font=("arial", 10))
blank.pack()

if __name__ == "__name__":
    window.mainloop()
