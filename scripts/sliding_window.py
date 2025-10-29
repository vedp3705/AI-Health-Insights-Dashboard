import pandas as pd

def create_sliding_windows(df, window_size=5):
    windows = []
    for i in range(len(df) - window_size + 1):
        window = df.iloc[i:i + window_size].mean()
        windows.append(window)
    return pd.DataFrame(windows)

if __name__ == "__main__":
    df = pd.read_csv("output/preprocessed_data.csv")
    windowed = create_sliding_windows(df, window_size=5)
    windowed.to_csv("output/features_windowed.csv", index=False)
    print("Sliding window features saved to output/features_windowed.csv")