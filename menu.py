def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro! Divisão por zero."

def menu():
    while True:
        print("Escolha uma operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")
        
        opcao = input("Digite a opção: ")
        
        if opcao == "0":
            print("Saindo...")
            break
        elif opcao in ["1", "2", "3", "4"]:
            try:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
            except ValueError:
                print("Por favor, insira valores numéricos válidos.")
                continue

            if opcao == "1":
                print(f"Resultado: {somar(a, b)}")
            elif opcao == "2":
                print(f"Resultado: {subtrair(a, b)}")
            elif opcao == "3":
                print(f"Resultado: {multiplicar(a, b)}")
            elif opcao == "4":
                print(f"Resultado: {dividir(a, b)}")
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função menu para testar
menu()
