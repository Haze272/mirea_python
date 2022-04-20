# Над входной таблицей провести ряд преобразований:
# 1) Удалить дубли среди столбцов.
# 2) Удалить пустые столбцы.
# 3) Удалить дубли среди строк. DONE
# 4) Удалить пустые строки. DONE
# 5) Преобразовать содержимое ячеек по примерам.
from itertools import groupby


def main(*data_row):
    data_row = list(data_row)
    rows = len(data_row)

    # удаление лишних строк
    damn = data_row.copy()
    for i in range(rows):
        if all(x is None for x in data_row[i]):
            damn.pop(i)

    # удаление дублей среди строкS
    print(damn)


main([0.828, "Алексей Шувокберг", "Алексей Шувокберг", None, None, "нет"],
     [None, None, None, None, None, None],
     [0.828, "Алексей Шувокберг", "Алексей Шувокберг", None, None, "нет"])
print()


'''main([0.828, "Алексей Шувокберг", "Алексей Шувокберг", None, None, "нет"],
     [None, None, None, None, None, None],
     [0.956, "Артур Чонефберг", "Артур Чонефберг", None, None, "да"],
     [0.954, "Игнат Ренефак", "Игнат Ренефак", None, None, "нет"],
     [None, None, None, None, None, None],
     [0.956, "Артур Чонефберг", "Артур Чонефберг", None, None, "да"])
print()'''

main([None, None, None, None, None, None],
     [None, None, None, None, None, None],
     [0.951, "Рустам Точатов", "Рустам Точатов", None, None, "нет"],
     [0.951, "Рустам Точатов", "Рустам Точатов", None, None, "нет"],
     [0.453, "Игорь Чонин", "Игорь Чонин", None, None, "да"],
     [None, None, None, None, None, None],
     [0.091, "Савелий Лутезян", "Савелий Лутезян", None, None, "нет"])

