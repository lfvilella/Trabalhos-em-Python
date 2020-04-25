def show_statistic(days):
    for item in zip(*days.values()):
        print(f'Min = {min(item)}, Max = {max(item)}, Average = {sum(item) / len(item):4.1f}')


if __name__ == "__main__":
    days = {
        'sunday': [24, 25, 26, 26, 33],
        'monday': [25, 24, 22, 30, 30],
        'tuesday': [20, 16, 18, 23, 23],
    }
    show_statistic(days)
