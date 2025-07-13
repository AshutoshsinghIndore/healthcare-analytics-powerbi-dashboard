import pandas as pd

if __name__ == '__main__':
    df = pd.DataFrame({'name' : ['Dummy']})
    df.to_csv(r'../Dummy.csv')