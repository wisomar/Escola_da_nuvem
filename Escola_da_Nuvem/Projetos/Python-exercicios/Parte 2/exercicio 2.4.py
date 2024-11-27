def calcular_valor_total_pecas():
    # Ler o numero de peças : peça 1

    codigo_peca1, quantidade_peca1, valor_unitario_peca1 = input("Digite o codigo e quantidade e valor da primeira peça, separados por espaço: ").split()
    codigo_peca1 = int(codigo_peca1)
    quantidade_peca1 = int(quantidade_peca1)
    valor_unitario_peca1 = float(valor_unitario_peca1)

    # Ler o numero de peças: peça 2
    codigo_peca2, quantidade_peca2, valor_unitario_peca2 = input("Digite o codigo e quantidade e valor da primeira peça, separados por espaço: ").split()
    codigo_peca2 = int(codigo_peca2)
    quantidade_peca2 = int(quantidade_peca2)
    valor_unitario_peca2= float(valor_unitario_peca2)

    # Calcular o valor total a ser pago
    valor_total = (quantidade_peca1 * valor_unitario_peca1) + (quantidade_peca2 * valor_unitario_peca2)

    # Mostre o valor final
    print(f"Valor total a pagar: R$ {valor_total:.2f}")

if __name__ == "__main__":
    calcular_valor_total_pecas()