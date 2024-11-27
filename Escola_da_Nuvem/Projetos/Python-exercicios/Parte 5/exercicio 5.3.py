#calcular fatorial
def calcular_fatorial(n):
    #função para calculo de fatorial de numero inteiro
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    return fatorial
def main():
    try:
    #Leitura de valor inteiro
        N = int(input("Digite um numero inteiro entre 1 e 20: "))
        if N < 1 or N > 20:
            raise ValueError("O numero deve estar entre 1 e 20")
        resultado = calcular_fatorial(N)
        print(f"O fatorial de {N} é {resultado}")
    except ValueError as ve:
        print(f"Erro: {ve}")
main()    
    
        