import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_excel('Project 2.xlsx')

# To Print the entire DataFrame without truncation
print(df.to_string())

# Total records in DataSet
print("Total Records:",(len(df)))

# Columns Name 
print("Columns Name:",df.columns.tolist())

# Finding Missing Values
print("Missing Values:",df.isnull().sum())

# Total Sales Amount
print("Total Sales Amount:", df["TotalPrice"].sum())

# Mean order value
print("Mean Order Value:", df["TotalPrice"].mean())

# Maximum Order Value
print("Maximum Order Value:", df["TotalPrice"].max())

# Minimum Order Value
print("Minimum Order Value:", df["TotalPrice"].min())

# Most Sold Item
print("Most Sold Item:", df.groupby("Product")["Quantity"].sum().sort_values(ascending=False).index[0])

# Highest Revenue Generating Product
print("Highest Revenue Generating Product:", df.groupby("Product")["TotalPrice"].sum().sort_values(ascending=False))

# Most Used Payment Method
print("Most Used Payment Method:", df.groupby("PaymentMethod")["TotalPrice"].sum().sort_values(ascending=False))

# Most frequently order Status
print("Most Frequently Order Status:", df.groupby("OrderStatus")["TotalPrice"].sum().sort_values(ascending=False))

# Most referal Source
print("Most Referral Source:", df.groupby("ReferralSource")["TotalPrice"].sum().sort_values(ascending=False))


# Visualizations Product wise Sales
product_sales = df.groupby("Product")["TotalPrice"].sum()

plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()


# Visualizations Payment Method 
df["PaymentMethod"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(6,6)
)
plt.title("Payment Method Distribution")
plt.ylabel("")
plt.show()



# Order Status 
df["OrderStatus"].value_counts().plot(kind="bar")
plt.title("Order Status")
plt.xlabel("Status")
plt.ylabel("Count")
plt.show()

# Sales trend
df["Date"] = pd.to_datetime(df["Date"])

daily_sales = df.groupby("Date")["TotalPrice"].sum()

plt.figure(figsize=(10,5))
daily_sales.plot()
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()