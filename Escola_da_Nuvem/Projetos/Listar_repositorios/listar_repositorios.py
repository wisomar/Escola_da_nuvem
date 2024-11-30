import requests


class ListaDeRepositorios:
    """Classe para listar repositórios de um usuário do GitHub."""

    def __init__(self, usuario):
        """Inicializa a classe com o nome de usuário do GitHub."""
        self._usuario = usuario

    def requisicao_api(self):
        """Realiza uma requisição à API do GitHub para obter os repositórios do usuário."""
        try:
            resposta = requests.get(
                f'https://api.github.com/users/{self._usuario}/repos'
            )
            resposta.raise_for_status()  # Levanta uma exceção para erros HTTP
            return resposta.json()
        except requests.exceptions.RequestException as e:
            return f"Erro na requisição: {e}"

    def imprime_repositorios(self):
        """Imprime os nomes dos repositórios ou uma mensagem de erro."""
        dados_api = self.requisicao_api()

        if isinstance(dados_api, list):  # Verifica se a resposta é uma lista (JSON esperado)
            if dados_api:
                for repo in dados_api:
                    print(repo.get('name', 'Repositório sem nome'))
            else:
                print(f"O usuário {self._usuario} não possui repositórios públicos.")
        else:
            print(dados_api)


# Exemplo de uso
repositorios = ListaDeRepositorios('deysebonisegnia')
repositorios.imprime_repositorios()