from knapsacks import knapsack, ten_knapsack
from model import Item


def test_knapsack_best_value_size_8_best_value_3():
    try:
        knapsack_size = 8
        items = [Item(value=2, size=3), Item(value=1, size=2)]
        items_expected = items
        value_expected = 3
        result = knapsack(knapsack_size, items)

        print("test_knapsack_best_value_size_8_best_value_3:")
        print(f" - Tamanho mochila: {knapsack_size}")
        print(f" - Itens: {items}")
        print(f" - Quantidade itens esperados: {len(items_expected)}")
        print(f" - Quantidade itens obtidos: {len(result.items)}")
        print(f" - Itens esperados: {items_expected}")
        print(f" - Itens obtidos: {result.items}")
        print(f" - Valor esperado: {value_expected}")
        print(f" - Valor obtido: {result.get_total_value()}\n")
        assert items == result.items
        assert value_expected == result.get_total_value()
        print("test_knapsack_best_value_size_8_best_value_3 passou!\n")

    except AssertionError:
        print("test_knapsack_best_value_size_8_best_value_3 falhou!\n")


def test_ten_knapsack_size_8_best_value_5():
    try:
        knapsack_size = 8
        items = [Item(value=2, size=3), Item(value=1, size=2)]
        items_expected = [items[0] for i in range(2)] + [items[1]]
        value_expected = 5
        result = ten_knapsack(knapsack_size, items)

        print("test_ten_knapsack_size_8_best_value_5:")
        print(f" - Tamanho mochila: {knapsack_size}")
        print(f" - Itens por tipo: {items}")
        print(f" - Quantidade itens esperados: {len(items_expected)}")
        print(f" - Quantidade itens obtidos: {len(result.items)}")
        print(f" - Itens esperados: {items_expected}")
        print(f" - Itens obtidos: {result.items}")
        print(f" - Valor esperado: {value_expected}")
        print(f" - Valor obtido: {result.get_total_value()}\n")
        assert value_expected == result.get_total_value()

        print("test_ten_knapsack_size_8_best_value_5 passou!\n")

    except AssertionError:
        print("test_ten_knapsack_size_8_best_value_5 falhou!\n")


def test_ten_knapsack_size_22_best_value_52():
    try:
        knapsack_size = 22
        items = [Item(value=5, size=2), Item(value=1, size=1)]
        items_expected = [items[0] for i in range(10)] + [items[1] for i in range(2)]
        value_expected = 52
        result = ten_knapsack(knapsack_size, items)

        print("test_ten_knapsack_size_22_best_value_52:")
        print(f" - Tamanho mochila: {knapsack_size}")
        print(f" - Itens por tipo: {items}")
        print(f" - Quantidade itens esperados: {len(items_expected)}")
        print(f" - Quantidade itens obtidos: {len(result.items)}")
        print(f" - Itens esperados: {items_expected}")
        print(f" - Itens obtidos: {result.items}")
        print(f" - Valor esperado: {value_expected}")
        print(f" - Valor obtido: {result.get_total_value()}\n")
        assert value_expected == result.get_total_value()

        print("test_ten_knapsack_size_22_best_value_52 passou!\n")

    except AssertionError:
        print("test_ten_knapsack_size_22_best_value_52 falhou!\n")


def test_ten_knapsack_best_value_inst_1():
    try:
        knapsack_size = 269
        items = [Item(value=55, size=95), Item(value=10, size=4),
                 Item(value=47, size=60), Item(value=5, size=32),
                 Item(value=4, size=23), Item(value=50, size=72),
                 Item(value=8, size=80), Item(value=61, size=62),
                 Item(value=85, size=65), Item(value=87, size=46)]

        items_expected = [items[0] for i in range(0)] + [items[1] for i in range(9)] + \
                         [items[2] for i in range(0)] + [items[3] for i in range(0)] + \
                         [items[4] for i in range(0)] + [items[5] for i in range(0)] + \
                         [items[6] for i in range(0)] + [items[7] for i in range(0)] + \
                         [items[8] for i in range(0)] + [items[9] for i in range(5)]

        value_expected = 525
        result = ten_knapsack(knapsack_size, items)

        print("test_ten_knapsack_best_value_inst_1:")
        print(f" - Tamanho mochila: {knapsack_size}")
        print(f" - Itens por tipo: {items}")
        print(f" - Quantidade itens esperados: {len(items_expected)}")
        print(f" - Quantidade itens obtidos: {len(result.items)}")
        print(f" - Valor esperado: {value_expected}")
        print(f" - Valor obtido: {result.get_total_value()}\n")
        assert len(items_expected) == len(result.items)
        assert value_expected == result.get_total_value()

        print("test_ten_knapsack_best_value_inst_1 passou!\n")

    except (AssertionError, Exception):
        print("test_ten_knapsack_best_value_inst_1 falhou!\n")


