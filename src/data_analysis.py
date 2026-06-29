import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    return df

def expense_summary(df):
    total = df['amount'].sum()
    category = df.groupby('category')['amount'].sum()
    
    return total, category

if __name__ == "__main__":
    df = load_data("data/finance_data.csv")
    
    total, category = expense_summary(df)
    
    print("Total Expenses:", total)
    print("\nCategory Wise Expenses:")
    print(category)