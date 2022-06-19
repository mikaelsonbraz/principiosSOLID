import requests
'''
Essa classe não segue o principio de responsabilidade unica
Ela tem duas responsabilidades: fazer requisições a API do github e gerar um relatorio simples
'''

class listRepositories():

    API_BASE_URL = 'https://api.github.com'

    def __init__(self, user):
        self._user = user

    def get_repos_by_user(self) -> dict:
        response = requests.get(f'{self.API_BASE_URL}/users/{self._user}/repos')
        return {"status_code": response.status_code,
                "body": response.json() if response.status_code == 200 else "Error while getting repos"}

    def parse_response(self):
        response = self.get_repos_by_user()
        body = response['body']
        if response['status_code'] == 200:
            for i in range(len(body)):
                print(f'{body[i]["id"]} - {body[i]["name"]} - {body[i]["stargazers_count"]}')



print(listRepositories('mikaelsonbraz').parse_response())
