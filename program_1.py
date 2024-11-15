# Create a GUI window that displays your favorite saying.
import tkinter as tk

def main():

    main_window = tk.Tk()


    label = tk.Label(main_window, text="Hello there")
    label.pack()

    main_window.mainloop()


main()

