from decimal import Decimal as dec
from classes.InvalidProdAttr import InvalidProdAttr

class Produto:
    def __init__(
        self,
        nome : str,
        descricao : str,
        marca : str,
        tipo : str,
        preco : dec,
        quantidade: int,
        iva : dec
    ):
        
        if quantidade < 0:
            raise InvalidProdAttr(f"{quantidade=} Valor invalido, quantidade deve ser superior a 0")
        
        if preco < 0 and preco > 999:
            raise InvalidProdAttr(f"{preco=} Valor invalido, preco deve ser superior a 0 e menor que 999")
        
        self.__nome = nome
        self.__descricao = descricao
        self.__marca = marca
        self.__tipo = tipo
        self.__quantidade = quantidade
        self.__preco = preco
        self.__iva = iva

    # Getters
    @property
    def nome(self):
        return self.__nome
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def marca(self):
        return self.__marca

    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def preco(self):
        return self.__preco
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @property
    def iva(self):
        return self.__iva
    
    # Setters
    @nome.setter
    def nome(self, valor):
        if not valor.strip():
            raise ValueError("O nome não pode ser vazio.")
        self.__nome = valor

    @descricao.setter
    def descricao(self, valor):
        if not valor.strip():
            raise ValueError("A descrição não pode ser vazia.")
        self.__descricao = valor

    @marca.setter
    def marca(self, valor):
        if not valor.strip():
            raise ValueError("A marca não pode ser vazia.")
        self.__marca = valor

    @tipo.setter
    def tipo(self, valor):
        if not valor.strip():
            raise ValueError("O tipo não pode ser vazio.")
        self.__tipo = valor

    @quantidade.setter
    def quantidade(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("A quantidade deve ser um número maior ou igual a zero.")
        self.__quantidade = valor

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("O preço deve ser um número maior ou igual a zero.")
        self.__preco = valor

    @iva.setter
    def iva(self, valor):
        if valor < 0 or valor > 100:
            raise ValueError("O IVA deve ser um valor entre 0 e 100.")
        self.__iva = valor
        
    def __str__(self):
        return (f"""Produto: {self.nome}
Descrição: {self.descricao}
Marca: {self.marca}
Tipo: {self.tipo}
Quantidade: {self.quantidade}
Preço: {self.preco}
IVA: {self.iva}

----------------------------------    
""")