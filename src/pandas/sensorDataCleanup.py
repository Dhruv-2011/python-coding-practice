
#2. Messy Sensor Data Cleanup (Data Cleaning)
#Scenario: You receive a noisy sensor log with missing values, inconsistent text, and duplicate rows:
#python
import pandas as pd

raw_data = {
    "Sensor_ID": ["S1", "S2", "S2", "S3", "S4", "S5"],
    "Status": ["active", "ACTIVE", "ACTIVE", "inactive", "Active", "inactive"],
    "Temp_C": list((22.5, None, None, 19.0, 24.1, None))
}

#Tasks:
#Create a DataFrame and remove duplicate rows.
#Standardize the "Status" column so all values are lowercase ("active" / "inactive").
#Fill the missing None values in "Temp_C" with the average temperature of the valid readings.
# Convert data to Dataframe
df = pd.DataFrame(raw_data)
#Made all characters in Status column lowercase
df["Status"] = df["Status"].str.lower()
print(df)

#Found mean
mean = df["Temp_C"].mean(numeric_only=True)
df["Temp_C"] = df["Temp_C"].fillna(mean)
print(df)
