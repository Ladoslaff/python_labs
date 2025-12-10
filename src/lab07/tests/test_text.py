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
