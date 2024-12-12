import requests
import boto3
from botocore.exceptions import ClientError

# Configuração do Bedrock
client = boto3.client("bedrock-runtime", region_name="us-east-1")
model_id = "amazon.titan-text-premier-v1:0"

# Função para consultar endereço a partir do CEP
def consultar_endereco(cep):
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        if response.status_code == 200:
            endereco = response.json()
            if "erro" in endereco:
                print("CEP não encontrado. Verifique e tente novamente.")
                return None
            else:
                print("\nEndereço encontrado:")
                print(f"Logradouro: {endereco.get('logradouro', 'N/A')}")
                print(f"Bairro: {endereco.get('bairro', 'N/A')}")
                print(f"Cidade: {endereco.get('localidade', 'N/A')}")
                print(f"Estado: {endereco.get('uf', 'N/A')}")
                return endereco
        else:
            print(f"Erro ao consultar o endereço. Código de status: {response.status_code}")
    except Exception as e:
        print(f"Ocorreu um erro ao consultar o endereço: {e}")
    return None

# Função para listar as marcas de veículos
def listar_marcas(tipo_veiculo=None):
    try:
        url = f"https://parallelum.com.br/fipe/api/v1/{tipo_veiculo}/marcas" if tipo_veiculo else "https://parallelum.com.br/fipe/api/v1/carros/marcas"

        response = requests.get(url)
        if response.status_code == 200:
            marcas = response.json()
            if marcas:
                print("\nMarcas de veículos:")
                for marca in marcas:
                    print(f"Código: {marca['codigo']}, Nome: {marca['nome']}")
                return marcas
            else:
                print("Nenhuma marca encontrada.")
        else:
            print(f"Erro ao consultar a API. Código de status: {response.status_code}")
    except Exception as e:
        print(f"Ocorreu um erro ao consultar as marcas: {e}")
    return []

# Função para listar os modelos de um veículo baseado na marca
def listar_modelos(tipo_veiculo, codigo_marca):
    try:
        url = f"https://parallelum.com.br/fipe/api/v1/{tipo_veiculo}/marcas/{codigo_marca}/modelos"
        response = requests.get(url)
        if response.status_code == 200:
            modelos = response.json().get('modelos', [])
            if modelos:
                print("\nModelos disponíveis:")
                for modelo in modelos:
                    print(f"Código: {modelo['codigo']}, Nome: {modelo['nome']}")
                return modelos
            else:
                print("Nenhum modelo encontrado.")
        else:
            print(f"Erro ao consultar os modelos. Código de status: {response.status_code}")
    except Exception as e:
        print(f"Ocorreu um erro ao consultar os modelos: {e}")
    return []

# Função para listar os anos de um modelo
def listar_anos(tipo_veiculo, codigo_marca, codigo_modelo):
    try:
        url = f"https://parallelum.com.br/fipe/api/v1/{tipo_veiculo}/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos"
        response = requests.get(url)
        if response.status_code == 200:
            anos = response.json()
            if anos:
                print("\nAnos disponíveis:")
                for i, ano in enumerate(anos, 1):
                    print(f"{i}. Ano: {ano['codigo']}, Descrição: {ano['nome']}")
                return anos
            else:
                print("Nenhum ano encontrado.")
        else:
            print(f"Erro ao consultar os anos. Código de status: {response.status_code}")
    except Exception as e:
        print(f"Ocorreu um erro ao consultar os anos: {e}")
    return []

# Função para listar os preços do veículo baseado no ano escolhido
def listar_precos(tipo_veiculo, codigo_marca, codigo_modelo, codigo_ano, cep):
    try:
        url = f"https://parallelum.com.br/fipe/api/v1/{tipo_veiculo}/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos/{codigo_ano}"
        response = requests.get(url)
        if response.status_code == 200:
            preco = response.json()
            if isinstance(preco, dict) and 'Valor' in preco:
                print("\nInformações do veículo:")
                print(f"Preço: {preco['Valor']}")
                print(f"Marca: {preco['Marca']}")
                print(f"Modelo: {preco['Modelo']}")
                print(f"Ano Modelo: {preco['AnoModelo']}")
                print(f"Combustível: {preco['Combustivel']}")
                print(f"Código FIPE: {preco['CodigoFipe']}")
                print(f"Mês de referência: {preco['MesReferencia']}")
                buscar_servicos_bedrock(cep, preco['Modelo'])
            else:
                print("Estrutura de dados inesperada para preços.")
        else:
            print(f"Erro ao consultar os preços. Código de status: {response.status_code}")
    except Exception as e:
        print(f"Ocorreu um erro ao consultar os preços: {e}")

# Função para buscar serviços automotivos via Bedrock
def buscar_servicos_bedrock(cep, modelo_veiculo):
    prompt = (f"Eu possuo um veículo do modelo {modelo_veiculo}. "
              f"Estou localizado no CEP {cep}, no Brasil. "
              "Por favor, responda em português e liste os principais serviços automotivos disponíveis na região com endereço e telefone")
    conversation = [{"role": "user", "content": [{"text": prompt}]}]
    try:
        response = client.converse(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
        )
        response_text = response["output"]["message"]["content"][0]["text"]
        print("\nServiços automotivos Franqueados na região do CEP:")
        print(response_text)
    except (ClientError, Exception) as e:
        print(f"Erro ao buscar serviços automotivos via Bedrock: {e}")

# Função principal
def main():
    cep = input("Por favor, informe o seu CEP: ").strip()
    if not cep.isdigit() or len(cep) != 8:
        print("CEP inválido. O programa será encerrado.")
        return

    endereco = consultar_endereco(cep)
    if not endereco:
        return

    while True:
        print("\nEscolha uma opção:")
        print("1. Carros")
        print("2. Motos")
        print("3. Caminhões")
        print("4. Sair")
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            tipo_veiculo = "carros"
        elif escolha == "2":
            tipo_veiculo = "motos"
        elif escolha == "3":
            tipo_veiculo = "caminhoes"
        elif escolha == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue

        marcas = listar_marcas(tipo_veiculo)
        if marcas:
            codigo_marca = input("Digite o código da marca desejada: ")
            modelos = listar_modelos(tipo_veiculo, codigo_marca)
            if modelos:
                codigo_modelo = input("Digite o código do modelo desejado: ")
                anos = listar_anos(tipo_veiculo, codigo_marca, codigo_modelo)
                if anos:
                    escolha_ano = int(input("Digite o número do ano desejado: "))
                    if 1 <= escolha_ano <= len(anos):
                        codigo_ano = anos[escolha_ano - 1]['codigo']
                        listar_precos(tipo_veiculo, codigo_marca, codigo_modelo, codigo_ano, cep)
                    else:
                        print("Ano selecionado inválido!")
                else:
                    print("Nenhum ano encontrado!")
            else:
                print("Nenhum modelo encontrado!")
        else:
            print("Nenhuma marca encontrada!")

if __name__ == "__main__":
    main()
