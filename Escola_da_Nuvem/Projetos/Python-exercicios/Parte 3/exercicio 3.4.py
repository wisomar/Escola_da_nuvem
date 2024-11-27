def main():

# leia 4 valor inteiros A,B,C,D
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))
    C = int(input("Digite o valor de C: "))
    D = int(input("Digite o valor de D: "))

# Verifica se todas as condições são aceitas
    if A > 0 and B > 0 and C > 0 and D > 0 and A % 2 == 0 and B % 2 == 0 and C % 2 == 0 and D % 2 == 0:
        print(f"Os valores aceitos são: A = {A}, B = {B}, C = {C}, D = {D}")
    else:
        print("Os valores não são aceitos")

main()    