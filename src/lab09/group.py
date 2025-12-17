import csv
from pathlib import Path
from models import Student

class Group:
    def __init__(self, file_path):
        self.file = Path(file_path)
        self._create_file()

    def _create_file(self):
        if not self.file.exists():
            with self.file.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["fio", "birthdate", "group", "gpa"])

    def _load(self):
        data = []
        with self.file.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data

    def _save(self, data):
        with self.file.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writeheader()
            writer.writerows(data)

    def all(self):
        data = self._load()
        return [Student(**r) for r in data]

    def add(self, student):
        data = self._load()
        data.append({
            "fio": student.fio,
            "birthdate": student.birthdate,
            "group": student.group,
            "gpa": str(student.gpa)
        })
        self._save(data)

    def find(self, text):
        text = text.lower()
        data = self._load()
        found = []
        for row in data:
            if text in row["fio"].lower():
                found.append(Student(**row))
        return found

    def remove(self, name):
        data = self._load()
        new_data = [r for r in data if r["fio"] != name]
        self._save(new_data)

    def update(self, name, **new_data):
        data = self._load()
        for row in data:
            if row["fio"] == name:
                for key, value in new_data.items():
                    if key in ["fio", "birthdate", "group", "gpa"]:
                        row[key] = value
        self._save(data)

    def count(self):
        return len(self._load())

    def average_gpa(self):
        data = self._load()
        if not data:
            return 0
        total = sum(float(r["gpa"]) for r in data)
        return round(total / len(data), 2)


if __name__ == "__main__":
    folder = Path("/Users/vladislav/python_labs/data/lab09")
    folder.mkdir(parents=True, exist_ok=True)
    
    csv_path = folder / "students.csv"
    
    if csv_path.exists():
        csv_path.unlink()
    
    group = Group(csv_path)
    
    print("Добавляем студентов")
    students_to_add = [
        Student(fio="Соколов Андрей", birthdate="2007-11-15", group="БИВТ-25-1", gpa=4.8),
        Student(fio="Волкова Екатерина", birthdate="2004-05-22", group="БИВТ-25-2", gpa=3.2),
        Student(fio="Кузнецов Михаил", birthdate="2008-03-10", group="БИВТ-25-3", gpa=3.7),
        Student(fio="Павлова Ольга", birthdate="2002-07-18", group="БИВТ-25-4", gpa=4.9),
        Student(fio="Новиков Алексей", birthdate="2003-01-30", group="БИВТ-25-1", gpa=4.4),
    ]
    
    for student in students_to_add:
        group.add(student)
    
    print(f"Добавлено студентов: {group.count()}")
    
    print("\nВсе студенты:")
    all_students = group.all()
    for student in all_students:
        print(student)
    
    print("\nПоиск 'Соколов':")
    found_students = group.find("Соколов")
    for student in found_students:
        print(f"Найден: {student}")
    
    print("\nОбновляем Соколова:")
    group.update("Соколов Андрей", gpa=4.6, group="БИВТ-25-2")
    after_update = group.find("Соколов Андрей")
    if after_update:
        print(f"После обновления: {after_update[0]}")
    
    print("\nУдаляем Новикова:")
    group.remove("Новиков Алексей")
    print(f"Теперь студентов: {group.count()}")
    
    print(f"\nСредний балл: {group.average_gpa()}")
    print(f"Файл: {csv_path}")