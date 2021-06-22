from model import Knapsack


# EQUAÇÃO DE RECORRÊNCIA (PARA 1 ITEM DE CADA TIPO APENAS):
# OPT(i, b) =   0                                         if b == 0
#               OPT(i-1, b)                               if b[i] > b
#               max(v[i] + OPT(i-1, b-b[i]), OPT(i-1, b)) otherwise


# Funciona para 1 item de cada tipo apenas, retornando valor
def knapsack_best_value(B, items):
    result = knapsack(B, items).get_total_value()

    return result


# Encontra melhor organização para mochila de tamanho B e lista de itens items,
# com 1 instancia de cada tipo de item apenas
def knapsack(B, items):
    M = []
    for i in range(len(items)):
        M.append([])
        for j in range(B + 1):
            M[i].append(Knapsack())

    if len(items) == 0 or B == 0:
        return Knapsack()

    for i in range(len(items)):
        for j in range(1, B + 1):
            # print(f"Mochila tamanho {j}")
            if items[i].size > j:
                M[i][j] = Knapsack(j, M[i - 1][j].items)
                # print(f"Não coloquei itens, usei anterior")
            else:
                max_l = items[i].value + M[i - 1][j - items[i].size].get_total_value()
                max_r = M[i - 1][j].get_total_value()
                if max_l > max_r:
                    M[i][j] = Knapsack(j, M[i - 1][j - items[i].size].items)
                    M[i][j].items.append(items[i])
                    # print(f"Coloquei +1 item {items[i]} - Mochila: {M[i][j]}")
                else:
                    M[i][j] = Knapsack(j, M[i - 1][j].items)
                    # print(f"Não coloquei +1 item {items[i]} - Mochila: {M[i][j]}")

    return M[len(items) - 1][B]


# TODO Criar equação de recorrência para 10 itens de cada tipo

# TODO Fazer funcionar para 10 itens de cada tipo
def ten_knapsack(B, items):
    return 0