def test_ten_knapsack_best_value_inst_2():
    try:
        knapsack_size = 878
        items = [Item(value=44, size=92), Item(value=46, size=4), Item(value=90, size=43), Item(value=72, size=83),
                 Item(value=91, size=84), Item(value=40, size=68), Item(value=75, size=92), Item(value=35, size=82),
                 Item(value=8, size=6), Item(value=54, size=44), Item(value=78, size=32), Item(value=40, size=18),
                 Item(value=77, size=56), Item(value=15, size=83), Item(value=61, size=25), Item(value=17, size=96),
                 Item(value=75, size=70), Item(value=29, size=48), Item(value=75, size=14), Item(value=63, size=58)]

        result = ten_knapsack(knapsack_size, items)

        print("test_ten_knapsack_best_value_inst_2:")
        print(f" - Tamanho mochila: {knapsack_size}")
        print(f" - Itens por tipo: {items}")
        print(f" - Quantidade itens obtidos: {len(result.items)}")
        print(f" - Valor obtido: {result.get_total_value()}\n")

        print("test_ten_knapsack_best_value_inst_2 executado!\n")

    except (AssertionError, Exception):
        print("test_ten_knapsack_best_value_inst_2 falhou!\n")


def test_ten_knapsack_best_value_inst_3():
    try:
        knapsack_size = 20
        items = [Item(value=9, size=6), Item(value=11, size=5), Item(value=13, size=9), Item(value=15, size=7)]
        result = ten_knapsack(knapsack_size, items)

        print("test_ten_knapsack_best_value_inst_3:")
        print(f" - Tamanho mochila: {knapsack_size}")
        print(f" - Itens por tipo: {items}")
        print(f" - Quantidade itens obtidos: {len(result.items)}")
        print(f" - Valor obtido: {result.get_total_value()}\n")

        print("test_ten_knapsack_best_value_inst_3 executado!\n")

    except (AssertionError, Exception):
        print("test_ten_knapsack_best_value_inst_3 falhou!\n")


def test_ten_knapsack_best_value_inst_4():
    try:
        knapsack_size = 11
        items = [Item(value=6, size=2), Item(value=10, size=4), Item(value=12, size=6), Item(value=13, size=7)]

        result = ten_knapsack(knapsack_size, items)

        print("test_ten_knapsack_best_value_inst_4:")
        print(f" - Tamanho mochila: {knapsack_size}")
        print(f" - Itens por tipo: {items}")
        print(f" - Quantidade itens obtidos: {len(result.items)}")
        print(f" - Valor obtido: {result.get_total_value()}\n")

        print("test_ten_knapsack_best_value_inst_4 executado!\n")

    except (AssertionError, Exception):
        print("test_ten_knapsack_best_value_inst_4 falhou!\n")


def test_ten_knapsack_best_value_inst_5():
    try:
        knapsack_size = 60
        items = [Item(value=20, size=30), Item(value=18, size=25),
                 Item(value=17, size=20), Item(value=15, size=18),
                 Item(value=15, size=17), Item(value=10, size=11),
                 Item(value=5, size=5), Item(value=3, size=2),
                 Item(value=1, size=1), Item(value=1, size=1)]

        result = ten_knapsack(knapsack_size, items)

        print("test_ten_knapsack_best_value_inst_5:")
        print(f" - Tamanho mochila: {knapsack_size}")
        print(f" - Itens por tipo: {items}")
        print(f" - Quantidade itens obtidos: {len(result.items)}")
        print(f" - Valor obtido: {result.get_total_value()}\n")

        print("test_ten_knapsack_best_value_inst_5 executado!\n")

    except (AssertionError, Exception):
        print("test_ten_knapsack_best_value_inst_5 falhou!\n")


