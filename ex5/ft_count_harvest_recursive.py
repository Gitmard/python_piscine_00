def ft_count_harvest_recursive(n: int = -1, i: int = 0):
    if (n == -1):
        n = int(input("Days until harvest: "))
        if (n < 0):
            n = 0
    if (i == n):
        print("Harvest time !")
        return
    print(f"Day {i + 1}")
    ft_count_harvest_recursive(n, i + 1)
