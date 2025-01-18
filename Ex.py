primeiroValor = input("Digite um valor: ")
segundoValor = input("Digite outro: ")

if primeiroValor < segundoValor:
    print(f"{str(primeiroValor)} é menor que {str(segundoValor)}")
elif primeiroValor > segundoValor:
    print(f"{str(primeiroValor)} é maior que {str(segundoValor)}")
else:
    print("Os valores são iguais!")