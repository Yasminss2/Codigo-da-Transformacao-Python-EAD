# Biblioteca principal para criar a interface gráfica
import tkinter as tk

# Componentes adicionais do Tkinter, como o Combobox
from tkinter import ttk

# Permite trabalhar com data e horário
from datetime import datetime


# Configuração da janela principal

# Cria a janela principal do aplicativo
janela = tk.Tk()

# Define o título da janela
janela.title("TaskFlow")

# Define o tamanho da janela
# 420 = largura e 650 = altura
janela.geometry("420x650")

# Impede que o usuário altere o tamanho da janela
janela.resizable(False, False)

# Lista que vai armazenar as tarefas
tarefas = []


# Função para atualizar a lista de tarefas

# Atualiza as tarefas mostradas na tela
def atualizar_lista():

    # Remove os elementos antigos da área de tarefas
    for widget in lista_frame.winfo_children():
        widget.destroy()

    # Pega a opção escolhida no filtro
    filtro = filtro_var.get()

    # Mostra somente as tarefas que ainda não foram concluídas
    if filtro == "Tarefas pendentes":
        tarefas_exibir = [
            t for t in tarefas
            if not t["concluida"]
        ]

    # Mostra somente as tarefas concluídas
    elif filtro == "Tarefas concluídas":
        tarefas_exibir = [
            t for t in tarefas
            if t["concluida"]
        ]

    # Mostra todas as tarefas
    else:
        tarefas_exibir = tarefas

    # Se não houver tarefas, mostra uma mensagem
    if not tarefas_exibir:

        vazio = tk.Label(
            lista_frame,
            text="Nenhuma tarefa encontrada.",
            font=("Arial", 12)
        )

        vazio.pack(pady=30)

        # Para a função aqui
        return

    # Cria visualmente cada tarefa na tela
    for tarefa in tarefas_exibir:
        criar_tarefa(tarefa)


# Função que cria uma tarefa na tela

# Recebe uma tarefa e cria os elementos visuais dela
def criar_tarefa(tarefa):

    # Frame é uma área usada para organizar elementos
    # Cada tarefa terá seu próprio Frame
    tarefa_frame = tk.Frame(
        lista_frame,
        bd=0,
        padx=10,
        pady=8
    )

    # Coloca o Frame na área das tarefas
    # fill="x" faz ele ocupar o espaço horizontal
    # padx e pady criam espaçamento
    tarefa_frame.pack(
        fill="x",
        padx=15,
        pady=5
    )

    # Verifica se a tarefa está concluída
    if tarefa["concluida"]:

        # Símbolo que aparece quando a tarefa é concluída
        simbolo = "✓"

        # Cor verde para o símbolo
        cor_botao = "green"

        # Texto cinza para indicar que foi concluída
        cor_texto = "gray"

    else:

        # Círculo que aparece enquanto a tarefa está pendente
        simbolo = "○"

        # Cor do círculo
        cor_botao = "gray"

        # Cor do texto da tarefa pendente
        cor_texto = "black"

    # Monta o texto que aparecerá na tarefa
    # \n quebra a linha
    texto = (
        f'{tarefa["nome"]}\n'
        f'📅 {tarefa["data"]}   ⏰ {tarefa["hora"]}'
    )

    # Cria o texto da tarefa
    texto_label = tk.Label(
        tarefa_frame,
        text=texto,
        font=("Arial", 11),
        fg=cor_texto,
        justify="left"
    )

    # Coloca o texto no lado esquerdo
    texto_label.pack(
        side="left",
        fill="x",
        expand=True
    )

    # Cria o botão do círculo de conclusão
    botao_concluir = tk.Button(
        tarefa_frame,
        text=simbolo,
        font=("Arial", 18, "bold"),
        fg=cor_botao,
        bd=0,

        # Quando clicar, chama a função que conclui a tarefa
        # lambda permite enviar a tarefa específica clicada
        command=lambda: concluir_tarefa(tarefa)
    )

    # Coloca o botão no lado direito
    botao_concluir.pack(side="right")


# Função para concluir uma tarefa

# Altera o estado da tarefa entre pendente e concluída
def concluir_tarefa(tarefa):

    # False = pendente
    # True = concluída
    # not inverte o valor:
    # False vira True
    # True vira False
    tarefa["concluida"] = not tarefa["concluida"]

    # Atualiza a tela
    atualizar_lista()


# Função para abrir a tela de nova tarefa

