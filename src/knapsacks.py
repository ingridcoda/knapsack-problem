from model import Knapsack


# DESCRIÇÃO:
#   Calcula melhor organização para mochila de tamanho B e lista de itens items,
#   com 1 instancia de cada tipo de item apenas.
#
# EQUAÇÃO DE RECORRÊNCIA:
#   OPT(i, b) = 0                                                   if b == 0
#               OPT(i - 1, b)                                       if b[i] > b
#               max(v[i] + OPT(i - 1, b - b[i]), OPT(i - 1, b))     otherwise
#
# OBSERVAÇÕES:
#  - Foi necessário ajustar indices por causa do Python.
def knapsack(B, items):
    M = []
    for i in range(len(items)):
        M.append([])
        for b in range(B + 1):
            M[i].append(Knapsack())

    if len(items) == 0 or B == 0:
        return Knapsack()

    for i in range(len(items)):
        for b in range(1, B + 1):
            if items[i].size > b:
                M[i][b] = Knapsack(b, M[i - 1][b].items)
            else:
                max_l = items[i].value + M[i - 1][b - items[i].size].get_total_value()
                max_r = M[i - 1][b].get_total_value()
                if max_l > max_r:
                    M[i][b] = Knapsack(b, M[i - 1][b - items[i].size].items)
                    M[i][b].items.append(items[i])
                else:
                    M[i][b] = Knapsack(b, M[i - 1][b].items)

    return M[len(items) - 1][B]


# DESCRIÇÃO:
#   Calcula melhor organização para mochila de tamanho B e lista de itens items,
#   com 10 instancias de cada tipo de item.
#
# EQUAÇÃO DE RECORRÊNCIA:
#   OPT(i, b) = max((vi * k) + OPT(i - 1, b - (wi * k)))  if (wi * k) <= b, for 0 <= k <= 10
#
# OBSERVAÇÕES:
#  - Foi necessário ajustar indices por causa do Python;
#  - Não funciona direito, não conseguimos ajustar a tempo da entrega;
#  - Nos desculpe e favor considerar o que for possível. Obrigada!
def ten_knapsack(B, items):
    M = []
    for i in range(len(items)):
        M.append([])
        for b in range(B + 1):
            M[i].append(Knapsack())

    if len(items) == 0 or B == 0:
        return Knapsack()

    for i in range(len(items)):
        for b in range(1, B + 1):
            k = 0
            while items[i].size * (k + 1) <= b:
                k += 1
            previous = Knapsack()
            if i > 0:
                previous = M[i - 1][b - (items[i].size * k)]
            M[i][b] = Knapsack(b, previous.items)
            for x in range(1, k + 1):
                M[i][b].items.append(items[i])

    return M[len(items) - 1][B]
