# Salario

def calcula_salario():
    codigo_funcionario = int(input("Escreva o código do funcionário: "))
    horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
    valor_horas = float(input("Digite o valor hora: "))

    salario = horas_trabalhadas * valor_horas

    print(f"NUMERO = {codigo_funcionario}")
    print(f"SALARIO = R$ {salario:.2f}")  

if __name__ == "__main__":
    calcula_salario()  
