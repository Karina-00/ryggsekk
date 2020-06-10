def heuristic(capacity, items):
    """
    This function performs heuristic, greedy solution to the knapsack problem
    based on the value-to-size ratio.
    """

    items.sort(key=lambda el: el.desire, reverse=False)

    solution = []

    _size = 0

    while _size < capacity and items:
        taken = items.pop()
        _size += taken.size             # calculate the value of the knapsack/container
        solution.append(taken)

    if _size > capacity:
        _size -= solution.pop().size    # get rid of the surplus element

    print(
        "\nsize", _size,
        "\nvalue", sum([i.value for i in solution])
    )

    return solution
