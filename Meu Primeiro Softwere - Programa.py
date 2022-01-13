#Apresenta uma Tela de Boas-Vindas
print("="*40)
print("Seja Bem-Vindo a nossa loja: Mundo Vida Natural!")
print("Nossa tabela de produtos está dividida em...")
print("1 - Ervas")
print("2 - Cosméticos Naturais")
print("3 - Remédios Naturais")
print("4 - Temperos")
print("5 - Entre Outros...")
print("="*40)

print("Informe qual produto você procura...")
#A Estrutura a Qual o Programa vai dar Loop
infor = 0

#A Estrutura de Repetição das Compras
total_1 = 0
total_2 = 0
total_3 = 0
total_4 = 0
total_5 = 0

#Enquanto Não Chegar a 6 não sai do Loop
while infor != 6:
    print("=" * 40)
    print("""=== Tabela de Compras ===
            \nErvas[1] \nCosméticos[2] 
            \rRemedios[3] \nTemperos[4] \nOutros[5] 
            \nAperte 6 para Sair ou Para Finalizar a Compra > [6]""")
    infor = int(input("Selecione uma opção: "))
    print("=" * 40)

    if infor == 1:
#Compra de Ervas
        print("=" * 40)
        print("1 - Erva Doce: 50g por R$ 2,00 ")
        print("2 - Erva Cidreira: 50g por R$ 2,50")
        print("3 - Camomila: 50g por R$ 3,00")

        print('''\n[1] Para Comprar > Erva Doce 
                \r[2] Para Comprar > Erva Cidreira
                \r[3] Para Comprar > Camomila''')

        compra = int(input("Selecione um Número e Tecle [ENTER]: "))
        print("=" * 40)

        total_1 = total_1*1
        if compra == 1:
            total_1 += 2.00

        elif compra == 2:
            total_1 += 2.50

        elif compra == 3:
            total_1 += 3.00

    elif infor == 2:
#Compra de Cosmeticos
        print("=" * 40)
        print("\n1 - Sabonete Aloivera Natural: por R$ 3,00")
        print("2 - Mascara para Tratamento de Pele: por R$ 3,50")
        print("3 - Creme de Avelã Natural: R$ 4,50")

        print('''\n[1] Para Comprar > Sabonete Aloivera 
                \r[2] Para Comprar > Mascara Para Tratamento de Pele
                \r[3] Para Comprar > Creme de Avelã''')

        compra = int(input("Selecione um Número e Tecle [ENTER]: "))
        print("=" * 40)

        total_2 = total_2*1
        if compra == 1:
            total_2 += 3.00

        elif compra == 2:
            total_2 += 3.50

        elif compra == 3:
            total_2 += 4.50

    elif infor == 3:
#Compra de Remédios
        print("=" * 40)
        print("1 - Olho de Cocó Natural: por R$ 23,50")
        print("2 - Magnésio: por R$ 45,00")
        print("3 - Omega 3: por R$ 50,00")

        print('''\n[1] Para Comprar > Olho de Cocó Natural
                \r[2] Para Comprar > Magnésio
                \r[3] Para Comprar > Omega 3''')

        compra = int(input("Selecione um Número e Tecle [ENTER]: "))
        print("=" * 40)

        total_3 = total_3*1
        if compra == 1:
            total_3 += 23.50

        elif compra == 2:
            total_3 += 45.50

        elif compra == 3:
            total_3 += 50.00


    elif infor == 4:
#Compra de Temperos
        print("=" * 40)
        print("\n1 - Salsinha: por R$ 2,50")
        print("2 - Açafrão da Terra: por R$ 3,00")
        print("3 - Chimichurri: por R$ 3,50")

        print('''\n[1] Para Comprar > Salsinha 
                        \r[2] Para Comprar > Açafrão da Terra
                        \r[3] Para Comprar > Chimichurri''')

        compra = int(input("Selecione um Número e Tecle [ENTER]: "))
        print("=" * 40)

        total_4 = total_4*1
        if compra == 1:
            total_4 += 2.50

        elif compra == 2:
            total_4 += 3.00

        elif compra == 3:
            total_4 += 3.50

    elif infor == 5:
#Compra de outros Itens
        print("=" * 40)
        print("\n1 - Livro de Culinária Saúde e Bem Estar: por R$ 36,90")
        print("2 - Livro de Mil e Uma Receitas para Sucos e Chás Naturais: por R$ 42,50")
        print("3 - Serie Completa de DVDs com Mini-curso de Culinária Natural: por R$ 50,00")

        print('''\n[1] Para Comprar > Livro de Culinária 
                        \r[2] Para Comprar > Livro de Sucos
                        \r[3] Para Comprar > DVD de Cursos de Culinaria''')

        compra = int(input("Selecione um Número e Tecle [ENTER]: "))
        print("=" * 40)

        total_5 = total_5*1
        if compra == 1:
            total_5 += 36.90

        elif compra == 2:
            total_5 += 42.50

        elif compra == 3:
            total_5 += 50.00

#Aqui é mostrado o Resultado da Compra
    else:

        totalf = total_1+total_2+total_3+total_4+total_5

        if totalf >= 20:
            desconto = totalf - (totalf*5/100)
            print("O Total foi de R$ {:.2f} \nCom o desconto de 5% o total fica de R$ {:.2f}".format(totalf, desconto))
        else:
            print("O Total da sua compra é de: R$ {:.2f}".format(totalf))
        print("\nObrigado por nos visitar!")
