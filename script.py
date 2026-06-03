import json
import os

class Task:
    def __init__(self, id, title, description, priority="Moyenne", status="À faire"):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority  # Haute, Moyenne, Basse
        self.status = status      # À faire, En cours, Terminé

    def to_dict(self):
        """Convertit l'objet Task en dictionnaire pour le format JSON"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status
        }

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Charge les tâches depuis le fichier JSON s'il existe"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    # On reconstruit les objets Task à partir du JSON
                    self.tasks = [Task(**task) for task in data]
                except json.JSONDecodeError:
                    self.tasks = []
        else:
            self.tasks = []

    def save_tasks(self):
        """Sauvegarde la liste des tâches dans le fichier JSON"""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4, ensure_ascii=False)

    def add_task(self, title, description, priority="Moyenne"):
        """Ajoute une nouvelle tâche avec un ID unique automatique"""
        next_id = max([task.id for task in self.tasks], default=0) + 1
        new_task = Task(next_id, title, description, priority)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"🎉 Tâche '{title}' ajoutée avec succès (ID: {next_id}) !")

# Bloc de test temporaire pour vérifier que la base fonctionne
if __name__ == "__main__":
    manager = TaskManager()
    print("--- Test de la structure ---")
    manager.add_task("Configurer l'environnement", "Installer Python et Git sur la machine", "Haute")