from typing import List

from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task not in self.tasks:
            self.tasks.append(new_task)

            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str) -> str:

        try:
            curr_task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        Task.COMPLETE_WORD = True
        return f"Completed task {curr_task.name}"

    def clean_section(self) -> str:
        number_of_tasks = len(self.tasks)
        for task in self.tasks:
            if task.COMPLETE_WORD:
                self.tasks.remove(task)
        return f"Cleared {number_of_tasks - len(self.tasks)} tasks."

    def view_section(self) -> str:

        result = [f"Section {self.name}:"]

        [result.append(t.details()) for t in self.tasks]

        return "\n".join(result)


