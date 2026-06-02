def exibir_menu():
    print("-+" * 10, "Loja anjos", "-+" * 10)
    print("1- camisa")
    print("2- calça")
    print("3- tênis")


def escolher_produto():
    while True:
        try:
            produto = int(input("Digite o número do produto que deseja comprar: "))
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 3.")
            continue

        if produto == 1:
            return "camisa", 50.00
        elif produto == 2:
            return "calça", 100.00
        elif produto == 3:
            return "tênis", 150.00
        else:
            print("Produto inválido, por favor escolha um número entre 1 e 3.")


def escolher_metodo_pagamento():
    print("Formas de pagamento:")
    print("1- Dinheiro")
    print("2- Pix")
    print("3- Cartão")
    return input("Escolha o método de pagamento antes de finalizar: ").strip().lower()


def escolher_parcelas():
    while True:
        try:
            parcelas = int(input("Digite o número de parcelas do cartão: "))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro positivo.")
            continue

        if parcelas < 1:
            print("O número de parcelas deve ser no mínimo 1.")
            continue

        return parcelas


def calcular_desconto(valor, metodo, parcelas=1):
    if metodo in ["1", "dinheiro"]:
        return 0.10, "Dinheiro", 0.00
    elif metodo in ["2", "pix"]:
        return 0.10, "Pix", 0.00
    elif metodo in ["3", "cartão", "cartao", "cartao de crédito", "cartao de debito", "cartão de débito"]:
        juros = 0.01 if parcelas > 10 else 0.00
        return 0.00, "Cartão", juros
    else:
        return 0.00, "Outro", 0.00


def main():
    exibir_menu()
    produto_nome, valor = escolher_produto()
    print(f"Você escolheu a {produto_nome}, o valor é R${valor:.2f}")

    metodo = escolher_metodo_pagamento()
    parcelas = 1
    if metodo in ["3", "cartão", "cartao", "cartao de crédito", "cartao de debito", "cartão de débito"]:
        parcelas = escolher_parcelas()

    desconto, forma, juros = calcular_desconto(valor, metodo, parcelas)
    total = valor * (1 - desconto) * (1 + juros)

    if desconto > 0:
        print(f"Pagamento em {forma}. Desconto de 10% aplicado.")
    elif juros > 0:
        print(f"Pagamento em {forma} em {parcelas}x. Juros de 1% aplicado.")
    else:
        print(f"Pagamento em {forma}. Nenhum desconto aplicado.")

    print(f"Total a pagar: R${total:.2f}")


if __name__ == "__main__":
    main() 