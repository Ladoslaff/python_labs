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
![img02](/images/lab06/img02.png)
![img03](/images/lab06/img03.png)