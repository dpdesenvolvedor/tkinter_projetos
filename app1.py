import tkinter as tk

window = tk.Tk()
window.title("My App")
window.geometry("340x440")
#window.configure(bg='#333333')

def login():
    username = username_entry.get()
    password = password_entry.get()
    print(f"Username: {username}, Password: {password}")

frame =tk.Frame()
frame.grid(row=0, column=0, padx=10, pady=10)

#creatingh widgets
login_label = tk.Label(frame, text="Login", font=("Arial", 20), fg="blue")
username_label = tk.Label(frame, text="Username", font=("Arial", 12))
username_entry = tk.Entry(frame, font=("Arial", 12))
password_label = tk.Label(frame, text="Password", font=("Arial", 12))
password_entry = tk.Entry(frame, font=("Arial", 12), show="*")
login_button = tk.Button(frame, text="Login", font=("Arial", 12), 
                         bg="blue", fg="white", command="login")

login_label.grid(row=0, column=0, padx=10, pady=10, sticky=("news"))
username_label.grid(row=1, column=0, padx=10, pady=5)
username_entry.grid(row=1, column=1, padx=10, pady=5)
password_label.grid(row=2, column=0, padx=10, pady=5)
password_entry.grid(row=2, column=1, padx=10, pady=5)
login_button.grid(row=3, column=0, columnspan=2, pady=10)



window.mainloop()