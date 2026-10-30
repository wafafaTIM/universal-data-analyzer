import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV file
df = pd.read_csv("data/sales_data_messy.csv.csv")

# Step 2: Display dataset
print("\n===== ORIGINAL DATA =====")
print(df)

# Step 3: Display basic information
print("\n===== DATA INFORMATION =====")
print(df.info())

# Step 4: Display rows and columns
print("\n===== DATA SHAPE =====")
print(df.shape)

# Step 5: Display column names
print("\n===== COLUMN NAMES =====")
print(df.columns)

# Step 6: Display missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())
# Step 7: Check duplicate records

print("\n===== DUPLICATE RECORDS =====")

print("Total Duplicate Rows:", df.duplicated().sum())
# Step 8: Remove duplicate records

df = df.drop_duplicates()

print("\n===== AFTER REMOVING DUPLICATES =====")
print("Total Rows:", len(df))
print("Duplicates Remaining:", df.duplicated().sum())
# Step 9: Remove extra spaces

columns = ["Order_ID", "Product", "Category", "Region"]

for col in columns:
    df[col] = df[col].str.strip()

print("\n===== AFTER REMOVING EXTRA SPACES =====")
print(df[["Order_ID", "Product", "Category", "Region"]])
# Step 10: Convert text into title case

columns = ["Product", "Category", "Region"]

for col in columns:
    df[col] = df[col].str.title()

print("\n===== AFTER TITLE CASE =====")
print(df[["Product", "Category", "Region"]])
# Step 11: Convert Order_Date into datetime

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

print("\n===== DATE CLEANING =====")
print("Invalid Dates:", df["Order_Date"].isna().sum())
print(df[["Order_ID", "Order_Date"]])
# Step 12: Convert columns into numeric values

df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors="coerce")

print("\n===== NUMERIC DATA CHECK =====")
print(df[["Quantity", "Unit_Price"]].isnull().sum())
print(df[["Quantity", "Unit_Price"]].dtypes)
# Step 13: Remove rows with missing values

before_cleaning = len(df)

df = df.dropna()

removed_rows = before_cleaning - len(df)

print("\n===== AFTER REMOVING MISSING VALUES =====")
print("Rows Removed:", removed_rows)
print("Remaining Rows:", len(df))
print("Missing Values:")
print(df.isnull().sum())
# Step 14: Remove non-positive values

before = len(df)

df = df[(df["Quantity"] > 0) & (df["Unit_Price"] > 0)]

print("\n===== AFTER REMOVING NON-POSITIVE VALUES =====")
print("Rows Removed:", before - len(df))
print("Remaining Rows:", len(df))
# Step 15: Calculate Revenue

df["Revenue"] = df["Quantity"] * df["Unit_Price"]

print("\n===== REVENUE CALCULATION =====")
print(df[["Order_ID", "Product", "Quantity", "Unit_Price", "Revenue"]])
# Step 16: Sort data by date and Order ID

df = df.sort_values(
    by=["Order_Date", "Order_ID"]
).reset_index(drop=True)

print("\n===== SORTED CLEAN DATA =====")
print(df)
# Step 17: Save cleaned data to CSV

df.to_csv("output/cleaned_sales_data.csv", index=False)

print("\n===== FILE SAVED SUCCESSFULLY =====")
print("Cleaned file: output/cleaned_sales_data.csv")
# Step 18: Sales Analysis

print("\n===== SALES ANALYSIS =====")

print("Total Orders:", len(df))

print("Total Units Sold:", df["Quantity"].sum())

print("Total Revenue:", df["Revenue"].sum())

print("Average Revenue per Order:", df["Revenue"].mean())

print("Mean Unit Price:", df["Unit_Price"].mean())

print("Median Unit Price:", df["Unit_Price"].median())
# Step 19: Category-wise Sales Analysis

category_sales = df.groupby("Category")["Revenue"].sum()

category_sales = category_sales.sort_values(ascending=False)

print("\n===== CATEGORY-WISE SALES =====")
print(category_sales)
# Step 20: Region-wise Sales Analysis

region_sales = df.groupby("Region")["Revenue"].sum()

region_sales = region_sales.sort_values(ascending=False)

print("\n===== REGION-WISE SALES =====")
print(region_sales)
# Step 21: Product-wise Sales Analysis

product_sales = df.groupby("Product")["Revenue"].sum()

product_sales = product_sales.sort_values(ascending=False)

print("\n===== PRODUCT-WISE SALES =====")
print(product_sales)
# Step 22: Highest and Lowest Order Analysis

highest_order = df.loc[df["Revenue"].idxmax()]
lowest_order = df.loc[df["Revenue"].idxmin()]

print("\n===== HIGHEST REVENUE ORDER =====")
print(highest_order)

print("\n===== LOWEST REVENUE ORDER =====")
print(lowest_order)
# Step 23: Category-wise Revenue Chart

plt.figure(figsize=(8, 5))

category_sales.plot(kind="bar", color="skyblue")

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (PKR)")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("output/revenue_by_category.png")
plt.show()

print("Category chart saved successfully.")
# Step 24: Region-wise Revenue Chart

plt.figure(figsize=(8, 5))

region_sales.plot(kind="bar", color="orange")

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (PKR)")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("output/revenue_by_region.png")
plt.show()

print("Region chart saved successfully.")