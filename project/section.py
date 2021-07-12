from To_Do_List.project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task_name == task.name:
                task.completed = True
                return f"Completed task {task.name}"
            return f"Could not find task with the name {task.name}"

    def clean_section(self):
        cleared_tasks = 0
        for t in self.tasks:
            if t.completed:
                cleared_tasks += 1
                self.tasks.remove(t)
        return f"Cleared {cleared_tasks} tasks."

    def view_section(self):
        result = f"Section {self.name}:"
        for t in self.tasks:
            result += f"\n{t.details()}"
        return result
