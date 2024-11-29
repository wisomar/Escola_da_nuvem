import requests

BASE_URL = "https://viacep.com.br/ws/"

def obter_endereco(cep: str) -> dict:
    """
    Faz uma requisição à API do ViaCEP para obter informações de endereço
    com base no CEP fornecido.
    
    Args:
        cep (str): O CEP para o qual deseja buscar o endereço.
    
    Returns:
        dict: Um dicionário contendo as informações do endereço, ou um
        dicionário vazio se a requisição falhar.
    """
    try:
        # Chama a API com o CEP fornecido
        resposta = requests.get(f"{BASE_URL}{cep}/json", timeout=30)
        resposta.raise_for_status()  # Levanta exceção se o status não for 200
        return resposta.json()
    except requests.RequestException as e:
        print(f"Erro ao obter o endereço: {e}")
        return {}

def exibir_endereco(endereco: dict) -> None:
    """
    Exibe as informações do endereço de forma organizada.
    
    Args:
        endereco (dict): O dicionário contendo as informações do endereço.
    """
    if endereco:
        print("Endereço encontrado:")
        print(f"CEP: {endereco.get('cep', 'N/A')}")
        print(f"Logradouro: {endereco.get('logradouro', 'N/A')}")
        print(f"Bairro: {endereco.get('bairro', 'N/A')}")
        print(f"Cidade: {endereco.get('localidade', 'N/A')}")
        print(f"Estado: {endereco.get('uf', 'N/A')}")
    else:
        print("Nenhum endereço encontrado para o CEP informado.")

if __name__ == "__main__":
    cep_usuario = input("Digite o CEP: ")
    endereco = obter_endereco(cep_usuario)
    exibir_endereco(endereco)