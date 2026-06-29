def investment_split(savings, age):

    if savings <= 0:
        return 0, 0

    mf_percent = max(0, 100 - age)
    fd_percent = age

    mf_amount = savings * (mf_percent / 100)
    fd_amount = savings * (fd_percent / 100)

    return mf_amount, fd_amount
