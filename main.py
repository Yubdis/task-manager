from classes import *

gerencia_geral = """
=========================================
    MENU - Gerenciamento Geral
=========================================
    1- Menu de Usuários
    2- Menu de Tarefas
    3- Menu de Projetos
    0- Sair
"""

gerencia_users = """
=========================================
    MENU - Gerenciamento de Usuários
=========================================
    1- Inserir usuário
    2- Listar usuários
    3- Atualizar usuários
    4- Excluir usuários
    0- Voltar
"""

gerencia_tarefas = """
=========================================
    MENU - Gerenciamento de Tarefas
=========================================
    1- Criar Tarefas
    2- Listar Tarefas
    3- Atualizar descrição das Tarefas
    4- Deletar Tarefas
    5- Atualizar status das Tarefas
    6- Atribuir tarefa ao usuário
    7- Remover tarefa ao usuário
    0- Voltar ao Menu Principal
"""

gerencia_projeto = """
=========================================
    MENU - Gerenciamento de Projetos
=========================================
    1- Criar Projeto
    2- Listar Projeto
    3- Atualizar descrição do Projeto
    4- Deletar Projeto
    5- Atualizar status do Projeto
    0- Voltar ao Menu Projeto
"""


def menu_principal():
    # Cria uma instância de UsuarioDB, TarefaDB e ProjetoDB.
    usuario_BD = UsuarioBD()
    tarefa_BD = TarefaBD()
    projeto_BD = ProjetoBD()

    while True:
        print(f"{gerencia_geral}")

        # Solicita a escolha do usuário.
        escolha = input("Escolha um número: ")

        if escolha == "1":
            # Chama o Menu de Usuários.
            menu_usuarios(usuario_BD)
        elif escolha == "2":
            # Chama o Menu de Tarefas.
            menu_tarefas(tarefa_BD)
        elif escolha == "3":
            # Chama o Menu de Projetos.
            menu_projetos(projeto_BD)
        elif escolha == "0":
            # Fecha as conexões e encerra o programa.
            usuario_BD.close()
            projeto_BD.close()
            tarefa_BD.close()
            break
        else:
            # Opção inválida.
            print("Opção inválida. Tente novamente.")


def menu_usuarios(usuario_BD):
    while True:
        print(f"{gerencia_users}")

        # Solicita a escolha do usuário.
        escolha = input("Escolha um número: ")

        if escolha == "1":
            # Opção para inserir um novo usuário.
            nomeUsuario = input("Nome do usuário: ")
            email = input("Email do usuário: ")
            usuario_BD.create_usuario(nomeUsuario, email)
            print("Usuário adicionado com sucesso!")
        elif escolha == "2":
            # Opção para listar todos os usuários.
            resultados = usuario_BD.read_usuarios()
            for usuario in resultados:
                print(
                    f"ID: {usuario[0]}, Nome do Usuários: {usuario[1]}, Email: {usuario[2]}"
                )
        elif escolha == "3":
            # Opção para atualizar um usuário existente.
            idUsuarios = input("ID do usuário que deseja atualizar: ")
            novo_email = input("Insira o novo email: ")
            if usuario_BD.update_usuario(idUsuarios, novo_email) > 0:
                print("Usuário atualizado com sucesso!")
            else:
                print("Usuário não encontrado.")
        elif escolha == "4":
            # Opção para excluir um usuário.
            idUsuarios = input("idUser do usuário que deseja excluir: ")
            if usuario_BD.delete_usuario(idUsuarios) > 0:
                print("Usuário excluído com sucesso!")
            else:
                print("Usuário não encontrado.")
        elif escolha == "0":
            # Retorna ao Menu Principal.
            break
        else:
            # Opção inválida.
            print("Opção inválida. Tente novamente.")


