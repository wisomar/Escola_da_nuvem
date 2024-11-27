def main():
    N = int(input("DIGITE O NUMERO DE PARES DE VALORES: "))
    if N < 1:
        raise ValueError("Numero de pares -  valores (N) deve ser maior que zero")
    for _ in range(N):
        try:
            x = int(input("Digite o valor de x: "))
            y = int(input("Digite o valor de y: "))
            if y == 0:
                print("divisão impossivel")
            else:
                Resultado = x / y
                print(f"{Resultado:.1f}")
        except ValueError:
            print("Valor invalido")
        except ValueError as ve:
            print(f"Erro: {ve}")
main()
            
