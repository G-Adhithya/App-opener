# Ugly app-opener

import tkinter as tk
import os
from tkinter import Text, filedialog, PhotoImage

# App configurations
app = tk.Tk()
app.title("App opener")
app.geometry("750x530")
icon = PhotoImage(
    file="E:\\Programming\\Python\\App-opener\\src\img\\icon.png")
app.iconphoto(False, icon)
app.resizable(False, False)
app.configure(bg="#F25757")

apps = []

# Functionality

if os.path.isfile("Files.txt"):
    with open("Files.txt", "r") as f:
        applist = f.read()
        applist = applist.split(",")
        apps = [x for x in applist if x.split()]


def file_opener():
    for widget in frame.winfo_children():
        widget.destroy()

    files = filedialog.askopenfilename(title="Select your app", filetypes=(
        ("Executables", "*.exe"), ("All files", "*.*")))

    apps.append(files)

    for appp in apps:
        label = tk.Label(frame, fg="black", text=appp)
        label.pack()


def runner():
    for appp in apps:
        os.startfile(appp)


# GUI
frame = tk.Frame(app, bg="#F3B700")
frame.place(relheight=0.8, relwidth=0.88, relx=0.05, rely=0)

fileBtn = tk.Button(app, text="Open the files",
                    bg="#61E8E1", width=40, height=2, border=0, command=file_opener)
fileBtn.place(relx=0.05, rely=0.86)

runBtn = tk.Button(app, text="Run the apps", bg="#61E8E1",
                   width=40, height=2, border=0, command=runner)
runBtn.place(relx=0.55, rely=0.86)


for appp in apps:
    label = tk.Label(frame, fg="black", text=appp)
    label.pack()

app.mainloop()

# Extra functionality
with open("Files.txt", "w") as f:
    for appp in apps:
        f.write(appp + ",")
