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

def afficher_menu():
    print("\n" + "="*30)
    print(" 📋 GESTIONNAIRE DE TÂCHES PRO ")
    print("="*30)
    print("1. Afficher toutes les tâches")
    print("2. Ajouter une tâche")
    print("3. Modifier le statut d'une tâche")
    print("4. Quitter")
    print("="*30)

if __name__ == "__main__":
    manager = TaskManager()
    
    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-4) : ")
        
        if choix == "1":
            print("\n--- Liste des tâches ---")
            if not manager.tasks:
                print("Aucune tâche enregistrée.")
            for task in manager.tasks:
                print(f"[{task.id}] {task.title} - Priorité: {task.priority} | Statut: {task.status}")
                print(f"    Description: {task.description}")
        
        elif choix == "2":
            print("\n--- Ajouter une nouvelle tâche ---")
            title = input("Titre de la tâche : ")
            desc = input("Description : ")
            priority = input("Priorité (Haute, Moyenne, Basse) [Moyenne] : ") or "Moyenne"
            manager.add_task(title, desc, priority)
            
        elif choix == "3":
            print("\n--- Modifier le statut ---")
            try:
                task_id = int(input("Entrez l'ID de la tâche à modifier : "))
                # Recherche de la tâche par ID
                task = next((t for t in manager.tasks if t.id == task_id), None)
                if task:
                    print("1. À faire | 2. En cours | 3. Terminé")
                    statut_choix = input("Nouveau statut (1-3) : ")
                    if statut_choix == "1": task.status = "À faire"
                    elif statut_choix == "2": task.status = "En cours"
                    elif statut_choix == "3": task.status = "Terminé"
                    
                    manager.save_tasks()
                    print(f"👍 Statut mis à jour pour la tâche {task_id} !")
                else:
                    print("❌ ID introuvable.")
            except ValueError:
                print("❌ Veuillez entrer un ID valide.")
                
        elif choix == "4":
            print("\n👋 Au revoir !")
            break
        else:
            print("❌ Option invalide. Veuillez choisir entre 1 et 4.")