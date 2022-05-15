# input
# <color name="html">#e34c26</color>
# output
# tagsList.put("html", "#e34c26");
import re

regex = "(?<=[\"]).*?(?=[<][/])"
input_xml = ""
result = {}

is_input_finished = False
while not is_input_finished:
    tempInput = input()
    if tempInput == '0':
        is_input_finished = True
    input_xml += tempInput

access = re.findall(regex, input_xml)
for i in access:
    txt = i.split("\">")
    result[txt[0]] = txt[1]

for key, value in result.items():
   print("tagsList.put(\"" + key + "\", \"" + value + "\");")
