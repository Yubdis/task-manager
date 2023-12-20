import mysql.connector
from datetime import datetime


class bancoDados:
    def init(self):
        self.conexao = None
        self.cursor = None

    # Cria uma conexão com o banco de dados.
    def conectar(self):
        self.conexao = mysql.connector.connect(
            host="localhost", user="root", password="", database="OOP"
        )
        self.cursor = self.conexao.cursor()

    # Fecha a conexão com o banco de dados.
    def fechar_conexao(self):
        # Verifica se o cursor está aberto e fecha o cursor.
        if self.cursor:
            self.cursor.close()
        # Verifica se a conexão está aberta e fecha a conexao.
        if self.conexao:
            self.conexao.close()


class UsuarioBD(bancoDados):
    def init(self):
        # Chama o construtor da classe pai (superclasse) para inicializar as propriedades da classe base.
        super().init()

    # Cria um novo usuário no banco de dados.
    def create_usuario(self, nome, email):
        self.conectar()
        command = f'INSERT INTO usuarios (nome, email) VALUES ("{nome}", "{email}")'
        self.cursor.execute(command)
        self.conexao.commit()
        self.fechar_conexao()

    # Retorna todos os usuários do banco de dados.
    def mostrar_usuarios(self):
        self.conectar()
        command = "SELECT * FROM usuarios"
        self.cursor.execute(command)
        resultados = self.cursor.fetchall()
        self.fechar_conexao()
        return resultados

    # Atualiza o e-mail de um usuário no banco de dados.
    def update_usuario(self, idUsuario, novo_email, novo_nome):
        self.conectar()
        command = f'UPDATE usuarios SET email = "{novo_email}", nome = "{novo_nome}" WHERE idUsuarios = "{idUsuario}"'
        self.cursor.execute(command)
        self.cursor.rowcount
        self.conexao.commit()
        resultados = self.cursor.rowcount
        self.fechar_conexao()
        return resultados

    # Exclui um usuário do banco de dados baseado no nome.
    def delete_usuario(self, nome):
        self.conectar()
        command = f'DELETE FROM usuarios WHERE nome = "{nome}"'
        self.cursor.execute(command)
        self.conexao.commit()
        resultados = self.cursor.rowcount
        self.fechar_conexao()
        return resultados

    # Relaciona usuários a tarefas no banco de dados.
    def relacionar_usuarios_tarefas(self, idUsuarios, idTarefas):
        self.conectar()
        command = f"INSERT INTO usuariostarefas (idTarefas, idUsuarios) VALUES ({idTarefas}, {idUsuarios})"
        self.cursor.execute(command)
        self.conexao.commit()
        self.fechar_conexao()

    # Busca um usuário no banco de dados baseado no ID.
    def buscar_usuario_por_id(self, idUsuario):
        self.conectar()
        command = f'SELECT * FROM usuarios WHERE idUsuarios = "{idUsuario}"'
        self.cursor.execute(command)
        cliente = self.cursor.fetchone()
        self.fechar_conexao()
        return cliente


