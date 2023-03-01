from tkinter import *
import persona
from PIL import ImageTk, Image

root = Tk()
root.geometry("800x600")  # Center of the screen, kinda
root.title("Persona Compendium")
root.resizable(False, False)

# Placing Phantom thieves logo as the background

my_canvas = Canvas(root, width=800, height=600)
my_canvas.pack(fill="both", expand=TRUE)

bg = ImageTk.PhotoImage(Image.open("images/Logo.png"))
my_canvas.create_image(0, 0, image=bg, anchor="nw")


# Getting the user input

message = Label(root, text="Search for any persona", font=("overstrike", 20), bg="red", fg="black")

user_input = Entry(root, bg="red", fg="black")

persona_label = Label(root)  # Defining info so it can be overwritten later


# Getting the info from persona.py


def persona_info():
    global persona_label
    persona_label.destroy()  # Cleaning previous info
    try:
        formatted_info = (persona.Compendium[str(user_input.get())].info())
    except KeyError:
        formatted_info = "No persona of that name available. Try again"

    persona_label = Label(root, text=formatted_info, font=("bold", 17), bg="red", fg="black")
    persona_label.place(relx=0.5, rely=0.7, anchor=CENTER)

# Defining image placement (Work in progress!, only Alice works for now)

def image_info():
    global image, new_bg_picture

    try:

        image = (persona.Images[str(user_input.get())])
        new_bg_picture = ImageTk.PhotoImage(Image.open(persona.Images[str(user_input.get())]))

        my_canvas.create_image(0, 0, image=new_bg_picture, anchor="nw")

    except KeyError:
        pass

button = Button(root, text="Search", command=lambda: [image_info(), persona_info()], bg="red", fg="white")

# Packing

message.place(relx=0.5, rely=0.4, anchor=CENTER)
user_input.place(relx=0.5, rely=0.5, anchor=CENTER)
button.place(relx=0.5, rely=0.55, anchor=CENTER)

root.mainloop()
