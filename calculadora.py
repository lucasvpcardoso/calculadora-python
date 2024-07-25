def calculadora():
    while True:
        print()
        print("Calculadora Simples")
        print()
        print("1 PARA SOMAR")
        print("2 PARA SUBTRAIR")
        print("3 PARA MUTLIPLICAR")
        print("4 PARA DIVIDIR")
        print("S PARA SAIR")

        operacao = input("Selecione uma opção ou 's' para sair:")
        if operacao == 's' or operacao == 'S':
            print("Obrigado por utilizar a calculadora :)")
            break

        if operacao not in ['1', '2', '3', '4']:
           print("Opção inválida, tente novamente.")
           continue

        numero_1 = float(input("Digite o primeiro número: "))
        numero_2 = float(input("Digite o segundo número: "))

        if operacao == '1':
            resultado = numero_1 + numero_2
            print("o resultado da operação é: ", resultado)

        elif operacao == '2':
            resultado = numero_1 - numero_2
            print("o resultado da operação é: ", resultado)

        elif operacao == '3':
            resultado = numero_1 * numero_2
            print("o resultado da operação é: ", resultado)

        else:
            if numero_2 == 0:
                print("Divisões por 0 não são possíveis")
                continue
            else:
                resultado = numero_1 / numero_2
                print("o resultado da operação é: ", resultado)

calculadora()