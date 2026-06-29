def recommend_budget(income):

    budget = {}

    budget["Savings"] = income * 0.30
    budget["Rent"] = income * 0.30
    budget["Food"] = income * 0.15
    budget["Utilities"] = income * 0.10
    budget["Other"] = income * 0.15

    return budget


if __name__ == "__main__":

    income = 30000

    plan = recommend_budget(income)

    print("Recommended Budget")

    for k,v in plan.items():
        print(k,":",v)