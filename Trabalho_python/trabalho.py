#Gabriel Kesley da Silva Cesário

tarefas = []
estados = []

def adicionar_tarefa(nome):
    tarefas.append(nome)
    estados.append("pendente")
    print(f"Tarefa '{nome}' adicionada!")

def marcar_concluida(nome):
    if nome in tarefas:
        estados[tarefas.index(nome)] = "concluída"
        print(f"Tarefa '{nome}' concluída!")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

def remover_tarefa(nome):
    if nome in tarefas:
        idx = tarefas.index(nome)
        tarefas.pop(idx)
        estados.pop(idx)
        print(f"Tarefa '{nome}' removida!")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

def listar_tarefas():
    print("\nTarefas:")
    for nome, estado in zip(tarefas, estados):
        print(f"- {nome} ({estado})")

def pesquisar_tarefa(nome):
    if nome in tarefas:
        print(f"Tarefa encontrada: {nome} ({estados[tarefas.index(nome)]})")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

while True:
    print("\n1. Adicionar | 2. Concluir | 3. Remover | 4. Listar | 5. Pesquisar | 6. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa(input("Nome da tarefa: "))
    elif opcao == "2":
        marcar_concluida(input("Tarefa concluída: "))
    elif opcao == "3":
        remover_tarefa(input("Tarefa a remover: "))
    elif opcao == "4":
        listar_tarefas()
    elif opcao == "5":
        pesquisar_tarefa(input("Tarefa a pesquisar: "))
    elif opcao == "6":
        print("Saindo. Até mais!")
        break
    else:
        print("Opção inválida.")
