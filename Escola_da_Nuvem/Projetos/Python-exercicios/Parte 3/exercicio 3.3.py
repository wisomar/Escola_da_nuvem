def main():
    
    # Ler o salario atual do funcionario
    print("Digite o valor do seu salario atual: ")
    salario_atual = float(input())

    # Definição dos ajustes (de Acordo com faixa salarial)

    if salario_atual <= 400.00:
        percentual = 15
    elif salario_atual <= 800.00:
        percentual = 12
    elif salario_atual <= 1200.00:
        percentual = 10
    elif salario_atual <= 2000.00:
        percentual = 7
    else:
        percentual = 4

    reajuste = salario_atual * (percentual / 100)
    novo_salario = salario_atual + reajuste

    # Mostrar o calculo do novo salario

    print(f"O novo salario é: {novo_salario:.2f}")
    print(f"O percentual de reajuste foi de: {percentual}%")
    print(f"O valor do reajuste foi de: {reajuste:.2f}")

main()

