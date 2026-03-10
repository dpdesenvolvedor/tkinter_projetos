import tkinter as tk
import sqlite3


class ClientesView:

    def __init__(self, window):

        self.window = window
        self.window.title("Cadastro de Clientes")

        tk.Label(window, text="Nome").pack()
        self.nome = tk.Entry(window)
        self.nome.pack()

        tk.Label(window, text="Telefone").pack()
        self.telefone = tk.Entry(window)
        self.telefone.pack()

        tk.Label(window, text="Email").pack()
        self.email = tk.Entry(window)
        self.email.pack()

        tk.Button(window, text="Salvar", command=self.salvar).pack()


    def salvar(self):

        conn = sqlite3.connect("erp.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO clientes (nome,telefone,email) VALUES (?,?,?)",
            (self.nome.get(), self.telefone.get(), self.email.get())
        )

        conn.commit()
        conn.close()