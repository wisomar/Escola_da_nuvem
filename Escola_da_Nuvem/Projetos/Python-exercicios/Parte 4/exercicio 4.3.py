def main():
    try:
        N = int(input("Digite o numero de casos de teste: "))
        if N < 1:
            raise ValueError("Numero de casos de teste deve ser maior que zero")
        for _ in range(N):
            x = int(input("Digite o valor de x: "))
            y = int(input("Digite o valor de y: "))
            if x > y:
                x, y = y, x  # Troca x e y se x for maior que y
            soma = sum(i for i in range(x + 1, y) if i % 2 != 0)  # Soma os ímpares entre x e y
            print(soma)
    except ValueError as ve:
        print(f"erro: {ve}")
        
main()