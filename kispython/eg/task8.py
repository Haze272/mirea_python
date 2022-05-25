import re


def main(str):
    pattern = "(?<=[{]).*?(?=[)])"
    pattern2 = "(?<=[@][']).*?(?=['])"
    pattern3 = "(?<=[:][\"]).*?(?=[\"][.])"
    result = {}

    str = str.replace(" ", "")
    str = str.replace("\n", "")
    access = re.findall(pattern, str)

    for i in access:
        txt = i.split("=")
        key = re.findall(pattern3, txt[1])[0]
        value = re.findall(pattern2, txt[0])
        result[key] = value

    return result

str1 = ".begin( let{@'aerxe'@'maonxe' @'ralala' }=: \"ortere\". ); (let {@'laan'@'usmais' @'zare' }=: \"leed\". );( let{@'tirage_706'@'rearbi_805' @'edce' } =: \"onxe_861\".); (let{ @'arat'@'ace_100'}=:\"anle_391\". ); .end"
str2 = ".begin (let { @'zavete' @'islaed_153' } =: \"requ_897\". );( let {@'onti'@'xeesdi_899' } =: \"uslece\".); (let{ @'reedle'@'argeza_28'} =:\"maen\". );( let { @'xeti_697' @'biage'@'diso_732' } =: \"tebean_187\".);.end"

print(main(str1))
print(main(str2))
