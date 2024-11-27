def main():
    maior_valor = None
    posicao_maior = 0
    
    for i in range(1,5):
        valor = int(input())
        if maior_valor is None or valor > maior_valor:
            maior_valor = valor
            posicao_maior = i
    print(maior_valor)
    print(posicao_maior)

main()

