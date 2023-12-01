class ToDoList:
    def _init_(self):
        self.tasks = {}

    def add_task(self, task, priority=1):
        if priority not in self.tasks:
            self.tasks[priority] = []
        self.tasks[priority].append(task)
        print(f'Tarefa "{task}" adicionada com prioridade {priority}.')

    def view_tasks(self):
        if not self.tasks:
            print('Nenhuma tarefa cadastrada.')
            return

        print('Tarefas:')
        for priority in sorted(self.tasks.keys()):
            for task in self.tasks[priority]:
                print(f'[{priority}] {task}')

    def complete_task(self, task):
        for priority in self.tasks:
            if task in self.tasks[priority]:
                self.tasks[priority].remove(task)
                print(f'Tarefa "{task}" concluída.')
                if not self.tasks[priority]:  # Se a lista de tarefas de uma prioridade estiver vazia, remova a prioridade.
                    del self.tasks[priority]
                return

        print(f'Tarefa "{task}" não encontrada.')

# Exemplo de uso
if _name_ == "_main_":
    todo_list = ToDoList()

    todo_list.add_task("Estudar Python", priority=2)
    todo_list.add_task("Fazer compras", priority=1)
    todo_list.add_task("Ler livro", priority=3)

    todo_list.view_tasks()

    todo_list.complete_task("Fazer compras")

    todo_list.view_tasks()