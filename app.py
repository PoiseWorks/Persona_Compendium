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

message = Label(root, text="Search for any persona\nfrom persona 5", font=("Rooney Sans", 18), bg="white", fg="black")

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

    persona_label = Label(root, text=formatted_info, font=("bold", 12), bg="white", fg="black")
    persona_label.place(relx=0.8, rely=0.9, anchor=CENTER)

# Defining image placement

def image_info():
    global new_bg_picture

    try:

        new_bg_picture = ImageTk.PhotoImage(Image.open(persona.Images[str(user_input.get())]))

        my_canvas.create_image(0, 0, image=new_bg_picture, anchor="nw")

    except KeyError:
        pass

button = Button(root, text="Search", command=lambda: [image_info(), persona_info()], bg="red", fg="black")

# Packing

message.place(relx=0.8, rely=0.67, anchor=CENTER)
user_input.place(relx=0.8, rely=0.75, anchor=CENTER)
button.place(relx=0.8, rely=0.8, anchor=CENTER)

root.mainloop()
