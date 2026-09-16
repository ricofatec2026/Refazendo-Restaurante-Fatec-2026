"""
Entidades do dominio do restaurante, na ordem em que aparecem no fluxo
simulado (ver README.md):
  1. Comanda      -> abertura, inclusao (Etapa 2), remocao (Etapa 3) e
                     fechamento (Etapa 4) de itens
  2. Refeicao/Bebida -> itens que a Comanda guarda
  3. Produto      -> lote de estoque, usado no fechamento
  4. Pagamento    -> gerado ao fechar a comanda (Etapa 4)
"""

from datetime import datetime

from estruturas import ListaEncadeada


class Comanda:
    """Refeicoes e bebidas ficam em listas encadeadas proprias, permitindo
    adicionar/remover itens ate o fechamento."""

    def __init__(self, numero, nome_cliente):
        self.numero = numero
        self.nome_cliente = nome_cliente
        self.data_hora_abertura = datetime.now()
        self.data_hora_fechamento = None
        self.refeicoes = ListaEncadeada()
        self.bebidas = ListaEncadeada()
        self.fechada = False

    # ---------------------- Etapa 2: inclusao de itens ----------------------

    def adicionar_refeicao(self, refeicao):
        if self.fechada:
            raise RuntimeError("Comanda ja fechada.")
        self.refeicoes.inserir_fim(refeicao)

    def adicionar_bebida(self, bebida):
        if self.fechada:
            raise RuntimeError("Comanda ja fechada.")
        self.bebidas.inserir_fim(bebida)

    # ---------------------- Etapa 3: remocao de itens ----------------------

    def remover_refeicao(self, nome_refeicao):
        if self.fechada:
            raise RuntimeError("Comanda ja fechada.")
        return self.refeicoes.remover(lambda r: r.nome == nome_refeicao)

    def remover_bebida(self, nome_bebida):
        if self.fechada:
            raise RuntimeError("Comanda ja fechada.")
        return self.bebidas.remover(lambda b: b.nome == nome_bebida)

    # ---------------------- Etapa 4: fechamento ----------------------

    def calcular_total(self):
        return sum(r.preco for r in self.refeicoes) + sum(b.preco for b in self.bebidas)

    def fechar(self):
        self.fechada = True
        self.data_hora_fechamento = datetime.now()

    def __repr__(self):
        status = "fechada" if self.fechada else "aberta"
        return (f"Comanda #{self.numero} ({self.nome_cliente}) - {status} - "
                f"{len(self.refeicoes)} refeicao(oes), {len(self.bebidas)} bebida(s)")


class Refeicao:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Bebida:
    TIPOS_VALIDOS = ("Coca Cola", "Suco", "Agua")

    def __init__(self, nome, preco):
        if nome not in Bebida.TIPOS_VALIDOS:
            raise ValueError(f"Bebida invalida: {nome}")
        self.nome = nome
        self.preco = preco


class Produto:
    """Um lote de produto comprado pelo restaurante. Usado pelo Estoque
    (Etapa 4: a baixa de estoque acontece no fechamento da comanda)."""

    def __init__(self, nome, preco_compra, preco_venda, data_compra,
                 data_vencimento, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade = quantidade


class Pagamento:
    """Gerado ao final da Etapa 4 (fechamento da comanda), depois que o
    estoque ja foi baixado e o valor total calculado."""

    FORMAS_VALIDAS = ("PIX", "Cartao", "Dinheiro")

    def __init__(self, nome_cliente, numero_comanda, forma_pagamento, valor_total):
        if forma_pagamento not in Pagamento.FORMAS_VALIDAS:
            raise ValueError(f"Forma de pagamento invalida: {forma_pagamento}")
        self.nome_cliente = nome_cliente
        self.numero_comanda = numero_comanda
        self.forma_pagamento = forma_pagamento
        self.valor_total = valor_total
        self.data_hora = datetime.now()

    def __repr__(self):
        return (f"Pagamento(comanda #{self.numero_comanda}, "
                f"{self.forma_pagamento}, R${self.valor_total:.2f})")
