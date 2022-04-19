# Для словарей

from hypothesis import given, strategies as st


@given(data=st.dictionaries(st.booleans(), st.integers(), min_size=2))
def clean_dicts(data):
    print(data)
    assert len(data) != 0
    assert isinstance(data[True], int)  # Сложно доказать легко проверить
    data.clear()
    assert (len(data) == 0)


clean_dicts()