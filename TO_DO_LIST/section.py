from project.task import Task


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
        for t in self.tasks:
            if task_name == t.name:
                t.completed = True
                return f"Completed task {t.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        cleared_tasks = 0
        to_remove = []
        for t in self.tasks:
            if t.completed:
                cleared_tasks += 1
                to_remove.append(t)
        for obj in to_remove:
            self.tasks.remove(obj)
        return f"Cleared {cleared_tasks} tasks."

    def view_section(self):
        result = f"Section {self.name}:"
        for t in self.tasks:
            result += f"\n{t.details()}"
        return result


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