def menu_tarefas(tarefa_BD):
    while True:
        print(f"{gerencia_tarefas}")

        # Solicita a escolha do usuário.
        escolha = input("Escolha um número: ")

        if escolha == "1":
            # Opção para inserir uma nova tarefa.
            titulo = input("Digite o título da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")
            status = input("Status da tarefa (A-Ativa, C-Completa): ")
            nomeProjeto = input("Digite qual projeto ela pertence: ")
            try:
                tarefa_BD.create_tarefa(titulo, descricao, status, nomeProjeto)
                print("Tarefa adicionada com sucesso!")
            except ValueError as e:
                print(str(e))
        elif escolha == "2":
            # Opção para listar todas as tarefas.
            resultados = tarefa_BD.read_tarefas()
            for tarefa in resultados:
                print(
                    f"Titulo: {tarefa[1]}, Descrição: {tarefa[2]}, Status: {tarefa[3]}, Data Criação: {tarefa[4]}, Data Conclusão: {tarefa[5]}, ID Projeto: {tarefa[6]}"
                )
        elif escolha == "3":
            # Opção para atualizar a descrição de uma tarefa.
            titulo = input("Título da tarefa que deseja atualizar: ")
            nova_descricao = input("Nova descrição: ")
            if tarefa_BD.update_tarefa(titulo, nova_descricao) > 0:
                print("Descrição atualizada com sucesso!")
            else:
                print("Tarefa não encontrada.")
        elif escolha == "4":
            # Opção para excluir uma tarefa.
            titulo = input("Título da tarefa que deseja excluir: ")
            if tarefa_BD.delete_tarefa(titulo) > 0:
                print("Tarefa excluída com sucesso!")
            else:
                print("Tarefa não encontrada.")
        elif escolha == "5":
            # Opção para atualizar o status de uma tarefa.
            titulo = input("Título da tarefa que deseja atualizar o status: ")
            novo_status = input("Novo status: ")
            if tarefa_BD.alterar_status_tarefa(titulo, novo_status) > 0:
                print("Status atualizado com sucesso!")
            else:
                print("Tarefa não encontrada.")
        elif escolha == "6":
            # Opção para atribuir tarefa a usuários.
            idTarefas = input("Título da tarefa que deseja atribuir a usuários: ")
            idUsuario = [
                int(idUsuario)
                for idUsuario in input(
                    "Digite os IDs dos usuários separados por vírgula: "
                ).split(",")
            ]
            tarefa_BD.atribuir_tarefa_a_usuarios(idTarefas, idUsuario)
            print("Tarefa atribuída aos usuários com sucesso!")
        elif escolha == "7":
            # Opção para remover a atribuição de tarefa a usuário.
            idTarefas = input("Título da tarefa: ")
            idUsuario = int(input("ID do usuário para remover a atribuição: "))
            if tarefa_BD.remover_atribuicao_tarefa_usuario(idTarefas, idUsuario) > 0:
                print("Atribuição removida com sucesso!")
            else:
                print("Atribuição não encontrada.")
        elif escolha == "0":
            # Retorna ao Menu Principal.
            break
        else:
            # Opção inválida.
            print("Opção inválida. Tente novamente.")


# Parâmetros são os "espaços reservados" na definição da função.
# Argumentos são os valores reais que você fornece quando chama a função.


def menu_projetos(projeto_BD):
    while True:
        # Exibe as opções do Menu de Projetos.
        print("\nMenu de Projeto:")
        print(f"{gerencia_projeto}")

        # Solicita a escolha do usuário.
        escolha = input("Escolha um número: ")

        if escolha == "1":
            # Opção para inserir um novo projeto.
            nomeProjeto = input("Titulo do Projeto: ")
            descricao = input("Descrição do Projeto: ")
            statusProjeto = input("Status do Projeto: ")
            projeto_BD.create_projeto(nomeProjeto, descricao, statusProjeto)
            print("Projeto adicionado com sucesso!")
        elif escolha == "2":
            # Opção para listar todos os projetos.
            resultados = projeto_BD.read_projetos()
            for projeto in resultados:
                print(
                    f"Titulo: {projeto[1]}, descricao: {projeto[2]}, status: {projeto[3]}"
                )
        elif escolha == "3":
            # Opção para atualizar a descrição de um projeto existente.
            nomeProjeto = input("Titulo do projeto que deseja atualizar: ")
            nova_descricao = input("Nova descrição: ")
            if projeto_BD.update_projeto(nomeProjeto, nova_descricao) > 0:
                print("Descrição atualizada com sucesso!")
            else:
                print("Projeto não encontrado.")
        elif escolha == "4":
            # Opção para excluir um projeto.
            nomeProjeto = input("Titulo do projeto que deseja excluir: ")
            if projeto_BD.delete_projeto(nomeProjeto) > 0:
                print("Projeto excluído com sucesso!")
            else:
                print("Projeto não encontrado.")
        elif escolha == "5":
            # Opção para atualizar o status de um projeto.
            nomeProjeto = input("Titulo do projeto que deseja atualizar o status: ")
            novo_status = input("Novo status: ")
            if projeto_BD.alterar_status_projeto(nomeProjeto, novo_status) > 0:
                print("Status atualizado com sucesso!")
            else:
                print("Projeto não encontrado.")
        elif escolha == "0":
            # Volta ao Menu Principal.
            break
        else:
            # Opção inválida.
            print("Opção inválida. Tente novamente.")


# O código dentro deste bloco será executado somente se o script Python for executado como o programa principal, em vez de ser importado como um módulo em outro script.
if __name__ == "__main__":
    menu_principal()


# def menu_principal():
#     while True:
#         print("\n" * 20)
#         escolha = input(
#             """
# =========================================
#     MENU - Gerenciamento Geral
# =========================================
#     1- Menu de Usuários
#     2- Menu de Tarefas
#     3- Menu de Projetos
#     0- Sair
#     Escolha: """
#         ).lower()
#         if escolha == "0":
#             break
#         elif escolha == "1":
#             menu_usuarios()
#         elif escolha == "2":
#             menu_tarefas()
#         elif escolha == "3":
#             menu_projetos()


