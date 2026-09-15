"""
Estruturas de dados implementadas do zero (sem usar list/deque do Python
para representar a estrutura em si).
"""


# =============================================================================
# LISTA ENCADEADA
# Usada para os itens de cada Comanda (Etapas 2 e 3 do fluxo: incluir e
# remover refeicoes/bebidas) e para as listas de comandas, pagamentos e
# consumos do restaurante.
# =============================================================================

class NoLista:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    """Lista simplesmente encadeada: inserir no fim, remover por criterio,
    buscar por criterio e iterar."""

    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.cabeca is None

    def inserir_fim(self, dado):
        novo_no = NoLista(dado)
        if self.esta_vazia():
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
        self.tamanho += 1

    def remover(self, criterio):
        """Remove o primeiro dado para o qual criterio(dado) e True."""
        anterior = None
        atual = self.cabeca
        while atual is not None:
            if criterio(atual.dado):
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.tamanho -= 1
                return atual.dado
            anterior = atual
            atual = atual.proximo
        return None

    def buscar(self, criterio):
        atual = self.cabeca
        while atual is not None:
            if criterio(atual.dado):
                return atual.dado
            atual = atual.proximo
        return None

    def __len__(self):
        return self.tamanho

    def __iter__(self):
        atual = self.cabeca
        while atual is not None:
            yield atual.dado
            atual = atual.proximo


# =============================================================================
# FILA (FIFO)
# Usada no estoque (Etapa 4 do fluxo: fechamento da comanda baixa o estoque).
# A baixa de produtos sempre retira do lote mais antigo primeiro.
# =============================================================================

class NoFila:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Fila:
    """Fila FIFO com ponteiros de inicio/fim (enfileirar/desenfileirar em O(1))."""

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def enfileirar(self, dado):
        novo_no = NoFila(dado)
        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no
        self.tamanho += 1

    def desenfileirar(self):
        if self.esta_vazia():
            return None
        no_removido = self.inicio
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return no_removido.dado

    def espiar(self):
        return self.inicio.dado if not self.esta_vazia() else None

    def __len__(self):
        return self.tamanho

    def __iter__(self):
        atual = self.inicio
        while atual is not None:
            yield atual.dado
            atual = atual.proximo
