import pandas as pd
import time
import os

# Dynamically resolve correct file path regardless of execution context
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "user_events.csv")

# Simulated Kafka-like stream of events
new_events = [
    {"user_id": 1, "product_id": 104, "rating": 4},
    {"user_id": 2, "product_id": 105, "rating": 5},
    {"user_id": 5, "product_id": 101, "rating": 5},
]

def append_new_events():
    if not os.path.exists(DATA_PATH):
        print(f"❌ File not found: {DATA_PATH}")
        return

    df = pd.read_csv(DATA_PATH)
    print(f"📄 Original events loaded: {len(df)} rows")

    print("📡 Injecting new events...")
    for event in new_events:
        df = df._append(event, ignore_index=True)
        print(f"🟢 Added: {event}")
        time.sleep(1)

    df.to_csv(DATA_PATH, index=False)
    print(f"✅ All events written to file: {DATA_PATH}")
    print(f"📈 Total events after injection: {len(df)} rows")

if __name__ == "__main__":
    append_new_events()
