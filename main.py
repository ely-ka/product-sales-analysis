import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Create Data
# -----------------------------

data = {
    "Product_Name": [
        "Laptop",
        "Mobile",
        "Headphone",
        "Smartwatch",
        "Keyboard"
    ],

    "Product_ID": [
        "P101", "P102", "P103", "P104", "P105"
    ],

    "Category": [
        "Electronics",
        "Electronics",
        "Accessories",
        "Wearable",
        "Accessories"
    ],

    "Cost_Price": [
        25000000, 12000000, 1500000, 3000000, 800000
    ],

    "Selling_Price": [
        30000000, 15000000, 2000000, 4000000, 1000000
    ],

    "Discount_Percent": [
        10, 5, 15, 10, 20
    ],

    "Sales_Count": [
        15, 30, 20, 10, 25
    ],

    "Sales_Date": [
        "2026-10-02",
        "2026-10-05",
        "2026-10-10",
        "2026-10-15",
        "2026-10-20"
    ],

    "City": [
        "Tehran",
        "Shiraz",
        "Isfahan",
        "Mashhad",
        "Tabriz"
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# 2. Display Data
# -----------------------------

print(df)
print(df.info())
print(df.describe())

# -----------------------------
# 3. Calculate Final Price
# -----------------------------

df["Final_Price"] = (
    df["Selling_Price"] *
    (1 - df["Discount_Percent"] / 100)
)

# -----------------------------
# 4. Calculate Total Sales
# -----------------------------

df["Total_Sales"] = (
    df["Final_Price"] *
    df["Sales_Count"]
)

total_monthly_sales = df["Total_Sales"].sum()

print("Total Monthly Sales:", total_monthly_sales)

# -----------------------------
# 5. Sales of Each Product
# -----------------------------

product_sales = df.groupby(
    "Product_Name"
)["Total_Sales"].sum()

print("\nSales of Each Product:")
print(product_sales)

# -----------------------------
# 6. Best Selling Product
# -----------------------------

best_selling_product = df.loc[
    df["Sales_Count"].idxmax()
]

print("\nBest Selling Product:")
print(best_selling_product["Product_Name"])

# -----------------------------
# 7. Worst Selling Product
# -----------------------------

worst_selling_product = df.loc[
    df["Sales_Count"].idxmin()
]

print("\nWorst Selling Product:")
print(worst_selling_product["Product_Name"])

# -----------------------------
# 8. Monthly Sales Data
# -----------------------------

monthly_data = {
    "Month": [
        "May",
        "June",
        "July",
        "August",
        "September",
        "October"
    ],

    "Sales": [
        65, 80, 75, 90, 85, 100
    ]
}

monthly_df = pd.DataFrame(monthly_data)

# -----------------------------
# 9. Calculate Monthly Average
# -----------------------------

monthly_average = monthly_df["Sales"].mean()

print("\nMonthly Average Sales:", monthly_average)

# =====================================
# 10. Display All Three Charts Together
# =====================================

fig, axes = plt.subplots(1, 3, figsize=(20, 6))

# -----------------------------
# Chart 1: Bar Chart
# -----------------------------

axes[0].bar(
    df["Product_Name"],
    df["Sales_Count"],
    color="skyblue",
    edgecolor="black"
)

axes[0].set_title("Product Sales Quantity")
axes[0].set_xlabel("Product Name")
axes[0].set_ylabel("Sales Count")
axes[0].tick_params(axis="x", rotation=45)
axes[0].grid(axis="y", linestyle="--", alpha=0.5)

# -----------------------------
# Chart 2: Pie Chart
# -----------------------------

axes[1].pie(
    df["Sales_Count"],
    labels=df["Product_Name"],
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)

axes[1].set_title("Percentage Share of Total Product Sales")

# -----------------------------
# Chart 3: Line Chart
# -----------------------------

axes[2].plot(
    monthly_df["Month"],
    monthly_df["Sales"],
    marker="o",
    color="green",
    linewidth=2
)

axes[2].axhline(
    y=monthly_average,
    color="red",
    linestyle="--",
    label="Average Sales"
)
axes[2].set_title("Monthly Average Sales Trend")
axes[2].set_xlabel("Month")
axes[2].set_ylabel("Sales Quantity")
axes[2].tick_params(axis="x", rotation=45)
axes[2].legend()
axes[2].grid(True, linestyle="--", alpha=0.5)

# -----------------------------
# 11. Show All Charts
# -----------------------------

plt.tight_layout()
plt.show()

print("\nAll Charts Displayed Successfully!")