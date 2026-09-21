from pathlib import Path
import random
import pandas as pd

random.seed(42)
rows = []
channels = ["Organic","Paid Search","Social","Referral"]
for i in range(5000):
    variant = random.choice(["control","treatment"])
    signup = random.random() < 0.48
    activated = signup and random.random() < 0.70
    base_conversion = 0.31 if variant == "control" else 0.36
    converted = activated and random.random() < base_conversion
    rows.append({
        "user_id": f"U{i+1:05d}",
        "channel": random.choice(channels),
        "variant": variant,
        "visited": 1,
        "signed_up": int(signup),
        "activated": int(activated),
        "converted": int(converted)
    })

Path("data").mkdir(exist_ok=True)
pd.DataFrame(rows).to_csv("data/funnel_events.csv", index=False)
print("Synthetic funnel dataset created.")
