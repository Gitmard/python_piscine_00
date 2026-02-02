def ft_harvest_total():
    total: int = 0
    for i in range(3):
        total += int(input(f"Day {i+1} harvest: "))
    print(f"Total harvest: {total}")
