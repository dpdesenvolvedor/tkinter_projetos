import tkinter as tk
from tkinter import messagebox
import sqlite3


class LoginView:

    def __init__(self, window):

        self.window = window
        self.window.title("Mini ERP")
        self.window.geometry("300x200")

        tk.Label(window, text="Usuário").pack()

        self.username = tk.Entry(window)
        self.username.pack()

        tk.Label(window, text="Senha").pack()

        self.password = tk.Entry(window, show="*")
        self.password.pack()

        tk.Button(window, text="Login", command=self.login).pack(pady=10)


    def login(self):

        conn = sqlite3.connect("erp.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM usuarios WHERE username=? AND password=?",
            (self.username.get(), self.password.get())
        )

        user = cursor.fetchone()

        if user:

            messagebox.showinfo("Sucesso", "Login realizado")

        else:

            messagebox.showerror("Erro", "Usuário inválido")