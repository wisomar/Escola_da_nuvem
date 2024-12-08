import requests
import boto3
import json

# Configuração do Bedrock
def criar_cliente_bedrock():
    try:
        # Defina a região diretamente no cliente
        client = boto3.client('bedrock-runtime', region_name='us-east-1')
        return client
    except Exception as e:
        print(f"Erro ao criar cliente Bedrock: {e}")
        return None

def gerar_resposta_bedrock(cliente_bedrock, modelo_id, input_text):
    try:
        # Modificando contentType para 'application/json'
        response = cliente_bedrock.invoke_model(
            modelId=modelo_id,
            contentType='application/json',
            accept='application/json',
            body=json.dumps({"inputText": input_text})  # Passando a chave 'inputText'
        )
        resultado = json.loads(response['body'].read())
        return resultado.get('output', 'Sem resposta do modelo.')
    except Exception as e:
        print(f"Erro ao invocar o modelo Bedrock: {e}")
        return "Erro ao processar a solicitação."

# Função para consultar informações do CEP
def consultar_cep(cep):
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)

        if response.status_code == 200:
            dados_cep = response.json()

            if "erro" not in dados_cep:
                return dados_cep
            else:
                print("CEP não encontrado.")
        else:
            print(f"Erro ao consultar o CEP. Código de status: {response.status_code}")
    except Exception as e:
        print(f"Ocorreu um erro ao consultar o CEP: {e}")
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
                for i, ano in enumerate(anos, 1):  # Exibe o índice junto com o ano
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
def listar_precos(tipo_veiculo, codigo_marca, codigo_modelo, codigo_ano):
    try:
        url = f"https://parallelum.com.br/fipe/api/v1/{tipo_veiculo}/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos/{codigo_ano}"
        print(f"URL gerada: {url}")  # Verifica a URL gerada para facilitar o diagnóstico

        response = requests.get(url)

        if response.status_code == 200:
            preco = response.json()  # Aqui é o dado retornado pela API

            # Verificando a estrutura do objeto de resposta para acessar os preços
            if isinstance(preco, dict) and 'Valor' in preco:  # Preço único
                # Exibe as informações adicionais
                print("\nInformações do veículo:")
                print(f"Preço: {preco['Valor']}")
                print(f"Marca: {preco['Marca']}")
                print(f"Modelo: {preco['Modelo']}")
                print(f"Ano Modelo: {preco['AnoModelo']}")
                print(f"Combustível: {preco['Combustivel']}")
                print(f"Código FIPE: {preco['CodigoFipe']}")
                print(f"Mês de referência: {preco['MesReferencia']}")
            else:
                print("Estrutura de dados inesperada para preços.")
        else:
            print(f"Erro ao consultar os preços. Código de status: {response.status_code}, URL: {url}")
    except Exception as e:
        print(f"Ocorreu um erro ao consultar os preços: {e}")

# Função principal
def main():
    print("Consulta de CEP e Marcas de Veículos na Tabela Fipe")

    # Configuração Bedrock
    cliente_bedrock = criar_cliente_bedrock()
    modelo_id = "amazon.titan-text-premier-v1:0"  # Modelo atualizado

    # Consulta de CEP
    cep = input("Digite o CEP para consulta: ").strip()
    dados_cep = consultar_cep(cep)

    # Consulta de veículos
    tipo_veiculo = input("\nDigite o tipo de veículo (carros, motos, caminhões) ou deixe em branco para 'carros': ").strip().lower() or 'carros'
    marcas = listar_marcas(tipo_veiculo)

    if marcas:
        codigo_marca = input("Digite o código da marca desejada: ")
        modelos = listar_modelos(tipo_veiculo, codigo_marca)

        if modelos:
            codigo_modelo = input("Digite o código do modelo desejado: ")
            anos = listar_anos(tipo_veiculo, codigo_marca, codigo_modelo)

            if anos:
                # Solicita ao usuário que insira o número do ano desejado
                try:
                    escolha = int(input("\nDigite o número do ano desejado: "))
                    if 1 <= escolha <= len(anos):
                        codigo_ano = anos[escolha - 1]['codigo']  # Seleciona o código do ano com base na escolha
                        listar_precos(tipo_veiculo, codigo_marca, codigo_modelo, codigo_ano)

                        # Criando o prompt para Bedrock
                        if dados_cep and cliente_bedrock:
                            input_text = (
                                f"Me dê informações sobre serviços relacionados a veículos na região do CEP {cep}, "
                                f"para o veículo: Tipo: {tipo_veiculo}, Marca: {codigo_marca}, Modelo: {codigo_modelo}, "
                                f"Ano: {codigo_ano}. "
                                "Por favor, forneça os serviços disponíveis, incluindo endereço e telefone na região."
                            )
                            resposta = gerar_resposta_bedrock(cliente_bedrock, modelo_id, input_text)
                            print("\nServiços sugeridos na região do CEP {} para o seu veículo:".format(cep))
                            print(resposta)
                    else:
                        print("Escolha inválida. Por favor, escolha um número dentro da lista.")
                except ValueError:
                    print("Valor inválido. Por favor, insira um número.")

if __name__ == "__main__":
    main()
