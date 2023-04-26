# Variaveis Globais
end = False
divisoria = "*" * 50

# Metodos
def menuProdutos():
    sacola = []
    flag = True
    while flag:
        menuProduto = '''Digite o produto desejado:
        1 - Pão (R$1 a unidade)
        2 - Maçã (R$0,50 a unidade)
        3 - Banana (R$0,25 a unidade)
        4 - Fechar sacola
        5 - Voltar (Limpa a sacola)
        Opção: '''
        print(divisoria)
        escolha = input(menuProduto)
        if escolha == "1":
            preco = 1.00
            quantidade = float(input("Quantos produtos deseja? "))
            total = preco * quantidade
            sacola.append(total)
        elif escolha == "2":
            preco = 0.50
            quantidade = float(input("Quantos produtos deseja? "))
            total = preco * quantidade
            sacola.append(total)
        elif escolha == "3":
            preco = 0.25
            quantidade = float(input("Quantos produtos deseja? "))
            total = preco * quantidade
            sacola.append(total)
        elif escolha == "4":
            flag = False
            return sacola
        elif escolha == "5":
            flag = False
            sacola.clear()
            sacola.append(0.0)
            return sacola
        else:
            print("Comando incorreto, favor responder com base no menu'")


def formaPagamento(total):
    pagamentoFlag = True
    prestacaoFlag = True
    confirmacaoFlag = True
    dinheiroFlag = True
    menuPagamento = '''Qual será a forma de pagamento?
    1 - Cartão de crédito (Divide até 3x com 5% juros)
    2 - Cartão de débito
    3 - Dinheiro (Permite troco)
    4 - Pix (Desconto de 10%)
    5 - Cancelar compra
    Opção: '''
    menuPrestacao = '''Deseja dividir em quantas vezes? 
    1 - 2x
    2 - 3x
    Opção: '''
    while pagamentoFlag:
        escolha = input(menuPagamento)
        if escolha == "1":
            pagamentoFlag = False
            while prestacaoFlag:
                prestacao = input(menuPrestacao)
                if prestacao == "1":
                    prestacaoFlag = False
                    juros = total * 0.05
                    total += juros
                    print("O metodo de pagamento escolhido foi Cartão de crédito, dividindo em 2x")
                    print("O valor total a pagar é de R${}".format(total))
                elif prestacao == "2":
                    prestacaoFlag = False
                    juros = (total * 0.05) * 2
                    total += juros
                    print("O metodo de pagamento escolhido foi Cartão de crédito, dividindo em 3x")
                    print("O valor total a pagar é de R${}".format(total))
                else:
                    print("Comando incorreto, favor responder com base no menu'")
        elif escolha == "2":
            pagamentoFlag = False
            print("O metodo de pagamento escolhido foi Cartão de débito")
            print("O valor total a pagar é de R${}".format(total))
        elif escolha == "3":
            pagamentoFlag = False
            while dinheiroFlag:
                dinheiro = float(input("Valor pago: "))
                if total <= dinheiro:
                    dinheiroFlag = False
                    troco = -(total - dinheiro)
                    print("O metodo de pagamento escolhido foi Dinheiro")
                    print("O valor total a pagar é de R${}, o valor pago sera de R${} e o troco sera de R${}".format(
                        total, dinheiro, +troco))
                else:
                    print("Dinheiro insuficiente, favor completar o valor")
        elif escolha == "4":
            pagamentoFlag = False
            desconto = total * 0.1
            total -= desconto
            print("O metodo de pagamento escolhido foi PIX")
            print("O valor total a pagar é de R${}".format(total))
        elif escolha == "5":
            pagamentoFlag = False
            return
        else:
            print("Comando incorreto, favor responder com base no menu'")
    while confirmacaoFlag:
        confirmacao = input("Confirmar compra? (Sim ou não) ")
        if confirmacao[0].upper() == "S":
            confirmacaoFlag = False
            print("Compra finalizada, imprimindo comprovante...")
            print("Obrigado e volte sempre!")
        elif confirmacao[0].upper() == "N":
            print("Compra cancelada")
            return
        else:
            print("Comando incorreto, favor responder 'sim' ou 'nao'")


def pagamento(sacola):
    total = 0.0
    for elemento in sacola:
        total += elemento

    print(divisoria)
    print("O valor total a pagar é de R${}".format(total))
    flag = True
    while flag:
        temCupom = input("Você possui algum cupom de desconto? (Sim ou não) ")
        if temCupom[0].upper() == "S":
            cupom = input("Insira seu cupom: ")
            if cupom == "bet365":
                promo = total * 0.1
                total -= promo
                flag = False
        elif temCupom[0].upper() == "N":
            flag = False
        else:
            print("Comando incorreto, favor responder 'sim' ou 'nao'")
    print("Então, o valor total a pagar é de R${}".format(total))
    formaPagamento(total)
    print(divisoria)


# Menu utilizado pelo funcionário
def menuUsuario():
    sacola = []
    flag = True
    menu = '''Digite a opção desejada:
    1 - Adicionar item
    2 - Finalizar compra
    Opção: '''
    while flag:
        print(divisoria)
        escolha = input(menu)
        if escolha == "1":
            sacola = menuProdutos()
        elif escolha == "2":
            flag = False
            pagamento(sacola)
        else:
            print("Comando incorreto, favor responder com base no menu'")


# Código Principal de execução do programa
while end is False:
    escolha = input("Iniciar processo com novo cliente? (Sim ou não) ")
    if escolha[0].upper() == "S":
        print("Conectando ao sistema...")
        menuUsuario()

    elif escolha[0].upper() == "N":
        print("Fechando o caixa")
        print("Até logo!")
        end = True

    else:
        print("Comando incorreto, favor responder 'sim' ou 'nao'")
