def calcular_media_idades():
    soma_idades = 0
    quantidade = 0

    while True:  
        try:
            idade = int(input("Digite a idade da pessoa: "))
            if idade < 0:
                break
            soma_idades += idade
            quantidade += 1
        except ValueError:
            print("Erro: idade inválida")
    
    if quantidade > 0:
        media_idades = soma_idades / quantidade
        return round(media_idades, 2)  
    else:
        return "Nenhuma idade válida inserida"  

def main():
    try:
        media_idades = calcular_media_idades()
        print(f"A média das idades é {media_idades}")
    except Exception as e:
        print(f"Erro: {e}")

main()