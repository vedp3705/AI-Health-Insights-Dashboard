import pandas as pd

def load_data():
    df = pd.read_csv("data/Dataset_Health.csv")
    print(f"Loaded dataset with shape: {df.shape}")
    return df

if __name__ == "__main__":
    df = load_data()
    df.to_csv("output/raw_data_copy.csv", index=False)
    print("Data loaded and saved to output/raw_data_copy.csv")