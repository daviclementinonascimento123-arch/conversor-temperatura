# --- Funções de Conversão ---

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# --- Função de Suporte para Entrada de Dados ---

def ler_temperatura(mensagem):
    """Garante que a entrada do usuário seja um valor numérico válido."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Por favor, digite um número válido.")

# --- Programa Principal ---

def main():
    while True:
        print("\n" + "="*36)
        print("     CONVERSOR DE TEMPERATURA")
        print("="*36)
        print("1 - Celsius para Fahrenheit")
        print("2 - Celsius para Kelvin")
        print("3 - Fahrenheit para Celsius")
        print("4 - Fahrenheit para Kelvin")
        print("5 - Kelvin para Celsius")
        print("6 - Kelvin para Fahrenheit")
        print("0 - Sair")
        print("="*36)

        opcao = input("Escolha uma opção (0 a 6): ").strip()

        if opcao == '0':
            print("\nPrograma encerrado. Até mais!")
            break

        if opcao not in ['1', '2', '3', '4', '5', '6']:
            print("\nOpção inválida! Escolha um número de 0 a 6.")
            continue

        temp = ler_temperatura("\nDigite o valor da temperatura a converter: ")

        if opcao == '1':
            resultado = celsius_para_fahrenheit(temp)
            print(f"\nResultado: {temp:.2f}°C = {resultado:.2f}°F")
        elif opcao == '2':
            resultado = celsius_para_kelvin(temp)
            print(f"\nResultado: {temp:.2f}°C = {resultado:.2f} K")
        elif opcao == '3':
            resultado = fahrenheit_para_celsius(temp)
            print(f"\nResultado: {temp:.2f}°F = {resultado:.2f}°C")
        elif opcao == '4':
            resultado = fahrenheit_para_kelvin(temp)
            print(f"\nResultado: {temp:.2f}°F = {resultado:.2f} K")
        elif opcao == '5':
            resultado = kelvin_para_celsius(temp)
            print(f"\nResultado: {temp:.2f} K = {resultado:.2f}°C")
        elif opcao == '6':
            resultado = kelvin_para_fahrenheit(temp)
            print(f"\nResultado: {temp:.2f} K = {resultado:.2f}°F")

if __name__ == "__main__":
    main()