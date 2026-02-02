def ft_harvest_total():
    total: int = 0
    i = 0
    while i < 3:
        total += int(input(f"Day {i+1} harvest: "))
        i += 1
    print(f"Total harvest: {total}")
