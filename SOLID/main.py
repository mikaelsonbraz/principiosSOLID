from SOLID.good_srp.client.GitHubClient import GitHubClient
from SOLID.good_srp.models.owner import Owner
from SOLID.good_srp.utilities.parser.parser import RepoParser
from SOLID.good_srp.utilities.reports.reports_generator import ReportsGenerator
from SOLID.good_srp.utilities.reports.markdown_generator import MarkdownGenerator
from SOLID.good_srp.utilities.reports.html_generator import HTMLGenerator

from SOLID.good_srp.models.member import Member
from SOLID.good_srp.models.manager import Manager

from SOLID.good_srp.utilities.reports.writers.writer import Writer
from SOLID.good_srp.utilities.reports.writers.html_writer import HTMLWriter
from SOLID.good_srp.utilities.reports.writers.markdown_writer import MarkdownWriter

if __name__ == '__main__':
    user = 'mikaelsonbraz'
    response = GitHubClient.get_repos_by_user(user)
    if response["status_code"] == 200:
        repos = RepoParser.parse(response["body"])
        markdown_report = ReportsGenerator.build(MarkdownGenerator, repos)
        html_report = ReportsGenerator.build(HTMLGenerator, repos)

        '''Dependency Inversion
            Criei uma classe chamada Writer que tem um método que recebe dois parâmetros:
            1 - Um writer que tenha o método save() - seja de html ou markdown
            2 - O report específico seja pra html ou markdown
            Obedecendo o Open/Closed Principle de novo as classes também estão abertas apenas para extensão
        '''
        Writer.write(MarkdownWriter, markdown_report)
        Writer.write(HTMLWriter, html_report)

    else:
        print(response["body"])

    """Aplicando o principio de Liskov Substitution agora as heranças e abstrações estão corrretas
    Manager herda de User
    Member e Owner herda de Developer que herda de User"""

    member = Member(user, "memberTest@test.com")
    owner = Owner(user, "ownerTest@test.com")
    manager = Manager(user, "managerTest@test.com")

    print(member.getUsername, owner.getUsername, manager.getUsername)
    print(member.members())
    print(owner.members())
    print("O member está trabalhando: " + member.work())
    print("O owner está trabalhando: " + owner.work())
    print("O manager está trabalhando: " + manager.work())


