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


if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab03'))
    
    from text import normalize, tokenize, count_freq, top_n

    test_text = "Привет, мир! Привет!!!"
    ensure_parent_dir("data/input.txt")
    with open("data/input.txt", "w", encoding="utf-8") as f:
        f.write(test_text)
    print("Создан data/input.txt")

    text = read_text("data/input.txt")
    print(f"Прочитан текст: '{text}'")
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
        
    write_csv(csv_data, "data/report.csv", header=("word", "count"))
    print("Создан data/report.csv")