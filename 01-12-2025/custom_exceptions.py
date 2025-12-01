class LowBalanceError(Exception):
    pass

def withdraw(ac, bl):
    if ac>bl:
        raise LowBalanceError("Insufficient funds")
    return bl-ac

print(withdraw(170, 100))