# def menu_usuarios():
#     while True:
#         print(class_menu)
#         escolha = input("Escolha: ")
#         if escolha == "0":
#             break
#         elif escolha == "1":
#             # criar novo usuario
#             novo_nome = input("Digite o nome do novo usuário: ")
#             novo_email = input("Digite o email do novo usuário: ")
#             try:
#                 Usuario.criar_usuario(novo_nome, novo_email)
#                 Usuario.add_lista_usuarios()

#             except ValueError as e:
#                 print(f"Erro ao criar usuário: {e}")
#         elif escolha == "2":
#             # deletar usuario
#             try:
#                 usuario = input("Quem vocé quer deletar? ")
#                 if usuario in Usuario.get_lista_usuarios():
#                     Usuario.del_usuario(usuario)
#                 else:
#                     print("Digite usuario na sistema")
#             except:
#                 print("Erro, não consiga deletar usuário")
#         elif escolha == "3":
#             # mostrar lista usuários
#             print(lista_usuarios)

#         elif escolha == "4":
#             # seleciona usuario
#             select_usuario()
#             # need to ask Carey what to do to select a user and make sub menu


# def menu_tarefas():
#     while True:
#         # seleciona usuario
#         Usuario.select_usuario()
#         # need to ask Carey what to do to select a user and make sub menu
#         print(task_menu)
#         escolha = input("Escolha: ")
#         if escolha == "0":
#             break
#         elif escolha == "1":
#             Usuario.criar_tarefa()
#         elif escolha == "2":
#             tarefa = input("Escolha Tarefa para deletar: ")
#             if tarefa in Usuario.get_lista_tarefas():
#                 Usuario.remove_tarefa(tarefa)
#             else:
#                 print("Erro. Não consigo deletar tarefa.")
#         elif escolha == "3":
#             print(Usuario.get_lista_tarefas())

# elif escolha == "4":
#     # atualizar descrição
#     novo_desc = input("Digite nove descrição: ")
#     Tarefa.atualizar_descricao(novo_desc)

# elif escolha == "3":
#     # need to select user to add/delete tasks
#
#     while True:
#         print("\nSub-menu - Ações do Usuário:")
#         print("1. Criar nova tarefa")
#         print("2. Marcar tarefa como concluída")
#         print("0. Voltar")
#
#         escolha_sub_menu = input("Escolha: ")
#         if escolha_sub_menu == "0":
#             break
#         elif escolha_sub_menu == "1":
#             titulo_tarefa = input("Digite o título da nova tarefa: ")
#             descricao_tarefa = input("Digite a descrição da nova tarefa: ")
#             novo_tarefa = usuario_selecionado.criar_tarefa(
#                 titulo_tarefa, descricao_tarefa
#             )
#             print("Nova tarefa criada!")
#         elif escolha_sub_menu == "2":
#             Usuario.marcar_concluida(novo_tarefa)
#             pass
#         else:
#             print("Escolha inválida. Tente novamente.")


# def menu_projetos():
#     while True:
#         print(project_menu)
#         escolha = input("Escolha: ")
#         if escolha == "0":
#             break
#         elif escolha == "1":
#             try:
#                 novo_projeto = Projeto.criar_projeto()
#                 print(f"Novo projeto '{novo_projeto.get_nome()}' criado!")
#             except ValueError as e:
#                 print(f"Erro ao criar projeto: {e}")
#         elif escolha == "2":
#             print("\nLista de Projetos:")
#             for projeto in Projeto._lista_projetos:
#                 print(f"- {projeto.get_nome()} ({projeto.get_descricao()})")


# def mostrar_tarefas_do_usuario():
#     if not Usuario.get_lista_usuarios():
#         print("Nenhum usuário disponível.")
#         return

#     print("\nMostrando Tarefas dos Usuários:")
#     for idx, usuario in enumerate(Usuario._lista_usuarios, start=1):
#         print(f"{idx}. {usuario.get_nome()} ({usuario.get_email()})")

#     while True:
#         try:
#             usuario_choice = int(input("Escolha o número do usuário: ")) - 1

#             if 0 <= usuario_choice < len(Usuario._lista_usuarios):
#                 usuario_selecionado = Usuario._lista_usuarios[usuario_choice]
#                 for tarefa in usuario_selecionado.get_lista_tarefas():
#                     print(f"- {tarefa.get_titulo()} ({tarefa.get_status()})")
#                 break
#             else:
#                 print("Escolha inválida. Tente novamente.")
#         except ValueError:
#             print("Entrada inválida. Digite um número válido.")


# if __name__ == "__main__":
#     menu_principal()
