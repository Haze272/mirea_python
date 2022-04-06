# Над входной таблицей провести ряд преобразований:
# 1) Удалить дубли среди столбцов.
# 2) Удалить пустые столбцы.
# 3) Удалить дубли среди строк.
# 4) Удалить пустые строки.
# 5) Преобразовать содержимое ячеек по примерам.

def main(*data_row):
    rows = len(data_row)
    columns = [0, 0, 0, 0, 0, 0]
    for uno_row in data_row:
        print(uno_row)

    # Для начала уберём все пустые столбцы в таблице
    for i in columns:
        for uno in data_row:
            if uno[i] is None:
                columns[i] += 1
    for j in columns:
        if columns[j] == rows:
            for m in data_row:
                m.pop(j)

    for uno_row in data_row:
        print(uno_row)


main([0.828, "Алексей Шувокберг", "Алексей Шувокберг", None, None, "нет"])
print()

main([0.828, "Алексей Шувокберг", "Алексей Шувокберг", None, None, "нет"],
     [None, None, None, None, None, None],
     [0.956, "Артур Чонефберг", "Артур Чонефберг", None, None, "да"],
     [0.954, "Игнат Ренефак", "Игнат Ренефак", None, None, "нет"],
     [None, None, None, None, None, None],
     [0.956, "Артур Чонефберг", "Артур Чонефберг", None, None, "да"])
print()

main([None, None, None, None, None, None],
     [None, None, None, None, None, None],
     [0.951, "Рустам Точатов", "Рустам Точатов", None, None, "нет"],
     [0.951, "Рустам Точатов", "Рустам Точатов", None, None, "нет"],
     [0.453, "Игорь Чонин", "Игорь Чонин", None, None, "да"],
     [0.091, "Савелий Лутезян", "Савелий Лутезян", None, None, "нет"])

