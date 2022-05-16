import re


def main(str):
    pattern = "(?<=[o][p][t]).*?(?=[\"][;])"
    result = {}

    str = str.replace(" ", "")
    str = str.replace("\n", "")
    access = re.findall(pattern, str)

    for i in access:
        txt = i.split("<=@\"")
        result[txt[0]] = txt[1]

    return result

str1 = "((|| opt quus<= @\"onla\";|| ||opt enxe_900 <=@\"soti\"; || ))"
str2 = "((|| opt anle_456<= @\"antiat\"; || ||opt raen <=@\"geti_957\"; ||))"


print(main(str1))
print(main(str2))