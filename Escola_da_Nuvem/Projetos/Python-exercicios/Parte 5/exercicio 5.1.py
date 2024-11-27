def imprime_sequencia(n):
    for i in range (1, n + 1):

        #primeira linha
        print(f"{i} {i**2} {i**3}")
        #segunda linha
        print(f"{i} {i**2 + 1} {i**3 + 1}")
def main():
    try:
        N = int(input("Digite um número: "))
        if N < 1 or N > 1000:
            raise ValueError("N deve estar entre 1 e 1000")
        imprime_sequencia (N)
    except ValueError as ve:
        print(f"Erro: {ve}")

main()
