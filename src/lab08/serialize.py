import json
from models import Student
from pathlib import Path

def save_to_json(students, filename):
    data = [s.to_dict() for s in students]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_from_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    students = []
    for item in data:
        students.append(Student.from_dict(item))
    return students

if __name__ == "__main__":
    data_folder = Path("/Users/vladislav/python_labs/data/lab08")
    data_folder.mkdir(parents=True, exist_ok=True)
    
    input_file = data_folder / "students_input.json"
    output_file = data_folder / "students_output.json"
    
    example_students = [
        Student(fio="Иванов Петр", birthdate="2007-10-19", group="BIVT-25-8", gpa=4.8),
        Student(fio="Петров Иван", birthdate="2006-09-28", group="BIVT-25-12", gpa=4.6),
    ]
    
    save_to_json(example_students, input_file)
    print(f"Создан: {input_file}")
    
    loaded_students = load_from_json(input_file)
    print("\nЗагружено:")
    for student in loaded_students:
        print(f"  {student}")
    
    save_to_json(loaded_students, output_file)
    print(f"\nСохранен: {output_file}")