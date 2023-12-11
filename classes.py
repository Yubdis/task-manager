import json
from datetime import datetime


class Tarefa:
    lista_tarefas = []

    def __init__(self, titulo, descricao=None, status=None):
        self._titulo = titulo
        self._descricao = descricao
        self._status = status
        self._data_criacao = datetime.now()
        self._data_conclusao = None
        Tarefa.lista_tarefas.append(self)

    def alterar_status(self):
        if self._status is None:
            self._status = "ativa"
            self._data_criacao = datetime.now()
        elif self._status == "ativa":
            self._status = "completa"
            self._data_conclusao = datetime.now()

    def atualizar_descricao(self, descricao):
        self._descricao = descricao

    def get_titulo(self):
        return self._titulo

    def get_status(self):
        return self._status

    def to_dict(self):
        return {
            "titulo": self._titulo,
            "descricao": self._descricao,
            "status": self._status,
            "data_criacao": self._data_criacao.strftime("%d-%m-%Y"),
            "data_conclusao": self._data_conclusao.strftime("%d-%m-%Y")
            if self._data_conclusao
            else None,
        }

    @classmethod
    def from_dict(cls, task_dict):
        try:
            task = cls(task_dict["titulo"], task_dict["descricao"], task_dict["status"])
            task._data_criacao = datetime.strptime(
                task_dict["data_criacao"], "%d-%m-%Y"
            )
            if task_dict["data_conclusao"]:
                task._data_conclusao = datetime.strptime(
                    task_dict["data_conclusao"], "%d-%m-%Y"
                )
            return task
        except KeyError as e:
            raise ValueError(f"Missing key in task data: {e}")
        except (TypeError, ValueError) as e:
            raise ValueError(f"Error creating task from data: {e}")


class Usuario:
    lista_usuarios = []

    def __init__(self, nome, email):
        self._nome = nome
        self._email = email
        self._lista_tarefas = []
        Usuario.lista_usuarios.append(self)

    def criar_tarefa(self, titulo, descricao=None):
        nova_tarefa = Tarefa(titulo, descricao)
        nova_tarefa.alterar_status()
        self._lista_tarefas.append(nova_tarefa)

    def remove_tarefa(self, item_index):
        del self._lista_tarefas[item_index]

    def marcar_concluida(self, tarefa):
        if tarefa in self._lista_tarefas:
            tarefa.alterar_status()
        else:
            print("Error: Task not found in user's task list.")

    def get_lista_tarefas(self):
        return self._lista_tarefas

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email

    def to_dict(self):
        return {
            "nome": self._nome,
            "email": self._email,
            "lista_tarefas": [tarefa.to_dict() for tarefa in self._lista_tarefas],
        }

    @classmethod
    def from_dict(cls, user_dict):
        try:
            user = cls(user_dict["nome"], user_dict["email"])
            user._lista_tarefas = [
                Tarefa.from_dict(task_dict) for task_dict in user_dict["lista_tarefas"]
            ]
            return user
        except KeyError as e:
            raise ValueError(f"Missing key in user data: {e}")
        except (TypeError, ValueError) as e:
            raise ValueError(f"Error creating user from data: {e}")


class Projeto:
    lista_projetos = []

    def __init__(self, nome, descricao=None):
        self._nome = nome
        self._descricao = descricao
        self._lista_tarefas = []
        Projeto.lista_projetos.append(self)

    def adicionar_tarefa(self, tarefa, usuario):
        if not isinstance(tarefa, Tarefa) or not isinstance(usuario, Usuario):
            print("Error: Invalid task or user provided.")
            return

        if tarefa in self._lista_tarefas:
            print(f"Error: Task '{tarefa._titulo}' Ja esta no projeto.")
            return

        if tarefa not in usuario._lista_tarefas:
            print(
                f"Error: User '{usuario.get_nome()}' nao tem permisao para adicionar tarefa."
            )
            return

        self._lista_tarefas.append(tarefa)
        print(f"Task '{tarefa._titulo}' adicionar com sucesso.")

    def progresso_do_projeto(self):
        unfinished_tasks = sum(
            1 for tarefa in self._lista_tarefas if tarefa._status == "ativa"
        )
        total_tasks = len(self._lista_tarefas)
        progress_percentage = (
            (total_tasks - unfinished_tasks) / total_tasks * 100
            if total_tasks > 0
            else 0
        )
        return progress_percentage

    def get_nome(self):
        return self._nome

    def get_descricao(self):
        return self._descricao

    def to_dict(self):
        return {
            "nome": self._nome,
            "descricao": self._descricao,
            "lista_tarefas": [tarefa.to_dict() for tarefa in self._lista_tarefas],
        }

    @classmethod
    def from_dict(cls, project_dict):
        try:
            project = cls(project_dict["nome"], project_dict["descricao"])
            project._lista_tarefas = [
                Tarefa.from_dict(task_dict)
                for task_dict in project_dict["lista_tarefas"]
            ]
            return project
        except KeyError as e:
            raise ValueError(f"Missing key in project data: {e}")
        except (TypeError, ValueError) as e:
            raise ValueError(f"Error creating project from data: {e}")


def save_to_json(data, filename):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=2)
    except (IOError, json.JSONDecodeError) as e:
        raise ValueError(f"Error saving to JSON file {filename}: {e}")


def load_from_json(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {filename}")
    except (IOError, json.JSONDecodeError) as e:
        raise ValueError(f"Error loading from JSON file {filename}: {e}")


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
#     new_project.adicionar_tarefa(new_user._lista_tarefas[0], new_user)
#     progress = new_project.progresso_do_projeto()
#     print(f"Progress of '{new_project.get_nome()}': {progress:.2f}%")

#     all_users = [new_user.to_dict()]
#     all_projects = [new_project.to_dict()]
#     save_to_json({"usuarios": all_users, "projetos": all_projects}, "updated_data.json")

#     # Load the updated data from the JSON file
#     loaded_data = load_from_json("updated_data.json")

#     # Retrieve users
#     loaded_users = [
#         Usuario.from_dict(user_dict) for user_dict in loaded_data["usuarios"]
#     ]
#     loaded_projects = [
#         Projeto.from_dict(project_dict) for project_dict in loaded_data["projetos"]
#     ]

#     # Print loaded users and projects
#     for loaded_user in loaded_users:
#         print(f"\nUser: {loaded_user.get_nome()}")
#         for task in loaded_user._lista_tarefas:
#             print(f"  - Task: {task._titulo}, Status: {task._status}")

#     for loaded_project in loaded_projects:
#         print(f"\nProject: {loaded_project.get_nome()}")
#         for task in loaded_project._lista_tarefas:
#             print(f"  - Task: {task._titulo}, Status: {task._status}")

# except ValueError as e:
#     print(f"Error: {e}")
# except KeyboardInterrupt:
#     print("\nProgram terminated by user.")
