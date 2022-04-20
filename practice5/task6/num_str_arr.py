# Тестирование для чисел, строк и массивов

from hypothesis import given, strategies as st


def add(x, y):
    return x + y

@given(x=st.integers(), y=st.integers(), z=st.integers())
def test_add_num(x, y, z):
    print(x, y, z);
    assert add(x, y) == add(y, x)  # Трудно доказать, легко проверить.
    assert add(x, add(y, z)) == add(add(x, y), z)  # Трудно доказать, легко проверить.

@given(x=st.text(), y=st.text(), z=st.text())
def test_add_str(x, y, z):
    print(x, y, z)
    assert add(x, y) == add(x, y)

def get_max_of_arr(data):
    return max(data, key=data.count)

@given(data=st.lists(st.integers(), min_size=5))
def test_arr(data):
    print(data)
    res = get_max_of_arr(data)
    # Трудно доказать, легко проверить
    assert res in data
    assert all(data.count(res) >= data.count(x) for x in data)


if __name__ == "__main__":
    #test_add_num()
    #test_add_str()
    test_arr()
