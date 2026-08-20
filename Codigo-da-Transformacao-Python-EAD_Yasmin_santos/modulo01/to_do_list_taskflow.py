# Biblioteca principal para criar a interface gráfica
import tkinter as tk

# Componentes adicionais do Tkinter, como o Combobox
from tkinter import ttk

# Permite trabalhar com data e horário
from datetime import datetime


# Configuração da janela principal

janela = tk.Tk()
janela.title("TaskFlow")
janela.geometry("420x650")
janela.resizable(False, False)

# 🎨 Cores do TaskFlow
AZUL = "#4A90E2"
AMARELO = "#FFD166"
VERDE = "#4CAF50"
ROSA = "#FF6F91"
FUNDO = "#F7F9FC"
BRANCO = "#FFFFFF"
CINZA = "#6B7280"
TEXTO = "#263238"

# Cor de fundo da janela
janela.config(bg=FUNDO)

# Lista que vai armazenar as tarefas
tarefas = []


# Função para atualizar a lista de tarefas

def atualizar_lista():

    for widget in lista_frame.winfo_children():
        widget.destroy()

    filtro = filtro_var.get()

    if filtro == "Tarefas pendentes":
        tarefas_exibir = [
            t for t in tarefas
            if not t["concluida"]
        ]

    elif filtro == "Tarefas concluídas":
        tarefas_exibir = [
            t for t in tarefas
            if t["concluida"]
        ]

    else:
        tarefas_exibir = tarefas

    if not tarefas_exibir:

        vazio = tk.Label(
            lista_frame,
            text="Nenhuma tarefa encontrada.",
            font=("Arial", 12),
            bg=FUNDO,
            fg=CINZA
        )

        vazio.pack(pady=30)

        return

    for tarefa in tarefas_exibir:
        criar_tarefa(tarefa)


# Função que cria uma tarefa na tela

def criar_tarefa(tarefa):

    tarefa_frame = tk.Frame(
        lista_frame,
        bd=0,
        padx=10,
        pady=8,
        bg=BRANCO
    )

    tarefa_frame.pack(
        fill="x",
        padx=15,
        pady=5
    )

    if tarefa["concluida"]:

        simbolo = "✓"
        cor_botao = VERDE
        cor_texto = CINZA

    else:

        simbolo = "○"
        cor_botao = ROSA
        cor_texto = TEXTO

    texto = (
        f'{tarefa["nome"]}\n'
        f'📅 {tarefa["data"]}   ⏰ {tarefa["hora"]}'
    )

    texto_label = tk.Label(
        tarefa_frame,
        text=texto,
        font=("Arial", 11),
        fg=cor_texto,
        bg=BRANCO,
        justify="left"
    )

    texto_label.pack(
        side="left",
        fill="x",
        expand=True
    )

    botao_concluir = tk.Button(
        tarefa_frame,
        text=simbolo,
        font=("Arial", 18, "bold"),
        fg=cor_botao,
        bg=BRANCO,
        activeforeground=VERDE,
        bd=0,
        command=lambda: concluir_tarefa(tarefa)
    )

    botao_concluir.pack(side="right")


# Função para concluir uma tarefa

def concluir_tarefa(tarefa):

    tarefa["concluida"] = not tarefa["concluida"]

    atualizar_lista()


# Função para abrir a tela de nova tarefa

