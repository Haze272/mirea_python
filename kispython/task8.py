import re


def main(str):
    pattern = "(?<=[#]).*?(?=[.][:][>])"
    result = {}

    str = str.replace(" ", "")
    str = str.replace("\n", "")
    access = re.findall(pattern, str)

    for i in access:
        txt = i.split("->")
        result[txt[1]] = int(txt[0])

    return result

str1 = "{<:auto #9684 ->leorbe. :>. <:auto #-1244 -> rari. :>. <:auto #1761 ->bira.:>. }"
str2 = "{ <: auto #3109 -> rienla_709. :>.<: auto #-9400 ->atge_467. :>.}"
str3 = '{<:auto #9684 ->leorbe. :>. <:auto #-1244 -> rari. :>. <:auto #1761\n->bira.:>. }'

print(main(str1))
print(main(str2))
print(main(str3))