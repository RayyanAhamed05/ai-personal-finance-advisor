def calculate_emi(principal, rate, time):

    if rate == 0:
        return principal / (time * 12)

    r = rate / (12 * 100)
    n = time * 12

    emi = (principal * r * (1 + r)**n) / ((1 + r)**n - 1)

    return emi