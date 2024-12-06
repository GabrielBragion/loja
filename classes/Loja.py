from classes.DBconnection import DatabaseConnection
from classes.Produto import Produto
from classes.Venda import Venda
from classes.InvalidProdAttr import InvalidProdAttr
from decimal import Decimal as dec, InvalidOperation

class Loja:
    def __init__(self, nome: str):
        self.nome = nome
        self.db = DatabaseConnection(host="localhost", user="root", password="Ga130196#", database="venda_produto")
        self.lista_produtos = self.carregar_produtos()
        self.lista_vendas = [] 

    def carregar_produtos(self) -> list[Produto]:
        """
        Carrega todos os produtos do banco de dados e retorna uma lista de objetos Produto.
        """
        produtos = self.db.fetch_all("SELECT nome, descricao, marca, tipo, quantidade, preco, iva FROM produto")
        return [Produto(*produto) for produto in produtos]

    def obter_entrada_decimal(self, mensagem: str, min_val: dec = 0, max_val: dec = dec(999)) -> dec:
        """
        Obtém um valor decimal do usuário com validação.
        """
        while True:
            try:
                valor = dec(input(mensagem))
                if not (min_val <= valor <= max_val):
                    raise ValueError(f"O valor deve estar entre {min_val} e {max_val}.")
                return valor
            except (ValueError, InvalidOperation):
                print(f"Entrada inválida! Insira um número decimal válido entre {min_val} e {max_val}.")

    def obter_entrada_inteiro(self, mensagem: str, min_val: int = 0, max_val: int = 999) -> int:
        """
        Obtém um valor inteiro do usuário com validação.
        """
        while True:
            try:
                valor = int(input(mensagem))
                if not (min_val <= valor <= max_val):
                    raise ValueError(f"O valor deve estar entre {min_val} e {max_val}.")
                return valor
            except ValueError:
                print(f"Entrada inválida! Insira um número inteiro válido entre {min_val} e {max_val}.")

    def inserir_produto(self):
        while True:
            try:
                # Recebe o nome do produto e valida se já existe na base de dados
                nome = input("Digite o nome do produto: ").strip()
                if any(produto.nome.lower() == nome.lower() for produto in self.lista_produtos):
                    print(f"Produto '{nome}' já existe. Tente novamente com outro nome.")
                    continue

                # Entradas de dados do usuário
                descricao = input("Digite a descrição: ").strip()
                marca = input("Digite a marca do produto: ").strip()
                tipo = input("Digite o tipo do produto: ").strip()

                # Validar preço, quantidade e IVA com métodos de entrada robustos
                preco = self.obter_entrada_decimal("Digite o preço do produto: ", min_val=0.01, max_val=999)
                quantidade = self.obter_entrada_inteiro("Digite a quantidade do produto: ", min_val=1)
                iva = self.obter_entrada_decimal("Digite o IVA (em porcentagem): ", min_val=0, max_val=100)

                # Criar objeto Produto e validar através da classe Produto
                produto = Produto(nome, descricao, marca, tipo, preco, quantidade, iva)

                # Inserir o produto na base de dados
                query = """
                    INSERT INTO produto (nome, descricao, marca, tipo, quantidade, preco, iva) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                self.db.execute_query(query, (nome.lower(), descricao.lower(), marca.lower(), tipo.lower(), preco, quantidade, iva))
                print(f"{nome} foi adicionado à loja.")
                self.lista_produtos = self.carregar_produtos()  # Atualizar lista de produtos
                break  # Sai do loop se o produto foi inserido com sucesso

            except (ValueError, InvalidProdAttr) as error:
                print(f"Erro: {error}. Tente novamente.")
            
    def listar_produtos(self):
        if not self.lista_produtos:
            print("\nNenhum produto disponível.\n")
        else:
            print("\nLista de Produtos:\n")
            for produto in self.lista_produtos:
                print(produto)
            
    def atualizar_preco(self):
        nome = input("Digite o nome do produto: ").strip()
        produto_encontrado = False
        for produto in self.lista_produtos:
            if nome.lower() == produto.nome.lower():
                produto_encontrado = True
                preco = self.obter_entrada_decimal("Digite o novo preço do produto: ", min_val=0.01, max_val=999)
                query = "UPDATE produto SET preco = %s WHERE nome = %s"
                self.db.execute_query(query, (preco, nome))
                self.lista_produtos = self.carregar_produtos()
                print(f"\nProduto: {nome} - preço antigo: {produto.preco} preço novo: {dec(preco)}\n")
                break
            
        if not produto_encontrado:
            print(f"\nProduto '{nome}' não encontrado.\n")
    
    def repor_produto(self):
        nome = input("Digite o nome do produto: ").strip()
        produto_encontrado = False
        for produto in self.lista_produtos:
            if nome.lower() == produto.nome.lower():
                produto_encontrado = True
                quantidade_nova = self.obter_entrada_inteiro("Digite a quantidade quer quer adicionar do produto: ", min_val=1)
                query = "UPDATE produto SET quantidade = quantidade + %s WHERE nome = %s"
                self.db.execute_query(query, (quantidade_nova, nome))
                self.lista_produtos = self.carregar_produtos()
                print(f"\nProduto: {nome} - quantidade antiga: {produto.quantidade} quantidade nova: {produto.quantidade + quantidade_nova}\n")
                break
            
        if not produto_encontrado:
            print(f"\nProduto '{nome}' não encontrado.\n")
            
    def eliminar_produto(self):
        nome = input("Digite o nome do produto: ")
        produto_encontrado = False
        for produto in self.lista_produtos:
            if nome.lower() == produto.nome.lower():
                produto_encontrado = True
                query = "DELETE from produto WHERE nome = %s"
                self.db.execute_query(query, (nome,))
                self.lista_produtos = self.carregar_produtos()
                print(f"\nProduto: {nome} - Eliminado!\n")
                break
            
        if not produto_encontrado:
            print(f"\nProduto '{nome}' não encontrado.\n")

