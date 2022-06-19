from SOLID.good_srp.client.GitHubClient import GitHubClient
from SOLID.good_srp.utilities.parser.parser import RepoParser
from SOLID.good_srp.utilities.reports.reports_generator import ReportsGenerator
from SOLID.good_srp.utilities.reports.markdown_generator import MarkdownGenerator
from SOLID.good_srp.utilities.reports.html_generator import HTMLGenerator

if __name__ == '__main__':
    user = 'mikaelsonbraz'
    response = GitHubClient.get_repos_by_user(user)
    if response["status_code"] == 200:
        repos = RepoParser.parse(response["body"])
        markdown_report = ReportsGenerator.build(MarkdownGenerator, repos)
        html_report = ReportsGenerator.build(HTMLGenerator, repos)

        with open(r'C:\Users\mikae\PycharmProjects\principiosSolid\SOLID\good_srp\utilities\reports\markdown_reports\markdown_report.md',
                  mode="w", encoding="UTF-8") as arquivo_md:
            arquivo_md.write(markdown_report)
        arquivo_md.close()

        with open(r'C:\Users\mikae\PycharmProjects\principiosSolid\SOLID\good_srp\utilities\reports\html_reports\html_report.html',
                  mode="w", encoding="UTF-8") as arquivo_html:
            arquivo_html.write(html_report)
        arquivo_html.close()

    else:
        print(response["body"])


