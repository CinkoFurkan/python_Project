from tkinter import *
from tkinter import messagebox
import random
import pyperclip

window = Tk()
window.minsize(width=600, height=600)
window.title("Password Manager")
window.config(padx=20, pady=20)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def cleaner():
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()


def saving_information():
    website_info = website_entry.get()
    username_info = username_entry.get()
    password_info = password_entry.get()

    if len(website_info) == 0 or len(username_info) == 0 or len(password_info) == 0:
        messagebox.askretrycancel(website_info, "something is missing, please fill in all fields")
    else:
        user_confirming = messagebox.askokcancel(f"{website_info}", f"These are the entered: \nWebsite:{website_info}"
                                                                    f"\nEmail:{username_info}"
                                                                    f"\nPassword: {password_info} \n Is it okay to "
                                                                    f"save? ")
        if user_confirming:
            with open("information.txt", "a") as file:
                file.write(f"{website_info} || {username_info} || {password_info}\n")
            cleaner()


# ---------------------------- UI SETUP ------------------------------- #
canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0, columnspan=2)

website = Label(text="Website: ")
username = Label(text="Email/Username: ")
password = Label(text="Password: ")
website_entry = Entry(width=40)
username_entry = Entry(width=40)
password_entry = Entry(width=22)
password_generator_button = Button(text="Generate Password", command=password_generator)
add_button = Button(text="Add", width=13, command=saving_information)

website.grid(column=0, row=1)
username.grid(column=0, row=2)
password.grid(column=0, row=3)
website_entry.grid(column=1, row=1, columnspan=2)
username_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)
password_generator_button.grid(column=2, row=3)
add_button.grid(column=2, row=4)

website_entry.focus()
# username_entry.insert(0, "furkan_cinko23@hotmail.com")

window.mainloop()
