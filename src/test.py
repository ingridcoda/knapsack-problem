from knapsacks import knapsack, knapsack_best_value, ten_knapsack
from model import Item


def test_knapsack_best_value():
    knapsack_size = 8
    items = [Item(3, 2), Item(2, 1)]
    value_expected = 3
    result = knapsack_best_value(knapsack_size, items)

    print("knapsack_best_value - Teste 1:")
    print(f" - Tamanho mochila: {knapsack_size}")
    print(f" - Itens: {items}")
    print(f" - Valor esperado: {value_expected}")
    print(f" - Valor obtido: {result}\n")
    assert value_expected == result


def test_knapsack():
    knapsack_size = 8
    items = [Item(3, 2), Item(2, 1)]
    value_expected = 3
    result = knapsack(knapsack_size, items)

    print("knapsack - Teste 1:")
    print(f" - Tamanho mochila: {knapsack_size}")
    print(f" - Itens: {items}")
    print(f" - Itens esperados: {items}")
    print(f" - Itens obtidos: {result.items}")
    print(f" - Valor esperado: {value_expected}")
    print(f" - Valor obtido: {result.get_total_value()}\n")
    assert items == result.items
    assert value_expected == result.get_total_value()


def test_ten_knapsack_best_value():
    knapsack_size = 8
    items = [Item(3, 2), Item(2, 1)]
    items_expected = [Item(3, 2), Item(3, 2), Item(2, 1)]
    value_expected = 5
    result = ten_knapsack(knapsack_size, items)

    print("ten_knapsack - Teste 1:")
    print(f" - Tamanho mochila: {knapsack_size}")
    print(f" - Itens: {items}")
    print(f" - Quantidade itens esperados: {len(items_expected)}")
    print(f" - Quantidade itens obtidos: {len(result.items)}")
    print(f" - Itens esperados: {items_expected}")
    print(f" - Itens obtidos: {result.items}")
    print(f" - Valor esperado: {value_expected}")
    print(f" - Valor obtido: {result.get_total_value()}\n")
    assert value_expected == result.get_total_value()

    knapsack_size = 22
    items = [Item(2, 5), Item(1, 1)]
    items_expected = [
        Item(2, 5), Item(2, 5),
        Item(2, 5), Item(2, 5),
        Item(2, 5), Item(2, 5),
        Item(2, 5), Item(2, 5),
        Item(2, 5), Item(2, 5),
        Item(1, 1), Item(1, 1)
    ]
    value_expected = 52
    result = ten_knapsack(knapsack_size, items)

    print("ten_knapsack - Teste 2:")
    print(f" - Tamanho mochila: {knapsack_size}")
    print(f" - Itens: {items}")
    print(f" - Quantidade itens esperados: {len(items_expected)}")
    print(f" - Quantidade itens obtidos: {len(result.items)}")
    print(f" - Itens esperados: {items_expected}")
    print(f" - Itens obtidos: {result.items}")
    print(f" - Valor esperado: {value_expected}")
    print(f" - Valor obtido: {result.get_total_value()}\n")
    assert len(items_expected) == len(result.items)
    assert value_expected == result.get_total_value()


if __name__ == "__main__":
    test_knapsack()  # testa melhor organização de mochila para 1 item de cada tipo apenas
    test_knapsack_best_value()  # testa melhor valor guardado na mochila para 1 item de cada tipo apenas
    test_ten_knapsack_best_value()  # testa melhor valor guardado na mochila para 10 items de cada tipo
