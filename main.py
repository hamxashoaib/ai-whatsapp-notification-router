import pandas as pd

from loader import load_data
from predictor import predict


def main():

    print("=" * 60)
    print("Loading dataset...")
    print("=" * 60)

    data = load_data()

    print("Dataset loaded successfully.\n")

    print("=" * 60)
    print("Running AI Notification Routing...")
    print("=" * 60)

    predictions = predict(data)

    output = pd.DataFrame(predictions)

    output.to_csv("output.csv", index=False)

    print("\n✅ output.csv generated successfully!\n")

    print("First 5 Predictions:\n")
    print(output.head())


if __name__ == "__main__":
    main()