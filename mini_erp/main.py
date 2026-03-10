import tkinter as tk
from database.db import criar_tabelas
from views.login_view import LoginView

criar_tabelas()

window = tk.Tk()

app = LoginView(window)

window.mainloop()