# Será executada quando o usuário clicar no "+"
def abrir_adicionar():

    # Toplevel cria uma segunda janela ligada à principal
    janela_adicionar = tk.Toplevel(janela)

    # Define o título da segunda janela
    janela_adicionar.title("Nova tarefa")

    # Define o tamanho da segunda janela
    janela_adicionar.geometry("350x400")

    # Impede que a segunda janela seja redimensionada
    janela_adicionar.resizable(False, False)


    # Título da segunda janela

    titulo = tk.Label(
        janela_adicionar,
        text="Nova tarefa",
        font=("Arial", 20, "bold")
    )

    titulo.pack(pady=20)


    # Campo para o nome da tarefa

    nome_label = tk.Label(
        janela_adicionar,
        text="Tarefa:",
        font=("Arial", 11)
    )

    nome_label.pack(
        anchor="w",
        padx=30
    )

    # Entry é uma caixa onde o usuário pode digitar
    nome_entry = tk.Entry(
        janela_adicionar,
        font=("Arial", 12)
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
        font=("Arial", 11)
    )

    data_label.pack(
        anchor="w",
        padx=30,
        pady=(15, 0)
    )

    data_entry = tk.Entry(
        janela_adicionar,
        font=("Arial", 12)
    )

    data_entry.pack(
        fill="x",
        padx=30,
        pady=5
    )

    # Coloca automaticamente a data atual no campo
    data_entry.insert(
        0,
        datetime.now().strftime("%d/%m/%Y")
    )


    # Campo para o horário

    hora_label = tk.Label(
        janela_adicionar,
        text="Horário:",
        font=("Arial", 11)
    )

    hora_label.pack(
        anchor="w",
        padx=30,
        pady=(15, 0)
    )

    hora_entry = tk.Entry(
        janela_adicionar,
        font=("Arial", 12)
    )

    hora_entry.pack(
        fill="x",
        padx=30,
        pady=5
    )

    # Coloca automaticamente o horário atual no campo
    hora_entry.insert(
        0,
        datetime.now().strftime("%H:%M")
    )


    # Função para adicionar a tarefa

    # Pega as informações digitadas e cria uma nova tarefa
    def adicionar():

        # .get() pega o que foi digitado
        # .strip() remove espaços desnecessários
        nome = nome_entry.get().strip()
        data = data_entry.get().strip()
        hora = hora_entry.get().strip()

        # Se o nome estiver vazio, não adiciona
        if nome == "":
            return

        # Cria um dicionário com as informações da tarefa
        # Uma nova tarefa começa como pendente
        nova_tarefa = {
            "nome": nome,
            "data": data,
            "hora": hora,
            "concluida": False
        }

        # Adiciona a tarefa à lista
        tarefas.append(nova_tarefa)

        # Atualiza a tela principal
        atualizar_lista()

        # Fecha a janela de adicionar tarefa
        janela_adicionar.destroy()


    # Botão para adicionar a tarefa

    botao_adicionar = tk.Button(
        janela_adicionar,
        text="Adicionar tarefa",
        font=("Arial", 11, "bold"),
        command=adicionar
    )

    botao_adicionar.pack(pady=25)


# Título da tela principal

titulo = tk.Label(
    janela,
    text="TaskFlow",
    font=("Arial", 25, "bold")
)

titulo.pack(
    pady=(25, 20)
)


# Cabeçalho

# Frame usado para colocar o filtro e o botão "+"
# na mesma linha
cabecalho = tk.Frame(janela)

cabecalho.pack(
    fill="x",
    padx=20
)


# Guarda a opção escolhida no filtro
filtro_var = tk.StringVar()

# Define a opção que aparece inicialmente
filtro_var.set("Tarefas pendentes")


# Filtro de tarefas

# Combobox é a caixa com uma seta que permite escolher
# entre diferentes opções
filtro = ttk.Combobox(
    cabecalho,
    textvariable=filtro_var,

    # Opções disponíveis no filtro
    values=[
        "Tarefas pendentes",
        "Tarefas concluídas",
        "Todas as tarefas"
    ],

    # Permite apenas escolher uma opção da lista
    state="readonly",

    # Define a largura da caixa
    width=23
)

# Coloca o filtro no lado esquerdo
filtro.pack(side="left")


# Quando o usuário escolher uma opção do filtro,
# atualiza a lista de tarefas
filtro.bind(
    "<<ComboboxSelected>>",
    lambda evento: atualizar_lista()
)


# Botão "+"

# Abre a tela para criar uma nova tarefa
botao_mais = tk.Button(
    cabecalho,
    text="+",
    font=("Arial", 20, "bold"),
    bd=0,
    command=abrir_adicionar
)

# Coloca o botão "+" no lado direito
botao_mais.pack(side="right")


# Área onde as tarefas aparecem

# Frame que vai guardar as tarefas criadas
lista_frame = tk.Frame(janela)

lista_frame.pack(
    fill="both",
    expand=True,
    pady=20
)


# Inicialização

# Mostra a lista inicial
# Como ainda não existem tarefas,
# aparecerá "Nenhuma tarefa encontrada."
atualizar_lista()

# Mantém o aplicativo aberto
janela.mainloop()