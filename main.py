from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

def save() :
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password":password,
        }
    }    

    if len(password) == 0 or len(website) == 0 or len(email) == 0 :
        messagebox.showerror("Error", "Please fill all fields")
    else :    
        try :
            with open("Day_29\\data.json", mode="r") as file :
                data = json.load(file)
        except FileNotFoundError :
            with open("Day_29\\data.json", mode="w") as file :
                json.dump(new_data, file, indent=4)
        else :
            data.update(new_data)
            with open("Day_29\\data.json", mode="w") as file :
                json.dump(data, file, indent=4)
        finally :
                website_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)

def find_password() :
    website = website_input.get()
    try :
        with open("Day_29\\data.json") as file :
            data = json.load(file)
    except FileNotFoundError :
        messagebox.showinfo(title="File not found", message="Data is missing")
    else :
        if website in data :
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else :
            messagebox.showinfo(title="Error", message=f"No details for {website} exist ")

window=Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Day_29\\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=2)

website_label = Label(text="Website :", font=("Arial", 12, "bold"))
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.grid(column=1 ,row=1)
website_input.focus()
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username :", font=("Arial", 12, "bold"))
email_label.grid(column=0, row=2)
email_input = Entry(width=35)
email_input.grid(column=1 ,row=2, columnspan=2)

password_label = Label(text="Password :", font=("Arial", 12, "bold"))
password_label.grid(column=0, row=3)
password_input = Entry(width=35)
password_input.grid(column=1 ,row=3)
genpass_button = Button(text="Generate", command=generate_password)
genpass_button.grid(column=2, row=3) 

add_button = Button(text="Add", width=30, command=save, font=("Arial", 12, "bold"))
add_button.grid(column=1, row=4, columnspan=2) 

window.mainloop()
