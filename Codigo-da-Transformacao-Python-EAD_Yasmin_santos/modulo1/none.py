import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def saudar_usuario():
    nome = entrada_nome.get() # Pega o texto que o usuário digitou
    
    if not nome.strip():
        messagebox.showwarning("Aviso", "Por favor, digite seu nome!")
        return

    
    agora = datetime.now()
    hora_formatada = agora.strftime("%H:%M")
    
    texto_resultado.config(text=f"Oi, {nome}!\nAgora são {hora_formatada}.")

janela = tk.Tk()
janela.title("Introdução ao Python - Modulo 02")
janela.geometry("350x220") # Define o tamanho da janela
janela.configure(bg="#1e1e1e") # Cor de fundo escura (estilo VS Code)
ss



titulo = tk.Label(janela, text="Primeiro Programa", font=("Arial", 14, "bold"), fg="#ffffff", bg="#1e1e1e")
titulo.pack(pady=15)


instrucao = tk.Label(janela, text="Qual é o seu nome?", font=("Arial", 10), fg="#cccccc", bg="#1e1e1e")
instrucao.pack()

# 3. Caixa de Entrada (Onde o usuário digita)
entrada_nome = tk.Entry(janela, font=("Arial", 11), width=25, justify="center")
entrada_nome.pack(pady=5)
entrada_nome.focus() # Já deixa o cursor piscando aqui dentro

# 4. Botão para Executar
# Usamos cores que combinam com o Python (azul e amarelo)
botao_enviar = tk.Button(janela, text="Enviar", font=("Arial", 10, "bold"), fg="#1e1e1e", bg="#ffd43b", 
                         activebackground="#4b8bbe", command=saudar_usuario, width=12)
botao_enviar.pack(pady=10)

# 5. Label para exibir o resultado final
texto_resultado = tk.Label(janela, text="", font=("Arial", 11, "bold"), fg="#4b8bbe", bg="#1e1e1e")
texto_resultado.pack(pady=5)

# Inicia o loop da interface gráfica (mantém a janela aberta)
janela.mainloop()