def test_ten_knapsack_best_value_inst_6():
    try:
        knapsack_size = 50
        items = [Item(value=70, size=31), Item(value=20, size=10), Item(value=39, size=20),
                 Item(value=37, size=19), Item(value=7, size=4), Item(value=5, size=3),
                 Item(value=10, size=6)]

        items_expected = [items[0] for i in range(1)] + [items[1] for i in range(0)] + \
                         [items[2] for i in range(0)] + [items[3] for i in range(1)] + \
                         [items[4] for i in range(0)] + [items[5] for i in range(0)] + \
                         [items[6] for i in range(0)]

        value_expected = 107
        result = ten_knapsack(knapsack_size, items)

        print("test_ten_knapsack_best_value_inst_6:")
        print(f" - Tamanho mochila: {knapsack_size}")
        print(f" - Itens por tipo: {items}")
        print(f" - Quantidade itens esperados: {len(items_expected)}")
        print(f" - Quantidade itens obtidos: {len(result.items)}")
        print(f" - Valor esperado: {value_expected}")
        print(f" - Valor obtido: {result.get_total_value()}\n")
        assert len(items_expected) == len(result.items)
        assert value_expected == result.get_total_value()

        print("test_ten_knapsack_best_value_inst_6 passou!\n")

    except (AssertionError, Exception):
        print("test_ten_knapsack_best_value_inst_6 falhou!\n")


def test_ten_knapsack_best_value_inst_7():
    try:
        knapsack_size = 80
        items = [Item(value=33, size=15), Item(value=24, size=20), Item(value=36, size=17),
                 Item(value=37, size=8), Item(value=12, size=31)]

        result = ten_knapsack(knapsack_size, items)

        print("test_ten_knapsack_best_value_inst_7:")
        print(f" - Tamanho mochila: {knapsack_size}")
        print(f" - Itens por tipo: {items}")
        print(f" - Quantidade itens obtidos: {len(result.items)}")
        print(f" - Valor obtido: {result.get_total_value()}\n")

        print("test_ten_knapsack_best_value_inst_7 executado!\n")

    except (AssertionError, Exception):
        print("test_ten_knapsack_best_value_inst_7 falhou!\n")


def test_ten_knapsack_best_value_inst_8():
    try:
        knapsack_size = 879
        items = [Item(value=91, size=84), Item(value=72, size=83), Item(value=90, size=43), Item(value=46, size=4),
                 Item(value=55, size=44), Item(value=8, size=6), Item(value=35, size=82), Item(value=75, size=92),
                 Item(value=61, size=25), Item(value=15, size=83), Item(value=77, size=56), Item(value=40, size=18),
                 Item(value=63, size=58), Item(value=75, size=14), Item(value=29, size=48), Item(value=75, size=70),
                 Item(value=17, size=96), Item(value=78, size=32), Item(value=40, size=68), Item(value=44, size=92)]

        result = ten_knapsack(knapsack_size, items)

        print("test_ten_knapsack_best_value_inst_8:")
        print(f" - Tamanho mochila: {knapsack_size}")
        print(f" - Itens por tipo: {items}")
        print(f" - Quantidade itens obtidos: {len(result.items)}")
        print(f" - Valor obtido: {result.get_total_value()}\n")

        print("test_ten_knapsack_best_value_inst_8 executado!\n")

    except (AssertionError, Exception):
        print("test_ten_knapsack_best_value_inst_8 falhou!\n")


def run_all_tests():
    print("Executando testes...\n")

    # testa melhor valor guardado na mochila de tamanho 8, para 1 item de cada tipo apenas (teste extra)
    test_knapsack_best_value_size_8_best_value_3()

    # testa melhor valor guardado na mochila de tamanho 8, para 10 items de cada tipo (teste 1 do enunciado)
    test_ten_knapsack_size_8_best_value_5()

    # testa melhor valor guardado na mochila de tamanho 22, para 10 items de cada tipo (teste 2 do enunciado)
    test_ten_knapsack_size_22_best_value_52()

    # testa instancias dadas pelo professor, para 10 itens de cada tipo
    test_ten_knapsack_best_value_inst_1()
    test_ten_knapsack_best_value_inst_2()
    test_ten_knapsack_best_value_inst_3()
    test_ten_knapsack_best_value_inst_4()
    test_ten_knapsack_best_value_inst_5()
    test_ten_knapsack_best_value_inst_6()
    test_ten_knapsack_best_value_inst_7()
    test_ten_knapsack_best_value_inst_8()

    print("Testes finalizados!")


if __name__ == "__main__":
    run_all_tests()