class TarefaBD(bancoDados):
    def __init__(self):
        # Chama o construtor da classe pai (superclasse) para inicializar as propriedades da classe base.
        super().__init__()

    # Cria uma nova tarefa no banco de dados.
    def create_tarefa(self, titulo, descricao, status, nomeProjeto):
        self.conectar()
        # Atribui data e hora para criação da tarefa.
        dataCriacao = datetime.now()
        status = status.upper()
        # Verifica se o projeto existe e atribui o ID do projeto.
        idProjeto = self.verificar_projeto_existente(nomeProjeto)
        if idProjeto is None:
            raise ValueError(f"Projeto '{nomeProjeto}' não encontrado.")

        command = f'INSERT INTO tarefas (titulo, descricao, status, data_criacao, codProjeto) VALUES ("{titulo}","{descricao}" ,"{status}","{dataCriacao}" ,"{idProjeto}")'
        self.cursor.execute(command)
        self.conexao.commit()
        self.fechar_conexao()

    # Retorna todas as tarefas do banco de dados.
    def mostrar_tarefas(self):
        self.conectar()
        command = f"SELECT * FROM tarefas"
        self.cursor.execute(command)
        resultados = self.cursor.fetchall()
        self.fechar_conexao()
        return resultados

    # Atualiza a descrição de uma tarefa no banco de dados.
    def update_tarefa(self, titulo, nova_descricao):
        self.conectar()
        command = f'UPDATE tarefas SET descricao = "{nova_descricao}" WHERE titulo = "{titulo}"'
        self.cursor.execute(command)
        self.conexao.commit()
        resultados = self.cursor.rowcount
        self.fechar_conexao()
        return resultados

    # Exclui uma tarefa do banco de dados baseado no título.
    def delete_tarefa(self, titulo):
        self.conectar()
        command = f'DELETE FROM tarefas WHERE titulo = "{titulo}"'
        self.cursor.execute(command)
        self.conexao.commit()
        resultados = self.cursor.rowcount
        self.fechar_conexao()
        return resultados

    # Altera o status de uma tarefa no banco de dados.
    def alterar_status_tarefa(self, titulo, novo_status):
        self.conectar()
        novo_status = novo_status.upper()
        if novo_status not in ["A", "C"]:
            raise ValueError("Status inválido. Deve ser A ou C.")
        command = f'UPDATE tarefas SET status = "{novo_status} "'
        # Se o novo status for "C" (Concluído), atualiza a data_conclusao.
        if novo_status == "C":
            data_conclusao = datetime.now()
            command += f', data_conclusao = "{data_conclusao} "'
        command += f' WHERE titulo = "{titulo}"'
        self.cursor.execute(command)
        self.conexao.commit()
        resultados = self.cursor.rowcount
        self.fechar_conexao()
        return resultados

    # Atribui tarefa(s) a usuário(s) no banco de dados.
    def atribuir_tarefa_a_usuarios(self, idTarefas, idUsuario):
        self.conectar()
        for idUsuario in idUsuario:
            command = f"INSERT INTO usuariostarefas (codTarefas, codUsuarios) VALUES ({idTarefas}, {idUsuario})"
            self.cursor.execute(command)
        self.conexao.commit()
        self.fechar_conexao()

    # Remove a atribuição de uma tarefa a um usuário no banco de dados.
    def remover_atribuicao_usuario_tarefa(self, idTarefas, idUsuario):
        self.conectar()
        command = f"DELETE FROM usuariostarefas WHERE codTarefas = {idTarefas} AND codUsuarios = {idUsuario}"
        self.cursor.execute(command)
        self.conexao.commit()
        resultados = self.cursor.rowcount
        self.fechar_conexao()
        return resultados

    # Verifica se um projeto existe no banco de dados e retorna o ID do projeto.
    def verificar_projeto_existente(self, nomeProjeto):
        self.conectar()
        command = f'SELECT idProjeto FROM projetos WHERE nomeProjeto = "{nomeProjeto}"'
        self.cursor.execute(command)
        resultado = self.cursor.fetchone()

        if resultado is not None:
            return resultado[0]
        else:
            return None


class ProjetoBD(bancoDados):
    def __init__(self):
        # Chama o construtor da classe pai (superclasse) para inicializar as propriedades da classe base.
        super().__init__()

    # Cria um novo projeto no banco de dados.
    def create_projeto(self, nomeProjeto, descricao, statusProjeto):
        self.conectar()
        statusProjeto = statusProjeto.upper()
        command = f'INSERT INTO projetos (nomeProjeto, descricao, statusProjeto) VALUES ("{nomeProjeto}","{descricao}" ,"{statusProjeto}")'
        self.cursor.execute(command)
        self.conexao.commit()
        self.fechar_conexao()

    # Retorna todos os projetos do banco de dados.
    def mostrar_projetos(self):
        self.conectar()
        command = f"SELECT * FROM projetos"
        self.cursor.execute(command)
        resultados = self.cursor.fetchall()
        self.fechar_conexao()
        return resultados

    # Atualiza a descrição de um projeto no banco de dados.
    def update_projeto(self, nomeProjeto, nova_descricao):
        self.conectar()
        command = f'UPDATE projetos SET descricao ="{nova_descricao}" WHERE nomeProjeto = "{nomeProjeto}"'
        self.cursor.execute(command)
        self.conexao.commit()
        resultados = self.cursor.rowcount
        self.fechar_conexao()
        return resultados

    # Exclui um projeto do banco de dados baseado no nome do projeto.
    def delete_projeto(self, nomeProjeto):
        self.conectar()
        command = f'DELETE FROM projetos WHERE nomeProjeto = "{nomeProjeto}"'
        self.cursor.execute(command)
        self.conexao.commit()
        resultados = self.cursor.rowcount
        self.fechar_conexao()
        return resultados

    # Altera o status de um projeto no banco de dados.
    def alterar_status_projeto(self, nomeProjeto, novo_status):
        self.conectar()
        novo_status = novo_status.upper()
        if novo_status not in ["A", "I", "C"]:
            raise ValueError("Status inválido. Deve ser A, I ou C.")
        command = f'UPDATE projetos SET statusProjeto = "{novo_status}" WHERE nomeProjeto = "{nomeProjeto}"'
        self.cursor.execute(command)
        self.conexao.commit()
        resultados = self.cursor.rowcount
        self.fechar_conexao()
        return resultados

    # Mostra o progresso do projeto.
    def progresso_do_projeto(self):
        self.conectar()
        unfinished_tasks = sum(
            1 for tarefa in TarefaBD.read_tarefas() if tarefa.status == "A"
        )
        total_tasks = len(TarefaBD.read_tarefas())
        progress_percentage = (
            ((total_tasks - unfinished_tasks) / total_tasks) * 100
            if total_tasks > 0
            else 0
        )
        return print(f"{progress_percentage:} %")


