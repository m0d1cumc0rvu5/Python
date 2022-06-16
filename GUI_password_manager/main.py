#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# Change E-mail here
hard_coded_email = 'johndoe@johndoe.com'
# Change data.txt file location. Ensure the 'r' is included if you are relocating file to a different folder.
# Linux r'/home/user/Desktop/secrets.txt' // Windows r'C:\Users\user\Desktop\secrets.txt'
hard_coded_saved_secrets_location = r'data.txt'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please enter valid info")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {password}\n       Continue?")

        if is_ok:
            messagebox.showinfo(title="Verification", message="Complete!")
            with open(f"{hard_coded_saved_secrets_location}", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# labels
website_text = Label(text="Website:")
website_text.grid(column=0, row=1)

email_username_text = Label(text="Email/Username:")
email_username_text.grid(column=0, row=2)

password_prompt_text = Label(text="Password:")
password_prompt_text.grid(column=0, row=3)

# buttons
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=36)

generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(column=2, row=3)

# entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=35)
# focus on the website entry pane at start
website_entry.focus()

email_username_entry = Entry(width=40)
email_username_entry.grid(column=1, row=2, columnspan=35)
# enter most commonly used email at first entry point in email_username_entry entry
email_username_entry.insert(0, f"{hard_coded_email}")

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)


# canvas
canvas = Canvas(width=300, height=200)
mypass_photo = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=mypass_photo)
canvas.grid(column=1, row=0, columnspan=200, pady=20)


window.mainloop()
