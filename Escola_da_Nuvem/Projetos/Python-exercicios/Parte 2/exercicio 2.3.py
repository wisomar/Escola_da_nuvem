def calcular_salario_vendedor():
    nome = input("Digite o nome do vendedor: ")
    salario_base = float(input("Digite o salario fixo: "))
    total_vendas = float(input("Digite o total em vendas: "))

    comissao = total_vendas * 0.15

    salario_total = salario_base + comissao

    print(f"O salario do vendedor {nome} é R$ {salario_total:.2f}")

if __name__ == "__main__":
    calcular_salario_vendedor()