# class Tarefa:
#     def __init__(self, titulo, descricao):
#         self.__titulo = titulo
#         self.__descricao = descricao
#         self.__status = None
#         self.__data_criacao = None
#         self.__data_conclusao = None

#     def alterar_status(self):
#         if self.__status is None:
#             self.__status = "ativa"
#             self.__data_criacao = datetime.now()
#         elif self.__status == "ativa":
#             self.__status = "completa"
#             self.__data_conclusao = datetime.now()

#     def atualizar_descricao(self, descricao):
#         self.__descricao = descricao

#     def get_titulo(self):
#         return self.__titulo

#     def get_status(self):
#         return self.__status


# class Usuario:
#     def __init__(self, nome, email):
#         self.__nome = nome
#         self.__email = email

#     def criar_usuario(self, nome, email):
#         novo_usuario = {"nomeUsuario": nome, "email": email}
#         print(f"Novo usuário '{nome}' criado!")
#         return novo_usuario

#     def add_lista_usuarios(user):
#         lista_usuarios.append(user)
#         return len(lista_usuarios)

#     def del_usuario(self, usuario):
#         del lista_usuarios[usuario]

#     def criar_tarefa(self):
#         novo_titulo = input("Entre titulo do Tarefa: ")
#         novo_desc = input("Entre descricao do Tarefa: ")
#         lista_tarefas.append(Tarefa(novo_titulo, novo_desc))
#         return len(lista_tarefas)

#     def remove_tarefa(self, item_index):
#         del lista_tarefas[item_index]

#     def marcar_concluida(self, tarefa):
#         if tarefa in lista_tarefas:
#             tarefa.alterar_status()
#         else:
#             print("Error: Tarefa não encontrada na lista de tarefas do usuário.")

#     def get_lista_tarefas(self):
#         return lista_tarefas

#     def get_lista_usuarios(self):
#         return lista_usuarios

#     def get_user(self, user):
#         return lista_usuarios[user - 1]

#     def get_nome(self):
#         return self.__nome

#     def get_email(self):
#         return self.__email


# class Projeto:
#     def __init__(self, nome, descricao):
#         self.__nome = nome
#         self.__descricao = descricao

#     def criar_projeto(self):
#         novo_titulo = input("Entre nome do Projeto: ")
#         novo_desc = input("Entre descricao do Projeto: ")
#         lista_projetos.append(Projeto(novo_titulo, novo_desc))
#         return len(lista_projetos)

#     def adicionar_tarefa(self, tarefa, usuario):
#         if not isinstance(tarefa, Tarefa) or not isinstance(usuario, Usuario):
#             print("Error: Invalid task or user provided.")
#             return

#         if tarefa in lista_tarefas:
#             print(f"Error: Task '{tarefa.__titulo}' Ja esta no projeto.")
#             return

#         if tarefa not in usuario.lista_tarefas:
#             print(
#                 f"Error: User '{usuario.get_nome()}' nao tem permisao para adicionar tarefa."
#             )
#             return

#         lista_tarefas.append(tarefa)
#         print(f"Task '{tarefa.__titulo}' adicionar com sucesso.")


#     def get_nome(self):
#         return self.__nome

#     def get_descricao(self):
#         return self.__descricao


# # Example usage with user input:
# try:
#     new_user_name = input("Enter the name of the new user: ")
#     new_user_email = input("Enter the email of the new user: ")

#     new_user = Usuario(new_user_name, new_user_email)
#     new_user_task_title = input("Enter the title for the new task: ")
#     new_user_task_description = input(
#         "Enter the description for the new task (press Enter if none): "
#     )
#     new_user.criar_tarefa(new_user_task_title, new_user_task_description)

#     new_project_name = input("Enter the name of the new project: ")
#     new_project_description = input(
#         "Enter the description for the new project (press Enter if none): "
#     )

#     new_project = Projeto(new_project_name, new_project_description)
#     new_project.adicionar_tarefa(new_lista_tarefas[0], new_user)
#     progress = new_project.progresso_do_projeto()
#     print(f"Progress of '{new_project.get_nome()}': {progress:.2f}%")
