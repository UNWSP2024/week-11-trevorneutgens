import tkinter as tk

def show_info():

    text = "Name: Trevor Neutgens\nAddress: 2984 Thunder Bay Road"
    info_label.config(text=text)

def quit_program():
    root.quit()


root = tk.Tk()
root.title("Personal Information")


info_label = tk.Label(root)
info_label.pack()


tk.Button(root, text="Show Info", command=show_info).pack()
tk.Button(root, text="Quit", command=quit_program).pack()

root.mainloop()
