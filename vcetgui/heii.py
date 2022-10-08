import tkinter
import tkinter.messagebox
import customtkinter


root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("400x240")
root_tk.title("CustomTkinter Test")


slider = customtkinter.CTkSlider(master=root_tk,
                                 width=160,
                                 height=16,
                                 border_width=5.5,)
slider.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)