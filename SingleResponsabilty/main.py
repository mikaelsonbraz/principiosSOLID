from SingleResponsabilty.good_srp.client.GitHubClient import GitHubClient
from SingleResponsabilty.good_srp.utilities.Parser import RepoParser

if __name__ == '__main__':
    user = 'mikaelsonbraz'
    response = GitHubClient.get_repos_by_user(user)
    RepoParser.parse(response["body"]) if response["status_code"] == 200 else print(response["body"])
