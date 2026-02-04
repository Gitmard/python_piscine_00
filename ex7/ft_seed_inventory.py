def ft_seed_inventory(seed_type: str, quantity: int, unit: str)->None:
    if not unit in ["packets",  "grams", "area"]:
        print("Unknown unit type")
        return ;
    quantity_str: str
    if unit == "packets":
        quantity_str = f"{quantity} packets available"
    elif unit == "grams":
        quantity_str = f"{quantity} grams total"
    else:
        quantity_str = f"covers {quantity} square meters"
    print(f"{seed_type.capitalize()} seeds: {quantity_str}")
