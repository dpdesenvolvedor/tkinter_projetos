import tkinter as tk
import sqlite3


class ProdutosView:

    def __init__(self, window):

        self.window = window
        self.window.title("Cadastro de Produtos")

        tk.Label(window, text="Nome").pack()
        self.nome = tk.Entry(window)
        self.nome.pack()

        tk.Label(window, text="Preço").pack()
        self.preco = tk.Entry(window)
        self.preco.pack()

        tk.Label(window, text="Estoque").pack()
        self.estoque = tk.Entry(window)
        self.estoque.pack()

        tk.Button(window, text="Salvar", command=self.salvar).pack()


    def salvar(self):

        conn = sqlite3.connect("erp.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO produtos (nome,preco,estoque) VALUES (?,?,?)",
            (self.nome.get(), self.preco.get(), self.estoque.get())
        )

        conn.commit()
        conn.close()