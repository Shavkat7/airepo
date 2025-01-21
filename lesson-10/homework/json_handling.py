import json
from collections import Counter
import csv

with open('lesson-10/homework/tasks.json', 'r') as file:
    tasks = json.load(file)

total_tasks = len(tasks)
completed_tasks = Counter(task['completed'] for task in tasks)
pending_tasks = total_tasks - completed_tasks[True]
average_priority = sum(task['priority'] for task in tasks) / total_tasks

print(f'Total tasks: {total_tasks}')
print(f'Completed tasks: {completed_tasks[True]}')
print(f'Pending tasks: {pending_tasks}')
print(f'Average priority: {average_priority}')

with open("lesson-10/homework/tasks.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames = tasks[0].keys())
    writer.writeheader()
    writer.writerows(tasks)

    