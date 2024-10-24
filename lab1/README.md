# Лабораторная работа №1

## Пункт 8

**Задание:**

> Построить потенциальные диаграммы для контура с источником напряжения и контура без источника напряжения.

**Решение:**

В качестве контура с источниками напряжения (ЭДС) возьмём контур *abcdefa*, а для второго случая (без ЭДС) - *bcefb*.

Для построения требуется зависимость потенциала от сопротивления. Необходимо взять начальный потенциал, для первого случая возьмём потенциал в точке *a* равный 11 В. Чтобы получить потенциал в следующей точке нужно вычислить сумму потенциала и напряжения в ветви, где знак напряжения зависит от направления тока относительно предыдущей точки (входит в предыдущую точку - будет плюс, а выходит - минус). Нужно так же не забывать суммировать сопротивления для каждой точки. Еслм в ветви есть и ЭДС и сопротивление, то её нужно разбить на две.

Пример для точки *b*:

```math
\phi_b = \phi_a - I_1 R_1
```

Общая формула:

```math
\phi_i = \phi_{i-1} \pm I_{i-1} R_{i-1}
```

**Для контура abcdefa:**

```math
$$\phi_a = 11 В \quad R_a = 0 Ом $$
$$\phi_b = 5,752 В \quad R_b = 128 Ом $$
$$\phi_c = 6,052 В \quad R_c = 428 Ом $$
$$\phi_d = 9,016 В \quad R_d = 656 Ом $$
$$\phi_e = 0,016 В \quad R_e = 656 Ом $$
$$\phi_f = 0,306 В \quad R_f = 946 Ом $$
$$\phi_{a_{calc}} = 11,306 В \quad R_{a_{calc}} = 946 Ом $$
```

**Для контура bcefb:**

```math
$$\phi_b = 6,3 В \quad R_b = 0 Ом $$
$$\phi_c = 6,6 В \quad R_c = 300 Ом $$
$$\phi_e = 12,3 В \quad R_e = 775 Ом $$
$$\phi_f = 12,6 В \quad R_f = 1065 Ом $$
$$\phi_{b_{calc}} = 6,3 В \quad R_{b_{calc}} = 1215 Ом $$
```

После этих вычислений получим следующие графики:

![Потенциальные диаграммы](https://raw.githubusercontent.com/Retr0-code/tec-labs/refs/heads/lab1/lab1/PotentialDiagrams.jpeg)
