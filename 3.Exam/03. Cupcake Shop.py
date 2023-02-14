def stock_availability(inventory, command, *args):
    if command == "delivery":
        return inventory + list(args)

    elif command == "sell":
        if len(args) == 0:
            return inventory[1:]

        elif isinstance(args[0], int):
            return inventory[args[0]:]

        else:
            for flavour in args:
                if flavour in inventory:
                    while flavour in inventory:
                        inventory.remove(flavour)
    return inventory
