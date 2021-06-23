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


# EQUAÇÃO DE RECORRÊNCIA (PARA 10 ITENS DE CADA TIPO):
# OPT(i, b) = max ((vi * k) + OPT(i - 1, b - (wi * k)))  if (wi * k) <= b, for 0 <= k <= 10

# TODO Fazer funcionar para 10 itens de cada tipo (atualmente ele não considera ATÉ o item i e sim SÓ o item i)
def ten_knapsack(B, items):
    M = []
    for i in range(len(items) + 1):
        M.append([])
        for j in range(B + 1):
            M[i].append(Knapsack())

    if len(items) == 0 or B == 0:
        return Knapsack()

    for i in range(1, len(items) + 1):
        # print(f"item atual {items[i-1]}")
        for j in range(1, B + 1):
            # print("J", j)
            k = 0
            while items[i - 1].size * (k + 1) <= j:
                k += 1
            previous = M[i - 2][j - (items[i - 1].size * k)]
            # print("anterior", previous)
            M[i][j] = Knapsack(j, previous.items)
            for x in range(1, k + 1):
                # print("X", x)
                M[i][j].items.append(items[i - 1])
            # print("posterior", M[i-1][j])

    # for i in range(len(items)+1):
    #     print([M[i][j].get_total_value() for j in range(B+1)])

    result = M[0][B]
    for i in range(1, len(items) + 1):
        if M[i][B].get_total_value() > result.get_total_value():
            result = M[i][B]
    return result
