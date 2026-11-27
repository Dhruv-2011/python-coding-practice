import pandas as pd

telemetry = pd.DataFrame({
    "Subsystem": ["Drivetrain", "Shooter", "Intake", "Drivetrain", "Shooter", "Intake", "Drivetrain"],
    "Battery_V": list((12.4, 11.8, 12.6, 11.9, 11.2, 12.5, 12.1)),
    "Current_A": list((18.5, 34.0, 12.2, 22.1, 38.5, 11.8, 19.4)),
    "Temp_C": list((32.0, 48.5, 28.0, 35.5, 54.0, 29.1, 33.8))
})

# 1. Add calculated column "Power_W"
telemetry["Power_W"] = telemetry["Battery_V"] * telemetry["Current_A"]

# 2. Compute mean of "Power_W" and max of "Temp_C" for each subsystem
summary = telemetry.groupby("Subsystem").agg({
    "Power_W": "mean",
    "Temp_C": "max"
}).reset_index()

# 3. Sort by "Temp_C" descending so the hottest subsystem appears first
summary = summary.sort_values(by="Temp_C", ascending=False)

print(summary)