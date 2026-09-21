import math
import pandas as pd

df = pd.read_csv("data/funnel_events.csv")
print("Funnel totals:")
print(df[["visited","signed_up","activated","converted"]].sum().to_string())

ab = df.groupby("variant")["converted"].agg(["sum","count"])
ab["conversion_rate"] = ab["sum"] / ab["count"]
print("\nA/B conversion:")
print(ab.to_string())

c, t = ab.loc["control"], ab.loc["treatment"]
p_pool = (c["sum"] + t["sum"]) / (c["count"] + t["count"])
se = math.sqrt(p_pool * (1-p_pool) * (1/c["count"] + 1/t["count"]))
z = (t["conversion_rate"] - c["conversion_rate"]) / se if se else 0
print(f"\nTwo-proportion z statistic: {z:.3f}")
