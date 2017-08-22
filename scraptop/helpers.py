
def string2integer(price):
    return int("".join(list(filter(lambda x: x.isdigit(), price))))