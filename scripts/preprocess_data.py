import pandas as pd

def preprocess():
    df = pd.read_csv("data/Dataset_Health.csv")

    df = df.fillna(df.median(numeric_only=True))
    df.to_csv("data/Dataset_Health_clean.csv", index=False)
    print("Preprocessed dataset saved to data/Dataset_Health_clean.csv")

if __name__ == "__main__":
    preprocess()
