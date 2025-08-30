import datetime

def cadastrar_consulta():
    print("--------------------------------")
    print("        DATAS DISPONÍVEIS       ")
    print("--------------------------------")

    escolha = int(input("DIGITE A DATA ESCOLHIDA DE 1 ATÉ 5 " 
                        "\n1- 28/05 as 15h20 " \
                        "\n2- 03-06 as 10h15 " \
                        "\n3- 07/06 as 19h20 " \
                        "\n4- 11/06 as 8h10 " \
                        "\n5- 17/06 as 10h10 \n----------------------------\nDIGITE: "))

    match(escolha):
        case 1:
            data_consulta = datetime.datetime(2025, 5, 28, 15, 20)
            print("Sua consulta foi agendada para o dia 28/05 AS 15:20 DA TARDE!")
        case 2:
            data_consulta = datetime.datetime(2025, 6, 3, 10, 15)
            print("Sua consulta foi agendada para o dia 03/06 AS 10:15 DA MANHÃ!")
        case 3:
            data_consulta = datetime.datetime(2025, 6, 7, 19, 20)
            print("Sua consulta foi agendada para o dia 07/06 AS 19:10 DA NOITE!")
        case 4:
            data_consulta = datetime.datetime(2025, 6, 11, 8, 10)
            print("Sua consulta foi agendada para o dia 11/06 AS 08:10 DA MANHÃ!")
        case 5:
            data_consulta = datetime.datetime(2025, 6, 17, 10, 10)
            print("Sua consulta foi agendada para o dia 17/06 AS 10:10 DA MANHÃ!")

def cadastrar_faq():
    email = input("\nDigite o seu e-mail: ")
    duvida = input("Digite a sua dúvida: ")
    print("\nSua dúvida foi cadastrada! Você receberá uma resposta no e-mail em breve. Hospital das Clinicas agradece!")

print("\n-----------------------------")
print("          IMREA Hc           ")
print("-----------------------------")
print("1 - Cadastrar Usuário")
print("2 - Sair")
print("-----------------------------")

escolha = int(input("Escolha: "))

if int(escolha) == 1:

    nome = input("\nDigite o seu NOME: ")
    cpf = input("Digite o seu CPF: ")
    genero = (input("Digite o seu GENERO (M/F): "))
    estado_civil = input("Digite o seu ESTADO CIVIL: ")
    dia_nasc = int(input("Digite o DIA em que você nasceu: "))
    mes_nasc = int(input("Digite o MÊS em que você nasceu: "))
    ano_nasc = int(input("Digite o ANO em que você nasceu: "))

    data_nasc = datetime.datetime(ano_nasc, mes_nasc, dia_nasc)


    print("\n---------------------------------------------")
    print("            Cadastrado com sucesso!            ")
    print("---------------------------------------------")
    print("                     MENU           ")
    print("                 1= CONSULTAS           ")
    print("                 2= AGENDAMENTO         ")
    print("                 3= FAQ                 ")
    print("---------------------------------------------")

    escolha = int(input("Escolha: "))

    match escolha:
        case 1:
            print("\n----------------------------------------------------------------")
            print("      Nenhuma consulta agendada! Deseja realizar um agendamento? ")
            print("                            1= Sim                      ")
            print("                            2= Sair                      ")
            print("----------------------------------------------------------------")
            
            escolha = int(input("Digite:"))
            if escolha == 1:
                # Função de agendar uma consulta
                cadastrar_consulta()
            else:
                print("\nObrigado por usar nosso aplicativo!")
        case 2:
            # Função de agendar consulta
            cadastrar_consulta()

        case 3:
            #Função de FAQ
            cadastrar_faq()

else:
    print("\nVocê saiu do programa! Obrigado por usar nosso aplicativo.")    