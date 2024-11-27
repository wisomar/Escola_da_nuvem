def calcular_anos(PA, PB, G1, G2):
    anos = 0
    while PA <= PB:
        PA += int(PA * (G1 / 100))
        PB += int(PB * (G2 / 100))
        anos += 1

        if anos > 100:
            return "Mais do que 1 século/100 anos"
    
    return anos

def main():
    try:
        T = int(input("Digite o numero de casos de teste: "))
        if not (1 <= T < 3000):
            raise ValueError("Numero de testes deve ser maior que zero e menor que 3000")
        
        for _ in range(T):
            valores = input("Digite PA, PB, G1, G2: ").split()
            PA, PB = int(valores[0]), int(valores[1])
            G1, G2 = float(valores[2]), float(valores[3])

            resultado = calcular_anos(PA, PB, G1, G2)

            print(resultado)
    except ValueError as ve:
        print(f"Erro: {ve}")

main()