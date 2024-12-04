import boto3
from botocore.exceptions import ClientError

def pesquisar_erro_no_bedrock(mensagem_erro):
    # Criar o Bedrock Runtime client na região AWS de uso.
    client = boto3.client("bedrock-runtime", region_name="us-east-1")
    
    # Setar ID do modelo, exemplo: Titan Text Premier.
    model_id = "amazon.titan-text-premier-v1:0"
    
    # Configurar a mensagem do usuário.
    conversation = [
        {
            "role": "user",
            "content": [{"text": f"Explique o seguinte erro em Python, em português: {mensagem_erro}"}],
        }
    ]
    
    try:
        # Enviar a mensagem para o modelo, usando a inferência do modelo.
        response = client.converse(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
        )
        
        # Extrair e retornar a resposta.
        response_text = response["output"]["message"]["content"][0]["text"]
        return response_text
    except (ClientError, Exception) as e:
        return f"ERRO: Falha na chamada ao '{model_id}'. Detalhes do erro: {e}"

def main():
    N = int(input("Digite o numero de pares de valores: "))
    if N < 1:
        raise ValueError("Numero de pares - valores (N) deve ser maior que zero")
    for _ in range(N):
        try:
            X, Y = map(int, input("Digite os valores de X e Y separados por espaço: ").split())
            if Y == 0:
                print("Divisão impossível")
            else:
                resultado = X / Y
                print(f"{resultado:.1f}")
        except ValueError as ve:
            print(f"Erro: {ve}")
            resposta_bedrock = pesquisar_erro_no_bedrock(str(ve))
            print(f"Ajuda do Bedrock: {resposta_bedrock}")
        except Exception as e:
            print(f"Erro inesperado: {e}")
            resposta_bedrock = pesquisar_erro_no_bedrock(str(e))
            print(f"Ajuda do Bedrock: {resposta_bedrock}")

if __name__ == "__main__":
    main()