from classes import *

gerencia_geral = """
=========================================
    MENU - Gerenciamento Geral
=========================================
    1- Menu de usuários
    2- Menu de tarefas
    3- Menu de projetos
    0- Sair
"""


def menu_principal():
    usuario_BD = UsuarioBD()
    tarefa_BD = TarefaBD()
    projeto_BD = ProjetoBD()

    while True:
        print(f"{gerencia_geral}")

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
            tarefa_BD.close()
            projeto_BD.close()
            break
        else:
            # Opção inválida.
            print("Opção inválida. Tente de novo.")


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


def menu_usuarios(usuario_BD):
    while True:
        print(f"{gerencia_users}")

        escolha = input("Escolha um número: ")

        if escolha == "1":
            nomeUsuario = input("Nome do usuário: ")
            email = input("Email do usuário: ")
            usuario_BD.create_usuario(nomeUsuario, email)
            print("Usuário adicionado!")

        elif escolha == "2":
            resultados = usuario_BD.mostrar_usuarios()
            for usuario in resultados:
                print(
                    f"ID: {usuario[0]}, Nome dos usuários: {usuario[1]}, Email: {usuario[2]}"
                )

        elif escolha == "3":
            idUsuarios = input("ID do usuário que voce quer atualizar: ")
            novo_nome = input("Digite o nove nome: ")
            novo_email = input("Digite o novo email: ")

            if usuario_BD.update_usuario(idUsuarios, novo_email, novo_nome) > 0:
                print("Usuário atualizado!")
            else:
                print("Usuário não encontrado.")

        elif escolha == "4":
            idUsuarios = (input("Digite o nome do usuário que voce quer excluir: "))
            if usuario_BD.delete_usuario(idUsuarios) > 0:
                print("Usuário excluído!")
            else:
                print("Usuário não encontrado.")

        elif escolha == "0":
            break

        else:
            print("Opção inválida. Tente de novo.")


gerencia_tarefas = """
=========================================
    MENU - Gerenciamento de Tarefas
=========================================
    1- Criar tarefas
    2- Listar tarefas
    3- Atualizar descrição das tarefas
    4- Deletar tarefas
    5- Atualizar status das tarefas
    6- Atribuir tarefa ao usuário
    7- Remover tarefa ao usuário
    0- Voltar ao menu principal
"""


def menu_tarefas(tarefa_BD):
    while True:
        print(f"{gerencia_tarefas}")

        escolha = input("Escolha um número: ")

        if escolha == "1":
            titulo = input("Digite o título da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")
            status = input("Status da tarefa (A-Ativa, C-Completa): ")
            nomeProjeto = input("Digite o nome do projeto a que pertence a tarefa: ")
            try:
                tarefa_BD.create_tarefa(titulo, descricao, status, nomeProjeto)
                print("Tarefa adicionada!")
            except ValueError as e:
                print(str(e))

        elif escolha == "2":
            resultados = tarefa_BD.mostrar_tarefas()
            for tarefa in resultados:
                print(
                    f"Titulo: {tarefa[1]}, Descrição: {tarefa[2]}, Status: {tarefa[3]}, Data Criação: {tarefa[4]}, Data Conclusão: {tarefa[5]}, ID Projeto: {tarefa[6]}"
                )

        elif escolha == "3":
            titulo = input("Título da tarefa que voce quer atualizar: ")
            nova_descricao = input("Digite uma nova descrição: ")
            if tarefa_BD.update_tarefa(titulo, nova_descricao) > 0:
                print("Descrição atualizada!")
            else:
                print("Tarefa não encontrada.")

        elif escolha == "4":
            titulo = input("Título da tarefa que voce quer excluir: ")
            if tarefa_BD.delete_tarefa(titulo) > 0:
                print("Tarefa excluída!")
            else:
                print("Tarefa não encontrada.")

        elif escolha == "5":
            titulo = input("Título da tarefa que voce quer atualizar o status: ")
            novo_status = input("Digite um novo status: ")
            if tarefa_BD.alterar_status_tarefa(titulo, novo_status) > 0:
                print("Status atualizado!")
            else:
                print("Tarefa não encontrada.")

        elif escolha == "6":
            idTarefas = input(
                "Digite o ID da tarefa que voce quer atribuir a usuários: "
            )
            idUsuario = [
                int(idUsuario)
                for idUsuario in input(
                    "Digite os IDs dos usuários separados por vírgula: "
                ).split(",")
            ]
            tarefa_BD.atribuir_tarefa_a_usuarios(idTarefas, idUsuario)
            print("Tarefa atribuída aos usuários!")

        elif escolha == "7":
            idTarefas = input("Digite o ID da tarefa: ")
            idUsuario = int(input("ID do usuário para remover a atribuição: "))
            if tarefa_BD.remover_atribuicao_usuario_tarefa(idTarefas, idUsuario) > 0:
                print("Atribuição removida!")
            else:
                print("Atribuição não encontrada.")

        elif escolha == "0":
            break

        else:
            print("Opção inválida. Tente de novo.")


gerencia_projeto = """
=========================================
    MENU - Gerenciamento de Projetos
=========================================
    1- Criar projeto
    2- Listar projeto
    3- Atualizar descrição do projeto
    4- Excluir projeto
    5- Atualizar status do projeto
    0- Voltar ao menu projeto
"""


def menu_projetos(projeto_BD):
    while True:
        print(f"{gerencia_projeto}")
        escolha = input("Escolha um número: ")

        if escolha == "1":
            nomeProjeto = input("Titulo do projeto: ")
            descricao = input("Descrição do projeto: ")
            statusProjeto = input("Status do projeto: ")
            projeto_BD.create_projeto(nomeProjeto, descricao, statusProjeto)
            print("Projeto adicionado!")

        elif escolha == "2":
            resultados = projeto_BD.mostrar_projetos()
            for projeto in resultados:
                print(
                    f"Titulo: {projeto[1]} descricao: {projeto[2]} status: {projeto[3]}"
                )

        elif escolha == "3":
            nomeProjeto = input("Titulo do projeto que voce quer atualizar: ")
            nova_descricao = input("Digite uma nova descrição: ")
            if projeto_BD.update_projeto(nomeProjeto, nova_descricao) > 0:
                print("Descrição atualizada!")
            else:
                print("Projeto não encontrado.")

        elif escolha == "4":
            nomeProjeto = input("Titulo do projeto que voce quer excluir: ")
            if projeto_BD.delete_projeto(nomeProjeto) > 0:
                print("Projeto excluído!")
            else:
                print("Projeto não encontrado.")

        elif escolha == "5":
            nomeProjeto = input("Titulo do projeto que voce quer atualizar o status: ")
            novo_status = input("Digite um novo status: ")
            if projeto_BD.alterar_status_projeto(nomeProjeto, novo_status) > 0:
                print("Status atualizado!")
            else:
                print("Projeto não encontrado.")

        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente de novo.")


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
