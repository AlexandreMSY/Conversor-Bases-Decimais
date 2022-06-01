while True:

    opcao = int(input(
        "1 - Binario para decimal" + "\n"
        "2 - Octadecimal para decimal" + "\n"   
        "3 - Hexadecimal para decimal" + "\n"
        "4 - Sair" + "\n"

        "Selecione : "
    ))

    if opcao == 1:
        
        binario = int(input("Numero em binário > "))
        menu = binario #Guarda o valor entrado pelo usuário para ser mostrado no menu abaixo.
        numero = 0
        expoente = 0
        soma = 0

        while binario: #Loop termina quando a variável "binario" for igual a 0.

            numero = binario % 10       # Separa cada numero da variável "binario".
            binario = int(binario / 10)  
            soma += numero * 2 ** expoente
            expoente += 1

        print(
        "====================================" + "\n"
        f"Binario: {menu}" + "\n"
        f"Decimal: {soma}" + "\n"
        f"{menu} para decimal é {soma}" + "\n"
        "===================================="
        )
    
    elif opcao == 2:

        octa = int(input("Numero em octadecimal > "))
        menu = octa
        numero = 0
        expoente = 0
        soma = 0

        while octa:

            numero = octa % 10
            octa = int(octa // 10)
            soma += numero * 8 ** expoente
            expoente += 1

        print(
            "====================================" + "\n"
            f"Octadecimal: {menu}" + "\n"
            f"Decimal: {soma}" + "\n"
            f"{menu} para decimal é {soma}" + "\n"
            "===================================="
        )
    
    elif opcao == 3:

        hexa = str(input("Numero em hexadecimal > "))
        menu = hexa
        expoente = 0
        numero = 0
        soma = 0
        contador = 0

        for item in hexa:

            contador = contador + 1      #Esse loop conta quantos caracteres a variável "hexa" possui. Equivalente a função len().
            
        contador = contador - 1

        while contador >= 0:  #Esse loop verifica se a variável "hexa" possui certos caracteres pelo índice.

            if hexa[contador] >= "A" and hexa[contador] <= "F" or hexa[contador] >= "a" and hexa[contador] <= "f":      
                
                if hexa[contador] == "A" or hexa[contador] == "a":      
                    numero = 10
                
                elif hexa[contador] == "B" or hexa[contador] == "b":             
                    numero = 11
                
                elif hexa[contador] == "C" or hexa[contador] == "c":
                    numero = 12
                
                elif hexa[contador] == "D" or hexa[contador] == "d":
                    numero = 13
                
                elif hexa[contador] == "E" or hexa[contador] == "e":
                    numero = 14
                
                else:
                    numero = 15

            elif hexa[contador] >= "0" and hexa[contador] <= "9":
                numero = int(hexa[contador])

            soma += numero * 16 ** expoente
            
            contador -= 1
            expoente += 1

        print(
            "====================================" + "\n"
            f"Hexadecimal: {menu}" + "\n"
            f"Decimal: {soma}" + "\n"
            f"{menu} para decimal é {soma}" + "\n"
            "===================================="
        )

    else:
        break
