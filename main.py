from classes import *


def menu_principal():
    while True:
        print("\n" * 20)
        escolha = input(
            """
=========================================
    MENU - Gerenciamento Geral
=========================================
    1- Menu de Usuários
    2- Menu de Tarefas
    3- Menu de Projetos
    0- Sair
    Escolha: """
        ).lower()
        if escolha == "0":
            break
        elif escolha == "1":
            menu_usuarios()
        elif escolha == "2":
            menu_tarefas()
        elif escolha == "3":
            menu_projetos()


class_menu = """
=========================================
    MENU - Gerenciamento de Usuários
=========================================
    1- Criar novo usuário
    2- Mostrar Tarefas dos usuários
    3- Seleciona usuário
    0- Voltar
    """


def menu_usuarios():
    while True:
        if Usuario.lista_usuarios != []:
            print(f"Lista dos usuarios")
            for index, usuario in enumerate(Usuario.lista_usuarios, start=1):
                print(f"{index}. {usuario.get_nome()} ({usuario.get_email()})")
        print(class_menu)
        escolha = input("Escolha: ")
        if escolha == "0":
            break
        elif escolha == "1":
            try:
                nome = input("Digite o nome do novo usuário: ")
                email = input("Digite o email do novo usuário: ")
                novo_usuario = Usuario(nome, email)
                print(f"Novo usuário '{novo_usuario.get_nome()}' criado!")
            except ValueError as e:
                print(f"Erro ao criar usuário: {e}")
        elif escolha == "2":
            mostrar_tarefas_do_usuario()
            # usuario_choice = int(input("Escolha o número do usuário: ")) - 1
            # if 0 <= usuario_choice < len(Usuario.lista_usuarios):
            #     usuario_selecionado = Usuario.lista_usuarios[usuario_choice]
            #     for tarefa in usuario_selecionado.get_lista_tarefas():
            #         print(f"- {tarefa.get_titulo()} ({tarefa.get_status()})")
            # else:
            #     print("Escolha inválida. Tente novamente.")
        elif escolha == "3":
            # need to select user to add/delete tasks
            while True:
                print("\nSub-menu - Ações do Usuário:")
                print("1. Criar nova tarefa")
                print("2. Marcar tarefa como concluída")
                print("0. Voltar")

                escolha_sub_menu = input("Escolha: ")
                if escolha_sub_menu == "0":
                    break
                elif escolha_sub_menu == "1":
                    titulo_tarefa = input("Digite o título da nova tarefa: ")
                    descricao_tarefa = input("Digite a descrição da nova tarefa: ")
                    novo_tarefa = usuario_selecionado.criar_tarefa(
                        titulo_tarefa, descricao_tarefa
                    )
                    print("Nova tarefa criada!")
                elif escolha_sub_menu == "2":
                    Usuario.marcar_concluida(novo_tarefa)
                    pass
                else:
                    print("Escolha inválida. Tente novamente.")
            else:
                print("Escolha inválida. Tente novamente.")


task_menu = """
=========================================
    MENU - Gerenciamento de Tarefas
=========================================
    1- Criar nova tarefa
    2- Listar tarefas
    0- Voltar
    """
# edit tasks


def menu_tarefas():
    while True:
        print(task_menu)
        escolha = input("Escolha: ")
        if escolha == "0":
            break
        elif escolha == "1":
            try:
                titulo = input("Digite o título da nova tarefa: ")
                descricao = input(
                    "Digite a descrição da nova tarefa (press Enter if none): "
                )
                nova_tarefa = Tarefa(titulo, descricao)
                nova_tarefa.alterar_status()
                print(f"Nova tarefa '{nova_tarefa.get_titulo()}' criada!")
            except ValueError as e:
                print(f"Erro ao criar tarefa: {e}")
        elif escolha == "2":
            print("\nLista de Tarefas:")
            for tarefa in Tarefa.lista_tarefas:
                print(f"- {tarefa.get_titulo()} ({tarefa.get_status()})")


project_menu = """
=========================================
    MENU - Gerenciamento de Projetos
=========================================
    1- Criar novo projeto
    2- Listar projetos
    0- Voltar
    """
# add tasks, get status of project


def menu_projetos():
    while True:
        print(project_menu)
        escolha = input("Escolha: ")
        if escolha == "0":
            break
        elif escolha == "1":
            try:
                nome = input("Digite o nome do novo projeto: ")
                descricao = input(
                    "Digite a descrição do novo projeto (press Enter if none): "
                )
                novo_projeto = Projeto(nome, descricao)
                print(f"Novo projeto '{novo_projeto.get_nome()}' criado!")
            except ValueError as e:
                print(f"Erro ao criar projeto: {e}")
        elif escolha == "2":
            print("\nLista de Projetos:")
            for projeto in Projeto.lista_projetos:
                print(f"- {projeto.get_nome()} ({projeto.get_descricao()})")


def mostrar_tarefas_do_usuario():
    if not Usuario.lista_usuarios:
        print("Nenhum usuário disponível.")
        return

    print("\nMostrando Tarefas dos Usuários:")
    for idx, usuario in enumerate(Usuario.lista_usuarios, start=1):
        print(f"{idx}. {usuario.get_nome()} ({usuario.get_email()})")

    while True:
        try:
            usuario_choice = int(input("Escolha o número do usuário: ")) - 1

            if 0 <= usuario_choice < len(Usuario.lista_usuarios):
                usuario_selecionado = Usuario.lista_usuarios[usuario_choice]
                for tarefa in usuario_selecionado.get_lista_tarefas():
                    print(f"- {tarefa.get_titulo()} ({tarefa.get_status()})")
                break
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


if __name__ == "__main__":
    menu_principal()
