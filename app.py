# Importa a biblioteca Tkinter e dá a ela o apelido "tk"
# Tkinter é a biblioteca padrão do Python para criação de interfaces gráficas (GUI)
import tkinter as tk

# Importa apenas o módulo messagebox da biblioteca Tkinter
# Esse módulo permite exibir caixas de mensagem como alerta, erro, confirmação etc.
from tkinter import messagebox


# Cria a janela principal da aplicação
# Tk() inicializa o sistema gráfico do Tkinter
window = tk.Tk()

# Define o título da janela que aparecerá na barra superior
window.title("My App")

# Define o tamanho da janela (largura x altura) em pixels
window.geometry("340x440")

# Define a cor de fundo da janela
# Está comentado (não será executado)
# Se fosse usado, mudaria o fundo para cinza escuro
#window.configure(bg='#333333')


# Esse bloco foi um teste anterior do autor do código
# Está entre três aspas (''' ''') e por isso não será executado
# Provavelmente era apenas para testar a leitura dos campos

'''def login():
    username = username_entry.get()
    password = password_entry.get()
    print(f"Username: {username}, Password: {password}")'''


# Criação da função login()
# Essa função será executada quando o botão "Login" for clicado
def login():

    # Define o usuário correto que poderá entrar no sistema
    username = 'Denis'

    # Define a senha correta
    password = '12345'

    # username_entry.get() -> pega o texto digitado no campo de usuário
    # password_entry.get() -> pega o texto digitado no campo de senha
    # O IF verifica se os dois valores são iguais aos definidos acima
    if username_entry.get() == username and password_entry.get() == password:

        # Se estiver correto, mostra uma mensagem de sucesso
        messagebox.showinfo("Login Successful", "Usuário logado com sucesso!")

    else:

        # Caso contrário, imprime no terminal uma mensagem de erro
        print("Login failed. Please check your username and password.")

        # Mostra uma caixa de mensagem de erro na tela
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")


# Cria um Frame
# Frame é um container usado para organizar elementos dentro da janela
frame = tk.Frame()

# Posiciona o frame na janela usando o gerenciador de layout GRID
# row = linha
# column = coluna
# padx = espaço horizontal externo
# pady = espaço vertical externo
frame.grid(row=0, column=0, padx=10, pady=10)


# ---------------------------------------------------
# CRIAÇÃO DOS COMPONENTES (WIDGETS)
# ---------------------------------------------------


# Cria um texto grande escrito "Login"
login_label = tk.Label(frame, text="Login", font=("Arial", 20), fg="blue")

# Cria o texto "Username"
username_label = tk.Label(frame, text="Username", font=("Arial", 12))

# Cria o campo de entrada de texto para o usuário digitar o nome
username_entry = tk.Entry(frame, font=("Arial", 12))

# Cria o texto "Password"
password_label = tk.Label(frame, text="Password", font=("Arial", 12))

# Cria o campo de senha
# show="*" faz com que os caracteres digitados apareçam como *
password_entry = tk.Entry(frame, font=("Arial", 12), show="*")

# Cria o botão de login
login_button = tk.Button(
    frame,
    text="Login",
    font=("Arial", 12),
    bg="blue",      # cor de fundo
    fg="white",     # cor do texto
    command=login   # função que será executada ao clicar
)


# ---------------------------------------------------
# POSICIONAMENTO DOS ELEMENTOS NA TELA (GRID)
# ---------------------------------------------------


# Posiciona o título "Login"
# sticky="news" faz o elemento se expandir nas direções
login_label.grid(row=0, column=0, padx=10, pady=10, sticky=("news"))

# Posiciona o texto "Username"
username_label.grid(row=1, column=0, padx=10, pady=5)

# Posiciona o campo de digitação do usuário
username_entry.grid(row=1, column=1, padx=10, pady=5)

# Posiciona o texto "Password"
password_label.grid(row=2, column=0, padx=10, pady=5)

# Posiciona o campo da senha
password_entry.grid(row=2, column=1, padx=10, pady=5)

# Posiciona o botão
# columnspan=2 faz o botão ocupar duas colunas
login_button.grid(row=3, column=0, columnspan=2, pady=10)


# Inicia o loop principal da interface gráfica
# Esse loop mantém a janela aberta esperando eventos
# (cliques, teclado, interações do usuário)
window.mainloop()