class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open("output.html", "w", encoding="utf-8")

        fout.write("<html>")
        fout.write(
            '<head><meta http-equiv="content-type" content="text/html;charset=utf-8"></head>'
        )
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<img ")
            fout.write('width="201" src=%s />' % data["url"])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
