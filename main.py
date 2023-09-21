from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(6, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 5))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oops..", message="These fields cannot be empty.")

    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered\n Email: {email}"
                                                              f"\n Password: {password}")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website}| {email} | {password}\n")
                web_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, background=GREEN)

canvas = Canvas(width=200, height=200, highlightthickness=0, bg=GREEN)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", bg=GREEN)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ", bg=GREEN)
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ", bg=GREEN)
password_label.grid(column=0, row=3)

web_entry = Entry(width=35, bg=YELLOW)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=35, bg=YELLOW)
email_entry.grid(column=1, row=2, columnspan=2)
# email_entry.insert(0, "Ex: sanjay@gmail.com")

password_entry = Entry(width=17, bg=YELLOW)
password_entry.grid(column=1, row=3)

password_gen = Button(text="Generate Password", bg=YELLOW, command=password_generator)
password_gen.grid(column=2, row=3, columnspan=1)

add_button = Button(text="Add", width=30, bg=YELLOW, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
