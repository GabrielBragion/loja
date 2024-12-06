from classes.Loja import Loja
from classes.Detalhe_Venda import DetalheVenda

def menu_principal():
    print("\nMenu Principal")
    print("1. Gestão de Produtos")
    print("2. Gestão de Vendas")
    print("3. Sair")
    try:
        escolha = int(input("Escolha uma opção: "))
        return escolha
    except ValueError:
        print("\nDigite uma opção valida\n")  

def menu_produtos():
    print("1. Inserir Produto")
    print("2. Listar Produtos")
    print("3. Atualizar preço do produto")
    print("4. Registar reposição de produto")
    print("5. Eliminar produto")
    print("6. Voltar ao menu anterior")
    try:
        escolha = int(input("Escolha uma opção: "))
        return escolha
    except ValueError:
        print("\nDigite uma opção valida\n")    
    
def menu_vendas():
    print("1. Registrar Venda")
    print("2. Listar Vendas")
    print("3. Vendas por Dia")
    print("4. Vendas por Produto")
    print("5. Vendas por Mês")
    print("6. Anular Venda")
    print("7. Voltar ao menu anterior")
    try:
        escolha = int(input("Escolha uma opção: "))
        return escolha
    except ValueError:
        print("\nDigite uma opção valida\n")

def main():
    loja = Loja("Juliamania")
    print(f"\nBem-vindo ao sistema de gerenciamento de loja: {loja.nome}")
    
    
    while True:
        opcao = menu_principal()
        match opcao:
            case 1:
                while True:
                    escolha = menu_produtos()
                    match escolha:
                        case 1:
                            loja.inserir_produto()
                        case 2:
                            loja.listar_produtos()                        
                        case 3:
                            loja.atualizar_preco()
                        case 4:
                            loja.repor_produto()
                        case 5:
                            loja.eliminar_produto()
                        case 6:
                            break
                        case _:
                            print("\nOpção inválida! Tente novamente.\n")
            case 2:
                while True:
                    escolha = menu_vendas()
                    match escolha:
                            case 1:
                                pass
                            case 2:
                                pass
                            case 3:
                                pass
                            case 4:
                                pass
                            case 5:
                                pass
                            case 6:
                                pass
                            case 7:
                                break
                            case _:
                                print("\nOpção inválida! Tente novamente.\n")
            case 3:
                print("\nBeijinhos, volte sempre!\n")
                break
            case _:
                print("\nOpção inválida! Tente novamente.\n")

    loja.db.close()

if __name__ == "__main__":
    main()