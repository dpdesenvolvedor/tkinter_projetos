import tkinter as tk
from tkinter import messagebox

class LoginApp:

    def __init__(self, window):

        # Guarda referência da janela
        self.window = window
        self.window.title("My App")
        self.window.geometry("340x440")

        # Frame principal
        self.frame = tk.Frame(self.window)
        self.frame.pack(pady=40)

        # Título
        self.login_label = tk.Label(self.frame, text="Login", font=("Arial", 20), fg="blue")
        self.login_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Usuário
        tk.Label(self.frame, text="Username").grid(row=1, column=0)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=1, column=1)

        # Senha
        tk.Label(self.frame, text="Password").grid(row=2, column=0)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=2, column=1)

        # Botão
        self.login_button = tk.Button(self.frame, text="Login", command=self.login)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):

        username = "Denis"
        password = "12345"

        if self.username_entry.get() == username and self.password_entry.get() == password:
            messagebox.showinfo("Success", "Login successful")
        else:
            messagebox.showerror("Error", "Invalid login")


window = tk.Tk()

app = LoginApp(window)

window.mainloop()