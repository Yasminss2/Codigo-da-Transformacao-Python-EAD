import sqlite3

def conectar_bd():
    """Cria a conexão com o banco de dados e a tabela de tarefas se não existir."""
    conexao = sqlite3.connect("gerenciador_tarefas.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            status TEXT DEFAULT 'Pendente'
        )
    """)
    conexao.commit()
    return conexao

def adicionar_tarefa(conexao):
    """Adiciona uma nova tarefa ao banco de dados."""
    titulo = input("\nDigite o título da tarefa: ").strip()
    if titulo:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO tarefas (titulo) VALUES (?)", (titulo,))
        conexao.commit()
        print(f"✅ Tarefa '{titulo}' adicionada com sucesso!")
    else:
        print("❌ O título da tarefa não pode estar vazio.")

def visualizar_tarefas(conexao):
    """Exibe todas as tarefas cadastradas."""
    cursor = conexao.cursor()
    cursor.execute("SELECT id, titulo, status FROM tarefas")
    tarefas = cursor.fetchall()

    print("\n" + "=" * 40)
    print("📋 LISTA DE TAREFAS")
    print("=" * 40)
    
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for id_tarefa, titulo, status in tarefas:
            print(f"[{id_tarefa}] {titulo} - Status: {status}")
            
    print("=" * 40)

def excluir_tarefa(conexao):
    """Exclui uma tarefa com base no seu ID."""
    visualizar_tarefas(conexao)
    try:
        id_tarefa = int(input("\nDigite o ID da tarefa que deseja excluir: "))
        cursor = conexao.cursor()
        
        # Verifica se o ID existe
        cursor.execute("SELECT * FROM tarefas WHERE id = ?", (id_tarefa,))
        if cursor.fetchone():
            cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
            conexao.commit()
            print(f"🗑️ Tarefa com ID {id_tarefa} excluída com sucesso!")
        else:
            print("❌ Tarefa com esse ID não foi encontrada.")
    except ValueError:
        print("❌ Por favor, digite um número de ID válido.")

def menu_principal():
    """Exibe o menu interativo no terminal."""
    conexao = conectar_bd()

    while True:
        print("\n=== GERENCIADOR DE TAREFAS (SQLITE) ===")
        print("1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Excluir tarefa")
        print("4. Sair")

        opcao = input("Escolha uma opção (1-4): ").strip()

        if opcao == "1":
            adicionar_tarefa(conexao)
        elif opcao == "2":
            visualizar_tarefas(conexao)
        elif opcao == "3":
            excluir_tarefa(conexao)
        elif opcao == "4":
            print("\nEncerrando o programa... Até logo!")
            conexao.close()
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()