from SOLID.good_srp.client.GitHubClient import GitHubClient
from SOLID.good_srp.utilities.parser.parser import RepoParser
from SOLID.good_srp.utilities.reports.reports_generator import ReportsGenerator

if __name__ == '__main__':
    user = 'mikaelsonbraz'
    response = GitHubClient.get_repos_by_user(user)
    if response["status_code"] == 200:
        repos = RepoParser.parse(response["body"])
        markdown_report = ReportsGenerator.build("md", repos)
        html_report = ReportsGenerator.build("html", repos)

        print(markdown_report)
        print(html_report)
    else:
        print(response["body"])


