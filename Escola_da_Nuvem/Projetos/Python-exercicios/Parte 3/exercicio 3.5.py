def main():
    # Leitura das notas N1, N2, N3, N4
    N1 = float(input("Digite a nota N1: "))
    N2 = float(input("Digite a nota N2: "))
    N3 = float(input("Digite a nota N3: "))
    N4 = float(input("Digite a nota N4: "))

    # Calcula a média conforme os pesos 2, 3, 4, 1
    media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

    # Exibir a média com uma casa decimal
    print(f"A média é: {media:.1f}")

    # Verificar a situação do aluno conforme a média
    if media >= 7.0:
        print("Situação: Aprovado")
    elif media >= 5.0:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")

    if media < 5.0:  # Somente solicitar a nota do exame se o aluno estiver reprovado
        nota_recupera = float(input("Digite a nota do exame: "))
        print(f"Nota do exame: {nota_recupera:.1f}")

        # Recalcular a média após exame
        media_final = (media + nota_recupera) / 2

        if media_final >= 5.0:
            print("Situação: Aprovado")
        else:
            print("Situação: Reprovado")
        
        print(f"Média final: {media_final:.1f}")

main()