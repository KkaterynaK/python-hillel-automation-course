class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department

class Developer(Employee):
    def __init__(self, language, **kwargs):
        super().__init__(**kwargs)
        self.language = language

class TeamLead(Manager, Developer):
    def __init__(self, team_size, **kwargs):
        super().__init__(**kwargs)
        self.team_size = team_size

lead = TeamLead(
    name="Oleksandr",
    salary=5000,
    department="QA Department",
    language="Python",
    team_size=5
)

print(f"Ім'я: {lead.name}")
print(f"Зарплата: {lead.salary}")
print(f"Відділ: {lead.department}")
print(f"Мова: {lead.language}")
print(f"Команда: {lead.team_size}")
