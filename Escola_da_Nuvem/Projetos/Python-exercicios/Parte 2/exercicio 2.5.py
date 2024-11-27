# Cálculo

def calculo():
    try:
        # Coordenada ponto 1
        print("Entre com o valor do ponto 1 (exemplo: 3 4):")
        x1, y1 = map(float, input().split())  # Converte as duas entradas para float
        # Coordenada ponto 2
        print("Entre com o valor do ponto 2 (exemplo: 5 6):")
        x2, y2 = map(float, input().split())  # Converte as duas entradas para float

        # Cálculo da distância
        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 

        # Exibir a distância segundo a fórmula
        print(f"A distância é igual a: {distancia:.4f}")
    except ValueError:
        print("Erro: Certifique-se de que está digitando dois números separados por espaço.")
    
if __name__ == "__main__":
    calculo()
