# HW_ABC_3
Домашнее задание номер 3 по курсу "Архитектура вычислительных систем"

# Отчет по заданию 3

## Описание полученного задания
**Обобщенный артефакт, используемый в задании:** Квадратные матрицы с действительными числами

**Базовые альтернативы
(уникальные параметры,
задающие отличительные
признаки альтернатив):**
1. Обычный двумерный
массив
2. Диагональная (на основе
одномерного массива)
3. Нижняя треугольная
матрица (одномерный массив с формулой пересчета)

**Общие для всех альтернатив переменные:** Размерность – целое число

**Общие для всех альтернатив функции:** Вычисление среднего арифметического (действительное число)

**Обработка контейнера:** Упорядочивание элементов контейнера по убыванию используя Shaker Sort.
В качестве ключей для сортировки и других действий используются результаты функции, общей для всех альтернатив.

## Характеристики программы
**Число модулей**: 6 (8997 байт, ~9Кб)

**Результаты тестирования:**
1. test_in_1_bad.txt - catched exeption: "Incorrect number of values in file!"
2. test_in_2_bad.txt - 0.0005s - ignore problem
3. test_in_5.txt - 0.00057s
4. test_in_10.txt - 0.0017s
5. test_in_100.txt - 0.0064s
6. test_in_1000.txt - 0.195s
7. test_in_10000.txt - 12.068s

## Особенности архитектуры программы

** Каждая из альтернатив представлена в виде списка, элементами которого являются: название (str), размерность (int), содержимое (list), среднее (float)

**Отображение содержимого модуля main на память

* main
  * start_time (float)
  * argc (list)
  * cont (list)
  * count (int)
  * in_file (_io.TextIOWrapper (file))
  * data (list)
  * out_file_name (_io.TextIOWrapper (file))
  * out_file_name_sorted (_io.TextIOWrapper (file))
  * end_time (float)
  * extender.py (module) 
* input_error_message
* count_error_message
* file_error_message
* value_error_message
* index_error_message

**Отображение содержимого модуля extender на память**

* extender
  * common (module)
  * diagonal (module)
  * diagonal (module)
  * container (module)

**Отображение содержимого модуля container на память**

* in_file
  * line (str)
  * k (int)
  * common_matrix (list)
  * diagonal_matrix (list)
  * triangularn_matrix (list)
* in_random
  * k (int)
  * common_matrix (list)
  * diagonal_matrix (list)
  * triangularn_matrix (list)
* out
  * matrix (list)
* shaker_sort
  * swapped (bool)
  * start (int)
  * end (int)
  * i (int)

**Отображение модуля common на память**

* in_file
  * i (int)
  * j (int)
* in_random
* average

**Отображение модуля diagonal на память**

* in_file
  * i (int)
* in_random
* average

**Отображение модуля trinagularn на память**

* in_file
  * i (int)
* in_random
* average

# Сравнение с предыдущими реализациями

Реализация программы на динамически типизированном языке выигрывает по времени исполнения (на максимальном тесте 12s вместо 20s!), но это происходит только по причине того, что код программы на динамически типизированном языке был оптимизирован (функция общая для всех альтернатив теперь считается не каждый раз, а хранится), при изначальной оптимизации кода, код на динамически типизированном языке заметно проигрывал бы другим программам (примерно в 50 раз был бы медленнее). Но зато он выигрывает по времени написания кода: его проще писать и читать.

На мой взгляд ниболее подходящим подходом для данной задачи является именно динамически типизированный
