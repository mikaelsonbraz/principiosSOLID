class HTMLWriter:

    @staticmethod
    def save(report):
        with open(r'C:\Users\mikae\PycharmProjects\principiosSolid\SOLID\good_srp\utilities\reports\html_reports\html_report.html',
                  mode="w", encoding="UTF-8") as arquivo_html:
            arquivo_html.write(report)
        arquivo_html.close()