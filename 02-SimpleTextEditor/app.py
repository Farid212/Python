from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile, asksavefilename

def open_file():
    blank.delete("1.0", END)
    file = askopenfile(mode="r", filetypes=[("text files", "*.txt")])
    if file is not None:
        text = file.read()
        blank.insert("1.0", text)

def save_file():
    text = blank.get("1.0", "end-1c")
    file = asksavefilename(title="Save", filetypes=[("text files", "*.txt")])
    with open(file, "w") as data:
        data.write(text)

window = Tk()
window.title("Text Editor")

menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Exit", command=window.destroy)

blank = Text(window, font("arial", 10))
blank.pack()

if __name__ == "__name__":
    window.mainloop()
