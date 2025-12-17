# ЛАБОРАТОРНАЯ РАБОТА 1
## Задание 1
``` python
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age + 1}."
```
- скрин вывода - 
![img01](https://github.com/Ladoslaff/python_labs/blob/main/images/lab01/img01.png)

## Задание 2
``` python
num1 = float(input("a: "))
num2 = float(input("b: "))
sum = num1 + num2 
avg = sum/2
print(f"sum = {sum:.2f}", ";", f"avg={avg:.2f}")
```
- скрин вывода - 
![img02](https://github.com/Ladoslaff/python_labs/blob/main/images/lab01/img02.png)

## Задание 3
``` python
price = float(input("Введите цену = "))
discount = float(input("Скидка = "))
vat = float(input("НДС = "))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {base:.2f} ₽")
print(f"НДС: {vat_amount:.2f} ₽")
print(f"Итого к оплате: {total:.2f} ₽")
```
- скрин вывода - 
![img03](https://github.com/Ladoslaff/python_labs/blob/main/images/lab01/img03.png)

## Задание 4
``` python
minuts = int(input("Введите кол-во минут = "))
h = minuts//60
mm = minuts%60
print(f"{h}:{mm:02d}")
```
- скрин вывода - 
![img04](https://github.com/Ladoslaff/python_labs/blob/main/images/lab01/img04.png)

## Задание 5
``` python
fio = input("Введите ФИО ").split()
print("Инициалы = ", fio[0][0], fio[1][0], fio[2][0], sep = '')
print(len(fio[0] + fio[1] + fio[2])+2)
```
- скрин вывода - 
![img05](https://github.com/Ladoslaff/python_labs/blob/main/images/lab01/img05.png)


# ЛАБОРАТОРНАЯ РАБОТА 2


## Задание 1
``` python
def min_max(nums):
    if len(nums) == 0:
        raise ValueError
    mini = min(nums)
    maxi = max(nums)
    return (mini, maxi)
nums = [3, -1, 5, 5, 0] 
print(min_max(nums))
nums = [42]
print(min_max(nums))
nums = [-5, -2, -9]
print(min_max(nums))
nums = [1.5, 2, 2.0, -3.1]
print(min_max(nums))
nums = []
print(min_max(nums))
```
- скрин вывода -
![img01](https://github.com/Ladoslaff/python_labs/blob/main/images/lab02/img01.png)



``` python
def unique_sorted(nums):
    nums = sorted(set(nums))
    return nums
nums = [3, 1, 2, 1, 3]
print(unique_sorted(nums))
nums = []
print(unique_sorted(nums))
nums = [-1, -1, 0, 2, 2]
print(unique_sorted(nums))
nums = [1.0, 1, 2.5, 2.5, 0]
print(unique_sorted(nums))
```
- скрин вывода -
![img02](https://github.com/Ladoslaff/python_labs/blob/main/images/lab02/img02.png)


``` python
def flatten(nums):
    otvetik = []
    for e in nums:
        if type(e) == list or type(e) == tuple:
            for i in range(len(e)):
                if e[i] != '':
                    otvetik.append(e[i])
        else:
            raise TypeError
    return otvetik
nums = [[1, 2], [3, 4]]
print(flatten(nums))
nums = [[1, 2], (3, 4, 5)]
print(flatten(nums))
nums = [[1], [], [2, 3]]
print(flatten(nums))
nums = [[1, 2], "ab"]
print(flatten(nums))
```
- скрин вывода -
![img03](https://github.com/Ladoslaff/python_labs/blob/main/images/lab02/img03.png)


## Задание 2
``` python
def transpose(mat):
    if not mat:
        return []
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError
    result = []
    for col_index in range(len(mat[0])):
        new_row = []
        for row in mat:
            new_row.append(row[col_index])
        result.append(new_row)
    return result
```
- скрин вывода -
![img04](/images/lab02/img04.png)



``` python
def row_sums(l):
    new_l = []
    if len(l) == 0:
        return new_l
    for i in range(len(l) - 1):
        if len(l[i]) != len(l[i+1]):
            raise TypeError
    for i in l:
        new_l.append(sum(i))
    return new_l
nums = [[1, 2, 3], [4, 5, 6]]
print(row_sums(nums))
nums = [[-1, 1], [10, -10]]
print(row_sums(nums))
nums = [[0, 0], [0, 0]]
print(row_sums(nums))
nums = [[1, 2], [3]]
print(row_sums(nums))
```
- скрин вывода -
![img05](/images/lab02/img05.png)




``` python
def col_sums(l):
    new_l = []
    if len(l) == 0:
        return new_l
    for i in range(len(l) - 1):
        if len(l[i]) != len(l[i+1]):
            raise TypeError
    for i in range(len(l)-1):
        for j in range(len(l[1])):
            new_l.append(l[i][j] + l[i+1][j])
    return new_l
nums = [[1, 2, 3], [4, 5, 6]]
print(col_sums(nums))
nums = [[-1, 1], [10, -10]]
print(col_sums(nums))
nums = [[0, 0], [0, 0]]
print(col_sums(nums))
nums = [[1, 2], [3]]
print(col_sums(nums))
```
- скрин вывода -
![img06](/images/lab02/img06.png)



## Задание 3

``` python
def format_record(rec):
    fio, group, gpa = rec
    if not fio or not fio.strip():
        raise ValueError("ФИО не может быть пустым")
    if not group or not group.strip():
        raise ValueError("Группа не может быть пустой")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")
    fio_clean = ' '.join(fio.split())  # минус лишние пробелы
    fio_clean = fio_clean.title()      # первые буквы заглавнык
    parts = fio_clean.split()
    surname = parts[0] 
    initials = []
    for name in parts[1:]:  
        if name:  
            initials.append(name[0] + '.')  
    if initials:
        formatted_fio = surname + ' ' + ''.join(initials)
    else:
        formatted_fio = surname
    formatted_gpa = f"{gpa:.2f}"
    result = f"{formatted_fio}, гр. {group}, GPA {formatted_gpa}"
    return result
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Петр", "IKBO-12", 5.0)))
print(format_record(("Петров Петр Петрович", "IKBO-12", 5.0)))
print(format_record((" сидорова айна сергеевна ", "ABB-01", 3.999)))
print(format_record(("  ", "", )))
```
- скрин вывода -
![img07](/images/lab02/img07.png)

# ЛАБОРАТОРГАЯ РАБОТА 3
## Задание 1
```python
def normalize(text, *, casefold=True, yo2e=True):
    result = text
    if casefold:
        result = result.casefold()
    
    if yo2e:
        result = result.replace('ё', 'е')
        result = result.replace('Ё', 'е')
    result = result.replace('\t', ' ')
    result = result.replace('\n', ' ')
    result = result.replace('\r', ' ')
    words = result.split()
    result = ' '.join(words)
    return result
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
```
- скрин вывода -
![img01](/images/lab03/img01.png)



```python
def tokenize(text):
    pattern = r'\w+(?:-\w+)*'
    tokens = re.findall(pattern, text)
    return tokens
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто" ))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
```
- скрин вывода -
![img02](/images/lab03/img02.png)




```python
def count_freq(tokens):
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] = 1
    return freq

def top_n(freq, n=5):
    items = list(freq.items())
    items.sort(key=lambda x: (-x[1], x[0])) # - x[1] - это частота слова. -x[1] - минус делает сортировку по убыванию. x[0] - сортировка по возрастанию (А→Я)
    top_items = items[:n]
    return top_items
tokens = ["a", "b", "a", "c", "b", "a"]
freq = count_freq(tokens)
top = top_n(freq, 2)

print(f"Слова: {tokens}")
print(f"Частоты: {freq}") 
print(f"Топ-2: {top}")
```
- скрин вывода -
![img03](/images/lab03/img03.png)

## Задание 2
``` python
from text import normalize, tokenize, count_freq, top_n
text = input("Введите текст: ")
normalized_text = normalize(text)
tokens = tokenize(normalized_text)
freq_dict = count_freq(tokens)
top_words = top_n(freq_dict, 5)
print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq_dict)}")
print("Топ-5:")
for word, count in top_words:
    print(f"{word}:{count}")
```
- скрин вывода -
![img04](/images/lab03/img04.png)

# ЛАБОРАТОРНАЯ РАБОТА 4
## Задание 1
``` python
from pathlib import Path
import csv

def read_text(path, encoding="utf-8"):
    file_path = Path(path)
    return file_path.read_text(encoding=encoding)

def write_csv(rows, path, header=None):
    file_path = Path(path)
    rows_list = list(rows)
    
    if rows_list:
        first_row_length = len(rows_list[0])
        for i, row in enumerate(rows_list):
            if len(row) != first_row_length:
                raise ValueError(f"Строка {i} имеет другую длину")
    
    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        if header is not None:
            writer.writerow(header)
        
        for row in rows_list:
            writer.writerow(row)

def ensure_parent_dir(path):
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
```
## Задание 2
``` python
from pathlib import Path
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab03'))

from text import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv, ensure_parent_dir

def create_report(input_file="data/input.txt", output_file="data/report.csv", encoding="utf-8"):
    try:
        text = read_text(input_file, encoding)
    except FileNotFoundError:
        print(f"ОШИБКА: Файл {input_file} не найден!")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"ОШИБКА: Не удалось прочитать файл в кодировке {encoding}!")
        sys.exit(1)
    
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    freq_dict = count_freq(tokens)
    top_words = top_n(freq_dict, 5)
    
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq_dict)}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")
    
    sorted_words = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    csv_data = []
    for word, count in sorted_words:
        csv_data.append([word, count])
    
    ensure_parent_dir(output_file)
    write_csv(csv_data, output_file, header=("word", "count"))
    print(f"Отчет сохранен в: {output_file}")

if __name__ == "__main__":
    create_report()
```
- скрин вывода - 
![img01](/images/lab04/img01.png)

# ЛАБОРАТОРНАЯ РАБОТА 5
## Задание 1
```python 
import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    json_file = Path(json_path)
    if not json_file.exists():
        raise FileNotFoundError
    
    if json_file.suffix.lower() != '.json':
        raise ValueError
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if not data:
        raise ValueError
    
    fieldnames = list(data[0].keys())
    
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow({field: str(row.get(field, '')) for field in fieldnames})
json_to_csv(f"data/samples/people.json", f"data/samples/people.csv")


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError
    
    if csv_file.suffix.lower() != '.csv':
        raise ValueError
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    if not data:
        raise ValueError
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
csv_to_json(f"data/samples/people.csv",f"data/samples/people.json")
```
- Скрины -
![img01](/images/lab05/img01.png)
![img04](/images/lab05/img04.png)

## Задание 2
``` python
import csv
import os
from openpyxl import Workbook
from openpyxl.utils import*


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Файл не найден: {csv_path}")
    
    if not csv_path.lower().endswith('.csv'):
        raise ValueError("Входной файл должен иметь расширение .csv")
    
    if not xlsx_path.lower().endswith(".xlsx"):
        raise ValueError("Выходной файл должен иметь расширение .xlsx")
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    if not rows:
        raise ValueError("CSV-файл пуст")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    for i, col in enumerate(ws.columns, start=1):
        max_length = 0
        for cell in col:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        ws.column_dimensions[get_column_letter(i)].width = max(max_length, 8)

    wb.save(xlsx_path)
csv_to_xlsx("data/samples/people_02.csv", "data/output.xlsx")
```
- Скрины -
![img02](/images/lab05/img02.png)
![img03](/images/lab05/img03.png)

 # ЛАБОРАТОРНАЯ РАБОТА 6
 ## Задание 1
``` python
import argparse
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lab03.text import normalize, tokenize, count_freq, top_n

def cat(input_path, number_lines):
    with open(input_path, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file, 1):
            if number_lines:
                print(f"{i}: {line}", end='')
            else:
                print(line, end='')

def stats(input_text, n=5):
    with open(input_text, 'r', encoding='utf-8') as f:
        text = f.read()

    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    top_words = top_n(freq, n)

    print(f"Топ-{n} самых частых слов:")
    for word, count in top_words:
        print(f"{word}: {count}")

def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Анализы частрты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Кол-во слов в топе")

    args = parser.parse_args()

    if args.command == "cat":
        cat(args.input, args.n)
    elif args.command == "stats":
        stats(args.input, args.top)

if __name__ == "__main__":
    main()
```
- Скрин вывода -
![img01](/images/lab06/img01.png)

# Задание 2
``` python
import argparse
import sys
import os

# Добавляем путь для импорта
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lab05.json_csv import json_to_csv, csv_to_json
from lab05.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    subparsers = parser.add_subparsers(dest="command")

    p1 = subparsers.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = subparsers.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = subparsers.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    os.makedirs("data/out", exist_ok=True) #это типа для результатов папка

    if args.command == "json2csv":
        json_to_csv(args.input, args.output)
        print(f"Успешно: {args.input} -> {args.output}")
    elif args.command == "csv2json":
        csv_to_json(args.input, args.output)
        print(f"Успешно: {args.input} -> {args.output}")
    elif args.command == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)
        print(f"Успешно: {args.input} -> {args.output}")

if __name__ == "__main__":
    main()
```
- Скрин вывода
![img02](/images/lab06/img02.png)
![img03](/images/lab06/img03.png)


# ЛАБОРАТОРНАЯ РАБОТА 7
## Задание A
``` python
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))

from lab03.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Программирование Python", "программирование python"),
        ("Москва Питер Сочи", "москва питер сочи"),
        ("КОД ТЕСТ ПРОВЕРКА", "код тест проверка"),
        ("", ""),
    ],
)
def test_normalize(text, expected):
    result = normalize(text)
    assert result == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("python код тест", ["python", "код", "тест"]),
        ("hello,world!!", ["hello", "world"]),
        ("программирование-это-круто", ["программирование", "это", "круто"]),
        ("", []),
    ],
)
def test_tokenize(text, expected):
    result = tokenize(text)
    assert result == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["a", "b", "a", "c"], {"a": 2, "b": 1, "c": 1}),
        (["код", "тест", "код", "проверка"], {"код": 2, "тест": 1, "проверка": 1}),
        ([], {}),
    ],
)
def test_count_freq(tokens, expected):
    result = count_freq(tokens)
    assert result == expected


@pytest.mark.parametrize(
    "freq, n, expected",
    [
        ({"python": 5, "код": 3, "тест": 2}, 2, [("python", 5), ("код", 3)]),
        ({"яблоко": 3, "груша": 3, "апельсин": 1}, 2, [("груша", 3), ("яблоко", 3)]),
        ({}, 5, []),
        ({"слово": 10}, 0, []),
    ],
)
def test_top_n(freq, n, expected):
    result = top_n(freq, n)
    assert result == expected

```
- скрин вывода --
![img01](/images//lab07/img01.png)

# Задание В
``` python
import pytest
import json
import csv
import sys
import os
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))

from lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_correct_conversion(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_correct_conversion(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerow({"name": "Alice", "age": "22"})
        writer.writerow({"name": "Bob", "age": "25"})

    csv_to_json(str(src), str(dst))

    result = json.loads(dst.read_text(encoding="utf-8"))

    assert len(result) == 2
    assert set(result[0].keys()) == {"name", "age"}
    assert result[1]["name"] == "Bob"


def test_empty_file_error(tmp_path: Path):
    empty_file = tmp_path / "empty.json"
    output = tmp_path / "out.csv"
    empty_file.write_text("")

    with pytest.raises(ValueError):
        json_to_csv(str(empty_file), str(output))


def test_invalid_json_error(tmp_path: Path):
    bad_file = tmp_path / "bad.json"
    output = tmp_path / "out.csv"
    bad_file.write_text("{invalid json")

    with pytest.raises(ValueError):
        json_to_csv(str(bad_file), str(output))


def test_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        json_to_csv("несуществующий_файл.json", "выход.csv")

    with pytest.raises(FileNotFoundError):
        csv_to_json("несуществующий_файл.csv", "выход.json")

```
- Скрин вывода -
![img02](/images/lab07/img02.png)

# Задание С

- Скрин вывода -
![img03](/images/lab07/img03.png)


# ЛАБОРАТОРНАЯ РАБОТА 8
## Задание А
``` python
from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("birthdate must be in format YYYY-MM-DD")
        self.gpa = float(self.gpa)
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA должен быть от 0 до 5, получено {self.gpa}")

    def age(self):
        b = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        years = today.year - b.year
        if (today.month, today.day) < (b.month, b.day):
            years -= 1
        return years

    def to_dict(self):
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }


    @classmethod
    def from_dict(cls, d):
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=float(d["gpa"]),  
        )

    def __str__(self):
        return f"Студент: {self.fio}, группа {self.group}, GPA {self.gpa}, возраст {self.age()}"

s = Student(fio="Иванов Петр", birthdate="2007-10-19", group="BIVT-25-8", gpa=4.8)
print(f"Возраст: {s.age()}")
print(f"{s.to_dict()}")
s.from_dict(s.to_dict())
print(f"{s.__str__()}")
```
- скрин вывода -
![img01](/images/lab08/img01.png)

# Задание B
``` python
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
```
-скрин вывода -
![img02](/images/lab08/img02.png)



# ЛАБОРАТОРНАЯ РАБОТА 9
## Задание А
``` python
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
```
-скрин вывода -
![img01](/images/lab09/img01.png)



# ЛАБОРАТОРНАЯ РАБОТА 10
## Задание А
``` python
from collections import deque

class MyStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class MyQueue:
    def __init__(self):
        self.items = deque()

    def add(self, item):
        self.items.append(item)

    def remove(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items.popleft()

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


if __name__ == "__main__":
    print("Тестирование стека:")
    stack = MyStack()
    
    print("Пустой ли стек?", stack.is_empty())
    
    stack.push(5)
    stack.push(15)
    stack.push(25)
    
    print("Верхний элемент:", stack.top())
    print("Извлекаем:", stack.pop())
    print("Извлекаем:", stack.pop())
    print("Размер стека:", stack.size())
    print("Пустой ли стек?", stack.is_empty())
    
    print()
    
    print("Тестирование очереди:")
    queue = MyQueue()
    
    print("Пустая ли очередь?", queue.is_empty())
    
    queue.add("первый")
    queue.add("второй")
    queue.add("третий")
    
    print("Первый в очереди:", queue.front())
    print("Забираем:", queue.remove())
    print("Забираем:", queue.remove())
    print("Осталось элементов:", len(queue))
    print("Пустая ли очередь?", queue.is_empty())
```
-скрин вывода -
![img01](/images/lab10/lab01.png)


## Задание В
``` python
class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def add_last(self, value):
        new_node = ListNode(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
    
    def add_first(self, value):
        new_node = ListNode(value, self.first)
        self.first = new_node
        if self.last is None:
            self.last = new_node
        self.length += 1

    def insert_at(self, position, value):
        if position < 0 or position > self.length:
            raise IndexError(f"Некорректная позиция: {position}")

        if position == 0:
            self.add_first(value)
            return

        if position == self.length:
            self.add_last(value)
            return

        current = self.first
        for _ in range(position - 1):
            current = current.next

        new_node = ListNode(value, current.next)
        current.next = new_node
        self.length += 1

    def delete_at(self, position):
        if position < 0 or position >= self.length:
            raise IndexError(f"Некорректная позиция: {position}")

        if position == 0:
            deleted_value = self.first.value
            self.first = self.first.next
            if self.first is None:
                self.last = None
            self.length -= 1
            return deleted_value

        current = self.first
        for _ in range(position - 1):
            current = current.next

        deleted_node = current.next
        current.next = deleted_node.next

        if deleted_node is self.last:
            self.last = current

        self.length -= 1
        return deleted_node.value

    def __iter__(self):
        current = self.first
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self.length

    def __repr__(self):
        values = list(self)
        return f"LinkedList({values})"


if __name__ == "__main__":
    print("Демонстрация работы связного списка")
    
    lst = LinkedList()

    lst.add_last(10)
    lst.add_last(20)
    lst.add_last(30)
    print("После добавления в конец:", list(lst))
    
    lst.add_first(5)
    print("После добавления в начало:", list(lst))
    
    lst.insert_at(2, 99)
    print("После вставки на позицию 2:", list(lst))
    
    deleted = lst.delete_at(3)
    print(f"Удален элемент на позиции 3: {deleted}")
    print("После удаления:", list(lst))
    
    print(f"Длина списка: {len(lst)}")
    print(f"Строковое представление: {repr(lst)}")
    
    print("\nИтерация по списку:")
    for item in lst:
        print(f"  - {item}")
```
-скрин вывода -
![img02](/images/lab10/img02.png)