from loader import load_data

data = load_data()

print("✅ Dataset Loaded Successfully\n")

for name, df in data.items():
    print(f"{name}: {len(df)} rows")