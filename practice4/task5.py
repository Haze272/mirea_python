
class HTML:

    def __init__(self):
        self.resultCode = []

    class body:

        def __enter__(self):
            print("<body>")

        def __exit__(self, *args, **kwargs):
            print("</body>")

    class div:

        def __enter__(self):
            print("<div>")

        def __exit__(self, *args, **kwargs):
            print("</div>")

    def p(self, value):
        tag = "<p>" + value + "</p>"
        self.resultCode.append(tag)
        print(tag)

    def get_code(self):
        result = ''
        for item in self.resultCode:
            result += item
            result += '\n'

        return result


html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')

#print(html.get_code())
'''
html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')
print(html.get_code())
'''
'''
Результат:

<body>
    <div>
        <div>
            <p>Первая строка.</p>
            <p>Вторая строка.</p>
        </div>
        <div>
            <p>Третья строка.</p>
        </div>
    </div>
</body>
'''