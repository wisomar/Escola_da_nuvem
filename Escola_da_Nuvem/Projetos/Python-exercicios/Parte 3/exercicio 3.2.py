def calcula_pedido():
    # Imprime o menu para identificar o(s) código(s) do produto(s)
    print("Escolha o produto conforme o código:\n")
    print("Código | Produto         | Preço(R$)")
    print("-------------------------------------")
    print("1     | Cachorro Quente | R$ 4.00")
    print("2     | X-Salada        | R$ 4.50")
    print("3     | X-Bacon         | R$ 5.00")
    print("4     | Torrada Simples | R$ 2.00")
    print("5     | Refrigerante    | R$ 1.50")

    # Solicita a entrada de código do produto e guarda como inteiro
    codigo = int(input("\nDigite o código do produto: "))
    
    # Verifica se código existe
    if codigo < 1 or codigo > 5:
        print("Código inválido, tente novamente!")
        return
    else:
        # Caso o código exista solicita a entrada da quantidade
        quantidade = int(input("Digite a quantidade desejada: "))
        # Verifica se a quantidade é válida
        if quantidade <= 0:
            print("Digite uma quantidade valida!")
            return
        # Caso a quantidade for válida faz o cálculo de acordo com o código do produto e sua quantidade  
        else:
            if codigo == 1:
                print(f"Total: R$ {(4.00 * quantidade):.2f}")
            elif codigo == 2:
                print(f"Total: R$ {(4.50 * quantidade):.2f}")
            elif codigo == 3:
                print(f"Total: R$ {(5.00 * quantidade):.2f}")
            elif codigo == 4:
                print(f"Total: R$ {(2.00 * quantidade):.2f}")
            elif codigo == 5:
                print(f"Total: R$ {(1.50 * quantidade):.2f}")

#Chama a função      
calcula_pedido()