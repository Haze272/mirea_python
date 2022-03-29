import csv
import datetime
from matplotlib import pyplot as plt


def parse_time(text):
    result = datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S.%f")
    return result.time()


with open('messages.csv', encoding='utf8') as f:
    messages = list(csv.reader(f, delimiter=','))
with open('results.csv', encoding='utf8') as f:
    results = list(csv.reader(f, delimiter=','))

for i in range(10):
    print(messages[i])
    print(results[i], '\n')

alltime = []
for msg in messages:
    alltime.append(parse_time(msg[4]))

print(alltime[0])


x = alltime
y = range(len(x))

plt.plot(x, y)
plt.show()


#plt.plot(messages)
#plt.show()
