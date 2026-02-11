# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("Erro: divisão por zero não é permitida.")
        exit()
else:
    print("Operação inválida.")
    exit()

print(f"O resultado da operação {operacao} entre {numero1} e {numero2} é: {resultado}")