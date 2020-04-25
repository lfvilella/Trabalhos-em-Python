import random

def sort(list_to_sort):
    if len(list_to_sort) <= 1:
        return list_to_sort

    pivot = random.choice(list_to_sort)
    maior = []
    iqual = []
    menor = []
    for valor in list_to_sort:
        if valor < pivot:
            menor.append(valor)
        elif valor == pivot:
            iqual.append(valor)
        else:
            maior.append(valor)

    menor_sorted = sort(menor)
    maior_sorted = sort(maior)

    return menor_sorted + iqual + maior_sorted



def b_sort(list_to_sort):
    changed = True
    len_list = len(list_to_sort)
    while changed:
        changed = False
        for next_idx, idx in enumerate(range(len_list), start=1):
            if next_idx >= len_list:
                break
            value, next_value = list_to_sort[idx], list_to_sort[next_idx]
            if value > next_value:
                list_to_sort[idx], list_to_sort[next_idx] = next_value, value
                changed = True

    return list_to_sort


if __name__ == "__main__":
    print(sort([20, 20, 30, 30, 1, 2, 3, 55]))
    print(b_sort([20, 20, 30, 30, 1, 2, 3, 55]))
