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
![img05](//images/lab01/img05.png)


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
![img02.png](https://github.com/Ladoslaff/python_labs/blob/main/images/lab02/img02.png)


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
![img03.png](https://github.com/Ladoslaff/python_labs/blob/main/images/lab02/img03.png)


## Задание 2
``` python

```
- скрин вывода -
![]()



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
![img05.png](/images/lab02/img05.png)




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
![img06.png](//images/lab02/img06.png)




``` python

```
- скрин вывода -
![]()



``` python

```
- скрин вывода -
![]()


