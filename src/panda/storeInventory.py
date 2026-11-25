import pandas as pd
#asks:
#Convert data into a DataFrame df and add a new calculated column "Total_Value" equal to Price * Stock.
#Filter and print only the rows where "Category" is "Accessories" AND "Price" is under 80
#Use .loc to update the "Stock" of "Laptop" to 10 (or set "Item" as the index first, then use df.loc["Laptop", "Stock"] = 10).

data = {
    "Item": ["Laptop", "Mouse", "Keyboard", "Monitor", "USB Cable", "Webcam"],
    "Category": ["Computers", "Accessories", "Accessories", "Displays", "Accessories", "Accessories"],
    "Price": list((1200, 25, 75, 300, 12, 85)),
    "Stock": list((4, 30, 15, 6, 50, 8))
}
#converted data into DataFrame
df = pd.DataFrame(data)
#Added Total_Value Collumn
df["Total_Value"] = df["Price"] * df["Stock"]

# Filter to show Accessories under 80 dollars
filtered_df = df[(df["Category"] == "Accessories")
        & (df["Price"] < 80)]
print(filtered_df)

# Updated Computer Stock to 10
df = df.set_index("Item")
df.loc["Laptop", "Stock"] = 10
print(df)
