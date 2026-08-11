import tkinter as tk
from tkinter import messagebox


def saudar_usuario():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    porte = entrada_porte.get()

    if not nome.strip():
        messagebox.showwarning("Aviso", "Por favor, digite o nome do Pet!")
        return

    if not idade.strip():
        messagebox.showwarning("Aviso", "Por favor, digite a idade do Pet!")
        return

    if not porte.strip():
        messagebox.showwarning("Aviso", "Por favor, digite o porte do Pet!")
        return

    texto_resultado.config(
        text="🐾 Pet cadastrado com sucesso!"
    )


janela = tk.Tk()
janela.title("PetsZ - Cadastro de Pets")
janela.geometry("350x500")
janela.configure(bg="#953676")


# Logo
logo = tk.PhotoImage(file="logopetz.png")

imagem_logo = tk.Label(
    janela,
    image=logo,
    bg="#953676"
)
imagem_logo.pack(pady=10)


# Título
titulo = tk.Label(
    janela,
    text="💕 Pets Z 💕",
    font=("Arial", 14, "bold"),
    fg="#ffffff",
    bg="#953676"
)
titulo.pack(pady=15)


# Subtítulo
titulo = tk.Label(
    janela,
    text="Informações do Pet",
    font=("Arial", 14, "bold"),
    fg="#ffffff",
    bg="#953676"
)
titulo.pack(pady=15)


# Nome do Pet
instrucao = tk.Label(
    janela,
    text="Qual o nome do Pet",
    font=("Arial", 10),
    fg="#cccccc",
    bg="#953676"
)
instrucao.pack()

entrada_nome = tk.Entry(
    janela,
    font=("Arial", 11),
    width=25,
    justify="center"
)
entrada_nome.pack(pady=10)

entrada_nome.focus()


# Idade do Pet
instrucao = tk.Label(
    janela,
    text="Qual a idade do Pet",
    font=("Arial", 10),
    fg="#cccccc",
    bg="#953676"
)
instrucao.pack()

entrada_idade = tk.Entry(
    janela,
    font=("Arial", 11),
    width=25,
    justify="center"
)
entrada_idade.pack(pady=10)


# Porte do Pet
instrucao = tk.Label(
    janela,
    text="Qual o porte do Pet",
    font=("Arial", 10),
    fg="#cccccc",
    bg="#953676"
)
instrucao.pack()

entrada_porte = tk.Entry(
    janela,
    font=("Arial", 11),
    width=25,
    justify="center"
)
entrada_porte.pack(pady=10)


# Botão Enviar
botao_enviar = tk.Button(
    janela,
    text="Enviar",
    font=("Arial", 10, "bold"),
    fg="#1e1e1e",
    bg="#ffd43b",
    activebackground="#4b8bbe",
    command=saudar_usuario,
    width=10
)
botao_enviar.pack(pady=10)


# Resultado
texto_resultado = tk.Label(
    janela,
    text="",
    font=("Arial", 11, "bold"),
    fg="#ffffff",
    bg="#953676"
)
texto_resultado.pack(pady=5)


# Inicia o programa
janela.mainloop()