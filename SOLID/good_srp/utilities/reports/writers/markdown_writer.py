class MarkdownWriter:

    @staticmethod
    def save(report):
        with open(r'C:\Users\mikae\PycharmProjects\principiosSolid\SOLID\good_srp\utilities\reports\markdown_reports\markdown_report.md',
                  mode="w", encoding="UTF-8") as arquivo_md:
            arquivo_md.write(report)
        arquivo_md.close()