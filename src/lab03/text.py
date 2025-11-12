import re

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
# print(normalize("ПрИвЕт\nМИр\t"))
# print(normalize("ёжик, Ёлка"))
# print(normalize("Hello\r\nWorld"))
# print(normalize("  двойные   пробелы  "))


def tokenize(text):
    pattern = r'\w+(?:-\w+)*'
    tokens = re.findall(pattern, text)
    return tokens
# print(tokenize("привет мир"))
# print(tokenize("hello,world!!!"))
# print(tokenize("по-настоящему круто" ))
# print(tokenize("2025 год"))
# print(tokenize("emoji 😀 не слово"))



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

# print(f"Слова: {tokens}")
# print(f"Частоты: {freq}") 
# print(f"Топ-2: {top}")
