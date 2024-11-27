# Calculo area do circulo

def areacirculo():
    PI = 3.14159

    raio = float(input()) #le o valor do raio - ponto flutuante

    area = PI * (raio ** 2)

    # imprimi a saida
    print(f"A={area:.4f}")

if __name__ == "__main__":
    areacirculo()