def abrir_adicionar():

    janela_adicionar = tk.Toplevel(janela)

    janela_adicionar.title("Nova tarefa")
    janela_adicionar.geometry("350x400")
    janela_adicionar.resizable(False, False)
    janela_adicionar.config(bg=FUNDO)


    # Título da segunda janela

    titulo = tk.Label(
        janela_adicionar,
        text="Nova tarefa",
        font=("Arial", 20, "bold"),
        bg=FUNDO,
        fg=AZUL
    )

    titulo.pack(pady=20)


    # Campo para o nome da tarefa

    nome_label = tk.Label(
        janela_adicionar,
        text="Tarefa:",
        font=("Arial", 11, "bold"),
        bg=FUNDO,
        fg=TEXTO
    )

    nome_label.pack(
        anchor="w",
        padx=30
    )

    nome_entry = tk.Entry(
        janela_adicionar,
        font=("Arial", 12),
        bg=BRANCO,
        fg=TEXTO,
        highlightthickness=1,
        highlightbackground=AZUL
    )

    nome_entry.pack(
        fill="x",
        padx=30,
        pady=5
    )


    # Campo para a data

    data_label = tk.Label(
        janela_adicionar,
        text="Data:",
        font=("Arial", 11, "bold"),
        bg=FUNDO,
        fg=TEXTO
    )

    data_label.pack(
        anchor="w",
        padx=30,
        pady=(15, 0)
    )

    data_entry = tk.Entry(
        janela_adicionar,
        font=("Arial", 12),
        bg=BRANCO,
        fg=TEXTO,
        highlightthickness=1,
        highlightbackground=AMARELO
    )

    data_entry.pack(
        fill="x",
        padx=30,
        pady=5
    )

    data_entry.insert(
        0,
        datetime.now().strftime("%d/%m/%Y")
    )


    # Campo para o horário

    hora_label = tk.Label(
        janela_adicionar,
        text="Horário:",
        font=("Arial", 11, "bold"),
        bg=FUNDO,
        fg=TEXTO
    )

    hora_label.pack(
        anchor="w",
        padx=30,
        pady=(15, 0)
    )

    hora_entry = tk.Entry(
        janela_adicionar,
        font=("Arial", 12),
        bg=BRANCO,
        fg=TEXTO,
        highlightthickness=1,
        highlightbackground=ROSA
    )

    hora_entry.pack(
        fill="x",
        padx=30,
        pady=5
    )

    hora_entry.insert(
        0,
        datetime.now().strftime("%H:%M")
    )


    # Função para adicionar a tarefa

    def adicionar():

        nome = nome_entry.get().strip()
        data = data_entry.get().strip()
        hora = hora_entry.get().strip()

        if nome == "":
            return

        nova_tarefa = {
            "nome": nome,
            "data": data,
            "hora": hora,
            "concluida": False
        }

        tarefas.append(nova_tarefa)

        atualizar_lista()

        janela_adicionar.destroy()


    # Botão para adicionar a tarefa

    botao_adicionar = tk.Button(
        janela_adicionar,
        text="Adicionar tarefa",
        font=("Arial", 11, "bold"),
        bg=VERDE,
        fg=BRANCO,
        activebackground=AZUL,
        activeforeground=BRANCO,
        bd=0,
        padx=15,
        pady=8,
        command=adicionar
    )

    botao_adicionar.pack(pady=25)


# Título da tela principal

titulo = tk.Label(
    janela,
    text="TaskFlow",
    font=("Arial", 25, "bold"),
    bg=FUNDO,
    fg=AZUL
)

titulo.pack(
    pady=(25, 20)
)


# Cabeçalho

cabecalho = tk.Frame(
    janela,
    bg=FUNDO
)

cabecalho.pack(
    fill="x",
    padx=20
)


# Guarda a opção escolhida no filtro

filtro_var = tk.StringVar()
filtro_var.set("Tarefas pendentes")


# Filtro de tarefas

filtro = ttk.Combobox(
    cabecalho,
    textvariable=filtro_var,
    values=[
        "Tarefas pendentes",
        "Tarefas concluídas",
        "Todas as tarefas"
    ],
    state="readonly",
    width=23
)

filtro.pack(side="left")

filtro.bind(
    "<<ComboboxSelected>>",
    lambda evento: atualizar_lista()
)


# Botão "+"

botao_mais = tk.Button(
    cabecalho,
    text="+",
    font=("Arial", 20, "bold"),
    bg=AMARELO,
    fg=TEXTO,
    activebackground=ROSA,
    activeforeground=BRANCO,
    bd=0,
    padx=8,
    command=abrir_adicionar
)

botao_mais.pack(side="right")


# Área onde as tarefas aparecem

lista_frame = tk.Frame(
    janela,
    bg=FUNDO
)

lista_frame.pack(
    fill="both",
    expand=True,
    pady=20
)


# Inicialização

atualizar_lista()

janela.mainloop()