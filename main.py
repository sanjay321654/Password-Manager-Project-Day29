from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
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
    new_json_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oops..", message="These fields cannot be empty.")

    else:
        try:
            with open("data.json", "r") as data:
                """Reading the old data"""
                data_file = json.load(data)

                """Updating new data with old data"""
                data_file.update(new_json_data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_json_data, data, indent=4)

        else:
            """Writing the new data into json file"""
            with open("data.json", "w") as data:
                json.dump(data_file, data, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)


# -----------------------------FIND PASSWORD ----------------------------#
def find_password():
    web = web_entry.get()
    try:
        with open("data.json", "r") as data:
            data_file = json.load(data)

    except FileNotFoundError:
        messagebox.showinfo(title="error", message="No data file found")

    else:
        if web in data_file:
            email = data_file[web]["email"]
            password = data_file[web]["password"]
            messagebox.showinfo(title=web, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showwarning(title="Error", message=f"No details for the {web} exists.")


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

web_entry = Entry(width=31, bg=YELLOW)
web_entry.grid(column=1, row=1)
web_entry.focus()

email_entry = Entry(width=50, bg=YELLOW)
email_entry.grid(column=1, row=2, columnspan=2)
# email_entry.insert(0, "Ex: sanjay@gmail.com")

password_entry = Entry(width=31, bg=YELLOW)
password_entry.grid(column=1, row=3)

password_gen = Button(text="Generate Password", bg=YELLOW, command=password_generator)
password_gen.grid(column=2, row=3, columnspan=1, pady=4)

search_button = Button(text="Search", width=10, bg=YELLOW, command=find_password)
search_button.grid(row=1, column=2, pady=4, columnspan=1)

add_button = Button(text="Add", width=42, bg=YELLOW, command=save)
add_button.grid(column=1, row=4, columnspan=2, pady=3)

window.mainloop()
