import boto3
from botocore.exceptions import ClientError

# Criar o Bedrock Runtime client na região AWS de uso.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Setar ID do modelo, exemplo: Titan Text Premier.
model_id = "amazon.titan-text-premier-v1:0"

def start_conversation():
    print("Iniciando diálogo. Digite 'sair' para encerrar.")
    
    while True:
        # Ler a mensagem do usuário
        user_message = input("curioso: ")
        
        # Condição para sair do loop
        if user_message.lower() == "sair":
            print("Encerrando o diálogo.")
            break

        # Estruturar a conversa
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

            # Extrair e printar a resposta.
            response_text = response["output"]["message"]["content"][0]["text"]
            print(f"fofoqueiro: {response_text}")

        except (ClientError, Exception) as e:
            print(f"ERRO: Falha na chamada '{model_id}'. Erro: {e}")
            break

if __name__ == "__main__":
    start_conversation()