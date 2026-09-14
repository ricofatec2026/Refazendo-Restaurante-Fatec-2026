# Sistema de Controle de Restaurante

Projeto individual das disciplinas **Estrutura de Dados** e **Linguagem de
Programação 2** — Fatec Rio Claro, Tecnologia em Inteligência Artificial.

Tema proposto: um sistema para controlar comandas, estoque, pagamentos e
consumo de um pequeno restaurante.

## Requisito principal

As estruturas de dados centrais do problema (itens da comanda e controle de
estoque) foram implementadas **do zero**, sem usar `list`, `deque` ou outras
estruturas built-in do Python para representar a lógica pedida — apenas
classes próprias, com encapsulamento.

## Estrutura do projeto

| Arquivo | Conteúdo |
|---|---|
| `estruturas.py` | `ListaEncadeada` e `Fila`, implementadas manualmente com nós e ponteiros |
| `modelos.py` | Entidades do domínio: `Refeicao`, `Bebida`, `Produto`, `Comanda`, `Pagamento` |
| `estoque.py` | `Estoque`, controla os produtos usando uma `Fila` própria por produto |
| `restaurante.py` | `Restaurante`, orquestra comandas/estoque/pagamentos, gera dados falsos e relatórios |
| `main.py` | Ponto de entrada: roda a simulação completa |
| `requirements.txt` | Dependências do projeto |

## Decisões de design

- **Comandas → Lista Encadeada.** Cada comanda guarda suas refeições e
  bebidas em uma `ListaEncadeada` própria, permitindo adicionar ou remover
  itens em qualquer ponto antes do fechamento.
- **Estoque → Fila (FIFO).** Cada produto tem sua própria `Fila` de lotes.
  A baixa de estoque sempre remove da frente da fila (lote mais antigo),
  atendendo à regra de que produtos perecíveis mais velhos têm prioridade
  de uso.
- **Dicionário built-in do Python** é usado apenas como **índice** dentro do
  `Estoque` (nome do produto → sua `Fila`), nunca substituindo a lógica da
  estrutura de dados pedida no enunciado.

## Fluxo simulado

1. Abertura de uma comanda para um cliente
2. Inclusão de uma ou mais refeições e bebidas
3. Remoção de um item antes do fechamento (demonstração)
4. Fechamento da comanda: baixa o estoque dos itens consumidos, calcula o
   valor total e gera o pagamento
5. Geração de dados falsos com **Faker** para popular estoque e simular
   vários atendimentos
6. Persistência dos dados com **pickle** (salvar e recarregar)
7. Emissão dos relatórios de **vendas** e de **consumo**

## Como executar

```bash
pip install -r requirements.txt
python main.py
```

## Autor

Rico — Fatec Rio Claro, Tecnologia em Inteligência Artificial
