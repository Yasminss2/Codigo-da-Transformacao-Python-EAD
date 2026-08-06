import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def saudar_usuario():
    nome = entrada_nome.get() # Pega o texto que o usuário digitou
    
    if not nome.strip():
        messagebox.showwarning("Aviso", "Por favor, digite seu nome!")
        return

    
    agora = datetime.now()
    mensagem_formatada = agora.strftime("%H:%M")
    
    texto_resultado.config(text=f"Olá, {nome}!\nSeja bem vindo(a) {mensagem_formatada}.")

janela = tk.Tk()
janela.title("Introdução ao Python - Modulo 02")
janela.geometry("350x400") # Define o tamanho da janela
janela.configure(bg="#953676") # Cor de fundo escura (estilo VS Code)


titulo = tk.Label(janela, text="💕Pets Z 💕", font=("Arial", 14, "bold"), fg="#ffffff", bg="#953676")
titulo.pack(pady=15)

titulo = tk.Label(janela, text="Informações do  Pet", font=("Arial", 14, "bold"), fg="#ffffff", bg="#953676")
titulo.pack(pady=15)

instrucao = tk.Label(janela, text="Qual o nome do Pet", font=("Arial", 10), fg="#cccccc", bg="#953676")
instrucao.pack()

# 5. Caixa de Entrada (Onde o usuário digita)
entrada_nome = tk.Entry(janela, font=("Arial", 11), width=25, justify="center")
entrada_nome.pack(pady=10)

entrada_nome.focus() # Já deixa o cursor piscando aqui dentro
instrucao = tk.Label(janela, text="Qual a idade do Pet", font=("Arial", 10), fg="#cccccc", bg="#953676")
instrucao.pack()

# 6. Caixa de Entrada (Onde o usuário digita)
entrada_nome = tk.Entry(janela, font=("Arial", 11), width=25, justify="center")
entrada_nome.pack(pady=10)

entrada_nome.focus() # Já deixa o cursor piscando aqui dentro
instrucao = tk.Label(janela, text="Qual o porte do Pet", font=("Arial", 10), fg="#cccccc", bg="#953676")
instrucao.pack()

# 3. Caixa de Entrada (Onde o usuário digita)
entrada_nome = tk.Entry(janela, font=("Arial", 11), width=25, justify="center")
entrada_nome.pack(pady=10)
entrada_nome.focus() # Já deixa o cursor piscando aqui dentro

# 7. Botão para Executar
# Usamos cores que combinam com o Python (azul e amarelo)
botao_enviar = tk.Button(janela, text="Enviar", font=("Arial", 10, "bold"), fg="#1e1e1e", bg="#ffd43b", 
                         activebackground="#4b8bbe", command=saudar_usuario, width=10)
botao_enviar.pack(pady=10)

# 8. Label para exibir o resultado final
texto_resultado = tk.Label(janela, text="", font=("Arial", 11, "bold"), fg="#4b8bbe", bg="#1e1e1e")
texto_resultado.pack(pady=5)

# Inicia o loop da interface gráfica (mantém a janela aberta)
janela.mainloop()