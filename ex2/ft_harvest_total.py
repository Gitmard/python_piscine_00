def ft_harvest_total():
    harvests: list = []
    total: int = 0
    for i in range(3):
        harvests.append(int(input(f"Day {i+1} harvest: ")))
    for day in harvests:
        total += day
    print(f"Total harvest: {total}")
