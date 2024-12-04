import requests
import boto3
from botocore.exceptions import ClientError

# URL base do ViaCEP
BASE_URL = "https://viacep.com.br/ws/"

# Função para obter o endereço a partir do CEP
def obter_endereco(cep: str) -> dict:
    """
    Faz uma requisição à API do ViaCEP para obter informações de endereço
    com base no CEP fornecido.
    
    Args:
        cep (str): O CEP para o qual deseja buscar o endereço.
    
    Returns:
        dict: Um dicionário contendo as informações do endereço, ou um
        dicionário com o erro gerado pelo Bedrock se a requisição falhar.
    """
    try:
        # Chama a API do ViaCEP com o CEP fornecido
        resposta = requests.get(f"{BASE_URL}{cep}/json", timeout=30)
        resposta.raise_for_status()  # Levanta exceção se o status não for 200
        return resposta.json()
    except requests.RequestException as e:
        print(f"Erro ao obter o endereço: {e}")
        # Em caso de erro, chama a API do Amazon Titan Text
        return chamar_bedrock(f"Erro ao tentar acessar o CEP {cep} no ViaCEP: {e}")

# Função para chamar a API do Amazon Titan Text
def chamar_bedrock(mensagem: str) -> dict:
    """
    Chama a API de conversação da Amazon Bedrock (Titan Text) para obter uma resposta alternativa.
    
    Args:
        mensagem (str): A mensagem que será enviada ao modelo Bedrock para fornecer uma explicação detalhada.
    
    Returns:
        dict: Resposta gerada pela API do Bedrock, explicando o erro ocorrido.
    """
    # Criar o Bedrock Runtime client na região AWS de uso.
    client = boto3.client("bedrock-runtime", region_name="us-east-1")

    # Setar ID do modelo, exemplo: Titan Text Premier.
    model_id = "amazon.titan-text-premier-v1:0"

    # Preparando a mensagem de erro
    user_message = f"Estou tendo o seguinte problema: {mensagem}. Pode me explicar o que pode ter ocorrido?"

    conversation = [
        {
            "role": "user",
            "content": [{"text": user_message}],
        }
    ]

    try:
        # Enviar a mensagem para o modelo, usando a inferência do modelo.
        response = client.converse(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
        )

        # Extrair e retornar a resposta do modelo
        response_text = response["output"]["message"]["content"][0]["text"]
        return {"erro": response_text}
    
    except (ClientError, Exception) as e:
        print(f"ERRO: Falha na chamada '{model_id}'. Erro: {e}")
        return {"erro": "Falha ao tentar obter resposta do Bedrock."}

# Exemplo de uso
print(obter_endereco("1480r0600"))