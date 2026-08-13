import io
import urllib.request
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


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

    # Sugestão: Mensagem mais limpa e direta na interface
    texto_resultado.config(
        text="✨ Cadastrado com sucesso! ✨",
        fg="#2ecc71"  # Verde para indicar sucesso
    )
    
    # Opcional: Também podemos limpar os campos após o cadastro
    # entrada_nome.delete(0, tk.END)
    # entrada_idade.delete(0, tk.END)
    # entrada_porte.delete(0, tk.END)
    # entrada_nome.focus()


janela = tk.Tk()
janela.title("PetsZ - Cadastro de Pets")
janela.geometry("350x620")
janela.configure(bg="#000000")

# Carregando Imagem da Internet
try:
    url = "https://i.pinimg.com/236x/ae/c0/1c/aec01c54bc071d90cd561d58ac9a0ae9.jpg"
    with urllib.request.urlopen(url) as conexao:
        dados_imagem = conexao.read()
    
    imagem_stream = io.BytesIO(dados_imagem)
    imagem_pil = Image.open(imagem_stream)
    
    imagem_pil = imagem_pil.resize((180, 90), Image.Resampling.LANCZOS)
    imagem_tk = ImageTk.PhotoImage(imagem_pil)

    imagem_logo = tk.Label(janela, image=imagem_tk, bg="#000000")
    imagem_logo.image = imagem_tk
    imagem_logo.pack(pady=10)
except Exception as e:
    imagem_logo = tk.Label(janela, text="[Erro ao carregar imagem]", fg="#ffffff", bg="#000000")
    imagem_logo.pack(pady=10)

# Título
titulo = tk.Label(
    janela,
    text="💕 Pets Z 💕",
    font=("Arial", 14, "bold"),
    fg="#ffffff",
    bg="#000000"
)
titulo.pack(pady=5)

# Subtítulo
subtitulo = tk.Label(
    janela,
    text="Informações do Pet",
    font=("Arial", 12, "bold"),
    fg="#ffffff",
    bg="#000000"
)
subtitulo.pack(pady=5)

# Nome do Pet
instrucao_nome = tk.Label(
    janela,
    text="Qual o nome do Pet",
    font=("Arial", 10),
    fg="#cccccc",
    bg="#000000"
)
instrucao_nome.pack()

entrada_nome = tk.Entry(
    janela,
    font=("Arial", 11),
    width=25,
    justify="center"
)
entrada_nome.pack(pady=5)
entrada_nome.focus()

# Idade do Pet
instrucao_idade = tk.Label(
    janela,
    text="Qual a idade do Pet",
    font=("Arial", 10),
    fg="#cccccc",
    bg="#000000"
)
instrucao_idade.pack()

entrada_idade = tk.Entry(
    janela,
    font=("Arial", 11),
    width=25,
    justify="center"
)
entrada_idade.pack(pady=5)

# Porte do Pet
instrucao_porte = tk.Label(
    janela,
    text="Qual o porte do Pet",
    font=("Arial", 10),
    fg="#cccccc",
    bg="#000000"
)
instrucao_porte.pack()

entrada_porte = tk.Entry(
    janela,
    font=("Arial", 11),
    width=25,
    justify="center"
)
entrada_porte.pack(pady=5)

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
    bg="#000000"
)
texto_resultado.pack(pady=5)

# Inicia o programa
janela.mainloop()